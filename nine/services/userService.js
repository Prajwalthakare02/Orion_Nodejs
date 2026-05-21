import ApiError from '../errors/ApiError.js';

const users = [];
let nextId = 1;

export const getUsers = async () => users;

export const createUser = async (userData) => {
  const existingUser = users.find((user) => user.email === userData.email);

  if (existingUser) {
    throw new ApiError(409, 'A user with this email already exists');
  }

  const newUser = {
    id: String(nextId++),
    name: userData.name,
    email: userData.email,
    createdAt: new Date().toISOString()
  };

  users.push(newUser);

  return newUser;
};

export const getUserById = async (id) => {
  const user = users.find((entry) => entry.id === id);

  if (!user) {
    throw new ApiError(404, `User with id ${id} not found`);
  }

  return user;
};