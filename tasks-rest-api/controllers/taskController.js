import { tasksTable } from '../config/database.js';
import { Task } from '../models/taskModel.js';

// @desc    Get all stored tasks
// @route   GET /api/tasks
export const getAllTasks = (req, res) => {
    res.status(200).json(tasksTable);
};

// @desc    Get a single task by ID
// @route   GET /api/tasks/:id
export const getTaskById = (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasksTable.find(t => t.id === taskId);

    if (!task) {
        return res.status(404).json({ error: `Resource Exception: Task with ID ${taskId} not found.` });
    }
    res.status(200).json(task);
};

// @desc    Create a new task documentation item
// @route   POST /api/tasks
export const createTask = (req, res) => {
    const { title } = req.body;

    if (!title || title.trim() === "") {
        return res.status(400).json({ error: "Validation Failure: 'title' attribute is required and cannot be blank." });
    }

    const newTask = new Task(title.trim());
    tasksTable.push(newTask);
    
    res.status(201).json(newTask); // 201 Created status code mapping
};

// @desc    Update an existing task configuration item
// @route   PUT /api/tasks/:id
export const updateTask = (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasksTable.find(t => t.id === taskId);

    if (!task) {
        return res.status(404).json({ error: `Resource Exception: Cannot update task. ID ${taskId} does not exist.` });
    }

    const { title, completed } = req.body;

    // Conditionally update task attributes depending on what parameters were passed
    if (title !== undefined) task.title = title.trim();
    if (completed !== undefined) task.completed = typeof completed === 'boolean' ? completed : task.completed;

    res.status(200).json({ message: "Task update synchronized successfully.", task });
};

// @desc    Delete a target task document boundary
// @route   DELETE /api/tasks/:id
export const deleteTask = (req, res) => {
    const taskId = parseInt(req.params.id);
    const taskIndex = tasksTable.findIndex(t => t.id === taskId);

    if (taskIndex === -1) {
        return res.status(404).json({ error: `Resource Exception: Cannot delete task. ID ${taskId} not found.` });
    }

    const removedTask = tasksTable.splice(taskIndex, 1);
    res.status(200).json({ message: "Task dropped from repository cleanly.", task: removedTask[0] });
};