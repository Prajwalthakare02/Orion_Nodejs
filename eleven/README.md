# Eleven - Comprehensive Testing Strategy for User and Auth APIs

This folder contains a practical testing strategy for a Node.js application with User and Auth APIs. The goal is to clearly separate unit testing from integration testing and show how both work together to protect business logic, API contracts, and database behavior.

## 1. Testing Goals

The application should be verified at two levels:

- Unit tests verify isolated business logic in services, helpers, and small controller branches.
- Integration tests verify the full request-response cycle across routes, controllers, middleware, validation, and database access.

For this assessment, the important areas are:

- User service logic
- Auth service logic
- Controllers for user creation, user retrieval, registration, and login
- Route-level validation and middleware behavior
- Database interactions and persistence rules

## 2. Tools Used

- Jest for unit tests, mocks, spies, assertions, and test lifecycle hooks.
- Supertest for integration tests against an Express app.
- mongodb-memory-server for a disposable test database when real MongoDB should not be used.
- Jest mocks for external systems such as JWT, bcrypt, email services, and database calls.

## 3. Unit Testing Strategy

Unit tests should focus on one function or one small service method at a time. The database is mocked, so the test only checks logic, not persistence.

### What to unit test

- User Service: create user, find user by id, find by email, duplicate detection, not-found handling.
- Auth Service: password hashing, password comparison, token generation, registration checks, login checks.
- Helper logic: normalization, validation helpers, error formatting.

### What to mock

- Database model methods such as `findOne`, `findById`, `create`, `save`, and `deleteMany`.
- `bcryptjs` functions such as `hash` and `compare`.
- JWT functions such as `sign` and `verify`.
- Email or notification services.

### Example unit test targets

For the User Service, the test should confirm:

- a user is created only when the email does not already exist
- a duplicate email throws a conflict-style error
- a missing user throws a not-found error
- returned user data excludes sensitive fields where required

For the Auth Service, the test should confirm:

- passwords are hashed before save
- login succeeds when the password matches
- login fails with an invalid password
- registration rejects duplicate emails

### Sample unit test approach

```js
import userService from '../services/userService.js';
import User from '../models/User.js';

jest.mock('../models/User.js');

describe('userService.createUser', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('throws when email already exists', async () => {
    User.findOne.mockResolvedValue({ _id: '1', email: 'jane@example.com' });

    await expect(userService.createUser({ email: 'jane@example.com' }))
      .rejects
      .toThrow('User already exists');
  });
});
```

This test verifies the business rule without talking to a live database.

## 4. Integration Testing Strategy

Integration tests should hit the Express app through real HTTP requests using Supertest. These tests verify that validation, middleware, controllers, services, and database operations work together.

### What to integrate test

- `POST /api/users` for user creation
- `GET /api/users/:id` for user retrieval
- `POST /api/auth/register` for registration
- `POST /api/auth/login` for login

### What should be real

- Express app instance
- Route definitions
- Middleware chain
- Validation middleware
- Database connection, ideally against a separate test database or in-memory MongoDB

### What can still be mocked

- JWT token generation if the test is only checking response flow
- Email delivery if the test is not specifically about sending mail
- Third-party APIs and external network calls

### Example integration test approach

```js
import request from 'supertest';
import app from '../app.js';

describe('POST /api/users', () => {
  it('creates a user and returns 201', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'Jane Doe', email: 'jane@example.com', password: 'Password123!' });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('data');
  });
});
```

## 5. Database Testing Best Practices

The safest approach is to use a separate test database or `mongodb-memory-server`.

Recommended rules:

- Never point automated tests to production.
- Use a dedicated test database name, for example `app_test`.
- Reset the database before each test suite or before each test when isolation is important.
- Close database connections after the test run.

Typical lifecycle:

- `beforeAll`: connect to the test database
- `beforeEach`: clear collections
- `afterAll`: disconnect and stop the in-memory server

## 6. Resetting State Between Tests

Resetting state is important because tests should not depend on execution order.

Useful patterns:

- `deleteMany({})` on each collection before each test
- recreate seed data inside the test itself
- call `jest.clearAllMocks()` to reset mock histories

This prevents one test from polluting another through leftover records or cached mock values.

## 7. Coverage of Success, Failure, and Edge Cases

Every key endpoint should include at least three categories of tests:

- Success path: valid input returns the expected status and body.
- Failure path: invalid credentials, duplicate email, missing user, unauthorized access.
- Edge cases: empty body, invalid email format, short password, missing params, malformed ObjectId.

Examples:

- Register with an existing email should return a conflict error.
- Login with a wrong password should return unauthorized.
- Get user with an invalid id should return a validation or cast error.
- Create user with missing required fields should return 400.

## 8. Mocking External Services

External services should not make tests slow or flaky.

Mock these dependencies when they are not under test:

- JWT signing and verification
- Email sending services
- File storage services
- Payment APIs

This keeps the test focused on the code being verified.

## 9. Practical Test Structure

A clean test layout could look like this:

```text
tests/
  unit/
    userService.test.js
    authService.test.js
  integration/
    users.routes.test.js
    auth.routes.test.js
  helpers/
    db.js
    mocks.js
```

## 10. Final Assessment Approach

To complete the assessment well, I would present the strategy in this order:

1. Explain the difference between unit and integration testing.
2. Show how Jest is used for isolated service-level tests.
3. Show how Supertest is used for end-to-end API verification.
4. Describe how the test database is isolated and reset.
5. Demonstrate mocking for JWT, bcrypt, and email services.
6. Confirm success, failure, and edge-case coverage for both User and Auth APIs.

This gives a complete and practical API testing plan that is easy to implement and maintain.
