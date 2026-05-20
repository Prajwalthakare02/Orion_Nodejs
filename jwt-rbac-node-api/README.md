# JWT Authentication and RBAC in Node.js

This app demonstrates a complete authentication and authorization flow using JWT, bcryptjs, MongoDB, and Express.

## Install

```bash
npm install
```

Create a `.env` file from `.env.example` and set:

- `MONGO_URI`
- `JWT_SECRET`
- `JWT_EXPIRES_IN`

## How it works

- `bcryptjs` hashes passwords before they are stored.
- `jsonwebtoken` creates a token that embeds the user ID and role.
- `protect` reads the Bearer token from the `Authorization` header, verifies it, and loads the current user.
- `authorize` checks whether the authenticated user has one of the allowed roles.

## User model

The `User` model stores `name`, `email`, `password`, and `role`.

- `password` is hidden by default with `select: false`.
- `role` is restricted to `user` or `admin`.

## Register and login

`POST /api/auth/register`

- hashes the password with `bcryptjs`
- creates the user with a role
- returns a JWT token

`POST /api/auth/login`

- loads the stored password with `.select('+password')`
- compares the password with `bcryptjs.compare`
- returns a JWT token if credentials are valid

## Protected routes

All task routes require a Bearer token.

- `POST /api/tasks` is available to `user` and `admin`
- `DELETE /api/tasks/:id` is limited to `admin`

## Example requests

Register:

```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Ava\",\"email\":\"ava@example.com\",\"password\":\"secret123\",\"role\":\"user\"}"
```

Login:

```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"ava@example.com\",\"password\":\"secret123\"}"
```

Create task as a user or admin:

```bash
curl -X POST http://localhost:3000/api/tasks \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Finish docs\",\"description\":\"Write the auth guide\"}"
```

Delete task as an admin:

```bash
curl -X DELETE http://localhost:3000/api/tasks/TASK_ID \
  -H "Authorization: Bearer ADMIN_TOKEN"
```
