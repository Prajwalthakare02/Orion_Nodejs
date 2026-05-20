const express = require('express');
const userRoutes = require('./routes/userRoutes');

const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Main User API routes
app.use('/api/users', userRoutes);

// 404 Route handling
app.use((req, res, next) => {
    res.status(404).json({ message: 'API Endpoint not found' });
});

// Global error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'An unexpected error occurred!' });
});

module.exports = app;