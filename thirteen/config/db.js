import mongoose from 'mongoose';

export default async function connectDb(uri) {
  if (!uri) {
    throw new Error('MONGO_URI is required');
  }

  await mongoose.connect(uri, {
    autoIndex: process.env.NODE_ENV !== 'production'
  });

  console.log('MongoDB connected');
}
