import dotenv from 'dotenv';
import app from './app.js';
import connectDb from './config/db.js';

dotenv.config();

const PORT = process.env.PORT || 3000;

async function startServer() {
  await connectDb(process.env.MONGO_URI);

  app.listen(PORT, () => {
    console.log(`Thirteen app listening on port ${PORT}`);
  });
}

startServer().catch((error) => {
  console.error('Unable to start server:', error.message);
  process.exit(1);
});
