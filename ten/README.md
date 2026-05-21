# Ten — Practical API Performance Optimization Strategy

This example demonstrates strategies from Module 10: Performance Optimization in Practice. It shows how to integrate response compression, in-memory and Redis caching, and MongoDB query optimizations for a high-traffic `/api/users` endpoint.

Files of interest:

- `app.js` — Express app and middleware (including `compression`).
- `routes/users.js` — API route exposing `GET /api/users` with pagination and field selection.
- `controllers/userController.js` — Request flow, cache lookup, DB fallback, cache set.
- `cache/memoryCache.js` — Simple in-memory cache using `node-cache`.
- `cache/redisClient.js` — Redis client wrapper (uses `REDIS_URL` env).
- `models/User.js` — Mongoose model with recommended indexes.
- `config/db.js` — MongoDB connection helper.

How to run (locally):

1. Set environment variables in a `.env` file at the root of `ten`:

```
MONGO_URI=mongodb://localhost:27017/ten_example
REDIS_URL=redis://localhost:6379
PORT=3003
```

2. Install and run:

```powershell
cd d:/Codding/Project/orion/ten
npm install
$env:PORT='3003'
node server.js
```

Notes:

- If Redis is not available the app gracefully falls back to in-memory caching.
- The README below (in code) explains the request flow and measurement guidance.
