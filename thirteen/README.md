# Thirteen - Deployment and Production Readiness of Backend Applications

This folder explains how a backend application is prepared for production and includes a small Express scaffold that demonstrates the production setup patterns used in real deployments.

## 1. Environment Configuration

Production applications should load configuration from environment variables rather than hardcoding secrets.

Typical values include:

- `MONGO_URI` for the database connection string
- `JWT_SECRET` for token signing
- `JWT_EXPIRES_IN` for token lifetime
- `PORT` for the server port
- `NODE_ENV` for runtime-specific behavior

Best practices:

- Keep secrets in `.env` files locally.
- Never commit `.env` to version control.
- Commit only `.env.example` so teammates know which variables are required.
- Use separate values for development, staging, and production.

## 2. Production Optimization

The backend is tuned for production by applying middleware and runtime settings that improve security and reliability.

Recommended settings:

- Limit JSON payload size with `express.json({ limit: '1mb' })` or similar.
- Enable `trust proxy` when running behind a load balancer or reverse proxy.
- Use `helmet` for secure HTTP headers.
- Use `cors` with explicit allowed origins.
- Use `compression` to reduce response payload size.
- Use `morgan` or structured logging for request tracing.

Why this matters:

- Smaller payload limits reduce abuse risk.
- `trust proxy` ensures correct client IP and HTTPS awareness.
- Helmet and CORS reduce common web security risks.
- Compression improves bandwidth usage and response times.

## 3. Centralized Error Handling and Logging

Production systems should return consistent error responses from one central handler.

Benefits:

- Prevents leaking internal stack traces to clients
- Makes failures easier to monitor and debug
- Gives the frontend a stable error format

Structured logging is equally important because it helps track:

- request method and URL
- response status code
- latency
- errors and stack traces in non-production environments

## 4. Deployment Flow

Typical cloud deployment steps:

1. Push the code to GitHub.
2. Provision a server or use a platform like Render, DigitalOcean, or AWS.
3. Install Node.js and dependencies on the target environment.
4. Configure environment variables securely on the platform.
5. Set up the start command such as `npm start`.
6. Use a process manager such as PM2 when running on a VM or bare server.
7. Verify the live API with smoke tests and real endpoints.

## 5. PM2 for Reliability

PM2 is commonly used to keep Node.js applications running in production.

It helps with:

- automatic restarts after crashes
- process monitoring
- log management
- cluster mode for multi-core usage

Example usage:

```bash
pm2 start server.js --name thirteen-api
pm2 save
pm2 startup
```

## 6. Testing Deployed APIs

Once deployed, APIs should be tested against live endpoints.

Focus areas:

- authentication: register, login, token-protected access
- pagination: page and limit parameters
- RBAC: admin-only routes and user-only routes
- error cases: invalid tokens, expired tokens, bad payloads

Suggested checks:

- `GET /` returns a healthy response
- `POST /api/auth/login` returns a JWT for valid credentials
- `GET /api/products?page=1&limit=10` returns paginated data
- `POST /api/admin/products` rejects non-admin users

## 7. Common Deployment Mistakes

Common mistakes include:

- committing `.env` files
- using development secrets in production
- forgetting to set `NODE_ENV=production`
- not enabling a proxy-aware configuration
- exposing debug logs or stack traces publicly
- not validating that the database and JWT settings exist
- ignoring health checks after deployment

## 8. Production Best Practices

- Use separate environments for development, staging, and production.
- Store secrets in environment variables or a cloud secrets manager.
- Apply rate limiting and input validation.
- Keep response payloads small.
- Log requests and failures consistently.
- Monitor uptime, latency, and error rates.
- Test the live deployment after every release.

## 9. Scaffold Overview

This folder includes a small Express app that demonstrates the above ideas with production middleware, centralized errors, a health endpoint, and MongoDB connectivity.
