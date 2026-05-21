import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
  name: String,
  email: { type: String, index: true },
  role: String,
  createdAt: { type: Date, default: Date.now, index: true }
});

// compound indexes can be added for common query shapes
UserSchema.index({ role: 1, createdAt: -1 });

export default mongoose.model('User', UserSchema);
