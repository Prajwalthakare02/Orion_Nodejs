const Task = require('../models/Task');

const getAllTasks = async () => {
  // Populate the user reference
  return await Task.find().populate('user', 'name email');
};

const getTaskById = async (id) => {
  return await Task.findById(id).populate('user', 'name email');
};

const createTask = async (taskData) => {
  return await Task.create(taskData);
};

const updateTask = async (id, taskData) => {
  return await Task.findByIdAndUpdate(id, taskData, {
    new: true,
    runValidators: true,
  }).populate('user', 'name email');
};

const deleteTask = async (id) => {
  return await Task.findByIdAndDelete(id);
};

module.exports = {
  getAllTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask,
};