import asyncWrapper from '../middleware/asyncWrapper.js';
import { createUser, getUserById, getUsers } from '../services/userService.js';

export const listUsers = asyncWrapper(async (req, res) => {
  const users = await getUsers();

  res.status(200).json({
    status: 'success',
    results: users.length,
    data: { users }
  });
});

export const createUserController = asyncWrapper(async (req, res) => {
  const user = await createUser(req.body);

  res.status(201).json({
    status: 'success',
    data: { user }
  });
});

export const getUserController = asyncWrapper(async (req, res) => {
  const user = await getUserById(req.params.id);

  res.status(200).json({
    status: 'success',
    data: { user }
  });
});