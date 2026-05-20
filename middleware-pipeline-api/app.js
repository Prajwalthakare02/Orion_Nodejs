import express from 'express';
import cors from 'cors';
import helmet from 'helmet';

// Custom Middleware Modules Imports
import { requestLogger } from './middleware/logMiddleware.js';
import { checkAuthentication } from './middleware/authMiddleware.js';
import { validateTaskTitle } from './middleware/valMiddleware.js';

const app = express();

// Volatile local dataset mock repository
let databaseTasks = [
    { id: 1, title: "Review middleware documentation patterns", completed: true }
];

// ========================================================
// 1. GLOBAL MIDDLEWARE LAYER STACK (Executes for ALL requests)
// ========================================================

// Third-Party Security: Injects 15 secure HTTP headers automatically to harden the server footprint
app.use(helmet());

// Third-Party Access: Resolves Cross-Origin Resource Sharing boundaries for client interfaces
app.use(cors());

// Built-in Parser: Intercepts raw stream data buffers and parses them to req.body if content-type is JSON
app.use(express.json());

// Built-in Static Assets Server: Automatically routes incoming root GET requests to the public directory
app.use(express.static('public'));

// Custom Audit Logger: Processes real-time transaction tracking
app.use(requestLogger);


// ========================================================
// 2. PROTECTED ROUTING LAYER STACK (Using Route-Level Middleware)
// ========================================================

// GET /api/tasks -> Protected strictly by Authentication check middleware
app.get('/api/tasks', checkAuthentication, (req, res) => {
    res.status(200).json(databaseTasks);
});

// POST /api/tasks -> Composes multiple middleware levels sequentially (Auth check first, then structural Data validation)
app.post('/api/tasks', checkAuthentication, validateTaskTitle, (req, res) => {
    const newTaskItem = {
        id: databaseTasks.length + 1,
        title: req.body.title,
        completed: false
    };

    databaseTasks.push(newTaskItem);
    res.status(201).json({ message: "Task instantiated successfully.", data: newTaskItem });
});

// PUT /api/tasks/:id -> Composes multiple middleware levels sequentially
app.put('/api/tasks/:id', checkAuthentication, validateTaskTitle, (req, res) => {
    const targetId = parseInt(req.params.id);
    const selectedTask = databaseTasks.find(t => t.id === targetId);

    if (!selectedTask) {
        return res.status(404).json({ error: `Resource Exception: Target resource with identifier ${targetId} not found.` });
    }

    selectedTask.title = req.body.title;
    res.status(200).json({ message: "Task synchronized successfully.", data: selectedTask });
});

export default app;