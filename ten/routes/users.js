import { Router } from 'express';
import { getUsers } from '../controllers/userController.js';

const router = Router();

// GET /api/users?limit=20&page=1&fields=name,email
router.get('/', getUsers);

export default router;
