import { validationResult } from 'express-validator';
import ApiError from '../errors/ApiError.js';

const validationMiddleware = (req, res, next) => {
  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    return next(new ApiError(400, 'Validation failed', errors.array()));
  }

  return next();
};

export default validationMiddleware;