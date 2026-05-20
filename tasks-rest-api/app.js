import express from 'express';
import taskRouter from './routes/taskRoutes.js';

const app = express();

// Crucial Middleware: Configures Express to natively parse incoming application/json stream payloads
app.use(express.json());

// Bind our modular route configuration domain space to the base API path perimeter
app.use('/api/tasks', taskRouter);

// Fallback 404 security perimeter handler for unmapped routes
app.use((req, res) => {
    res.status(404).json({ error: "API routing parameter unmapped. Endpoint path pattern not found." });
});

export default app;