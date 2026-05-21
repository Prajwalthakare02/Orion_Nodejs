import { connectDb } from '../config/db.js';
import User from '../models/User.js';
import memoryCache from '../cache/memoryCache.js';
import { createRedis, getRedis } from '../cache/redisClient.js';
import mongoose from 'mongoose';

// initialize connections lazily
let redisClient = null;
let dbConnected = false;

async function ensureDb() {
  if (!dbConnected) {
    await connectDb(process.env.MONGO_URI || 'mongodb://localhost:27017/ten_example');
    dbConnected = true;
  }
}

function getCacheKey(q) {
  return `users:${JSON.stringify(q)}`;
}

export async function getUsers(req, res, next) {
  try {
    await ensureDb();

    // parse pagination and fields
    const limit = Math.min(parseInt(req.query.limit || '20', 10), 100);
    const page = Math.max(parseInt(req.query.page || '1', 10), 1);
    const skip = (page - 1) * limit;
    const fields = req.query.fields ? req.query.fields.split(',').join(' ') : 'name email role createdAt';

    const queryObj = { skip, limit, fields, q: req.query.q || '' };
    const cacheKey = getCacheKey(queryObj);

    // 1) Check in-memory cache
    const mem = memoryCache.get(cacheKey);
    if (mem) return res.json({ source: 'memory', ...mem });

    // 2) Check Redis (if configured)
    if (!redisClient && process.env.REDIS_URL) redisClient = createRedis(process.env.REDIS_URL);
    const redis = getRedis();
    if (redis) {
      const cached = await redis.get(cacheKey);
      if (cached) {
        const parsed = JSON.parse(cached);
        // warm memory cache for faster subsequent hits
        memoryCache.set(cacheKey, parsed, 30);
        return res.json({ source: 'redis', ...parsed });
      }
    }

    // 3) Database fallback with optimized query
    // - select only required fields
    // - use .lean() for faster read-only response objects
    // - use skip/limit for pagination
    const filter = {};
    if (req.query.q) filter.$text = { $search: req.query.q };

    const docs = await User.find(filter)
      .select(fields)
      .skip(skip)
      .limit(limit)
      .lean()
      .exec();

    const result = { total: docs.length, data: docs };

    // cache in Redis (5 minutes) and memory (30 seconds)
    if (redis) await redis.set(cacheKey, JSON.stringify(result), 'EX', 300);
    memoryCache.set(cacheKey, result, 30);

    return res.json({ source: 'db', ...result });
  } catch (err) {
    next(err);
  }
}
