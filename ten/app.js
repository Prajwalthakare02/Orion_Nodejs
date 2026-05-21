import express from 'express';
import compression from 'compression';
import morgan from 'morgan';
import userRouter from './routes/users.js';

const app = express();

// Compression middleware reduces payload sizes over the wire
app.use(compression());
app.use(express.json());
app.use(morgan('dev'));

app.use('/api/users', userRouter);

app.use((req, res) => res.status(404).json({ message: 'Not Found' }));

export default app;
