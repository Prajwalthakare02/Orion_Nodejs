import { Router } from 'express';
import {
  createUserController,
  getUserController,
  listUsers
} from '../controllers/userController.js';
import { createUserValidation } from '../validators/userValidators.js';

const router = Router();

router.get('/', listUsers);
router.get('/:id', getUserController);
router.post('/', createUserValidation, createUserController);

export default router;