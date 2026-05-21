import Redis from 'ioredis';

let client = null;

export function createRedis(url) {
  if (!url) return null;
  client = new Redis(url);
  client.on('error', (err) => console.error('Redis error', err));
  return client;
}

export function getRedis() {
  return client;
}
