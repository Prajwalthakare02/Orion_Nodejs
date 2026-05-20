const express = require('express');
const {
  getTasks,
  getTask,
  createTask,
  updateTask,
  deleteTask,
} = require('../controllers/taskController');
const { protect, authorize } = require('../middleware/authMiddleware');

const router = express.Router();

router.use(protect);

router.route('/').get(getTasks).post(authorize('user', 'admin'), createTask);

router
  .route('/:id')
  .get(getTask)
  .put(updateTask)
  .delete(authorize('admin'), deleteTask);

module.exports = router;
