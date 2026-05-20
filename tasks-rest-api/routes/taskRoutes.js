import express from 'express';
import { 
    getAllTasks, 
    getTaskById, 
    createTask, 
    updateTask, 
    deleteTask 
} from '../controllers/taskController.js';

const router = express.Router();

// Define endpoint mappings cleanly using Express routing pipelines
router.route('/')
      .get(getAllTasks)
      .post(createTask);

router.route('/:id')
      .get(getTaskById)
      .put(updateTask)
      .delete(deleteTask);

export default router;