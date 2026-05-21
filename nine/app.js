import express from 'express';
import userRouter from './routes/userRoutes.js';
import ApiError from './errors/ApiError.js';
import errorHandler from './middleware/errorHandler.js';

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.json({
    message: 'Centralized Error and Validation System API',
    routes: {
      users: '/api/users'
    }
  });
});

app.use('/api/users', userRouter);

app.use((req, res, next) => {
  next(new ApiError(404, `Route ${req.originalUrl} not found`));
});

app.use(errorHandler);

export default app;