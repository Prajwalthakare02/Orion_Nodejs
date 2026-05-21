# Nine - Centralized Error and Validation API

This project demonstrates a structured Node.js and Express implementation for centralized error handling and request validation.

## Features

- Global error-handling middleware
- Async controller wrapper
- Validation and sanitization with `express-validator`
- Custom service-layer errors for not found and duplicate users
- Route-level validation integration

## Start

```bash
npm install
npm run dev
```

## Endpoints

- `GET /` - API overview
- `GET /api/users` - list users
- `GET /api/users/:id` - get a user by id
- `POST /api/users` - create a user

## Example Request

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```