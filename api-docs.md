```markdown
# TaskManager API

The TaskManager API allows you to manage tasks and todos efficiently. This documentation provides an overview of the API endpoints, authentication, and usage examples.

## Table of Contents

- [Getting Started](#getting-started)
  - [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Users](#users)
  - [Todos](#todos)
  - [Tasks](#tasks)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the TaskManager API, follow these steps:

1. Clone the repository.
2. Install dependencies using `npm install`.
3. Set up your database and configure the environment variables.
4. Run the server using `npm start`.

### Authentication

The API uses JSON Web Tokens (JWT) for authentication. Obtain a token by sending a POST request to `/api/auth/login` with your username and password.

**Example:**

```bash
POST /api/auth/login HTTP/1.1
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

## Endpoints

### Users

#### `GET /api/users/`

Get a list of all users.

#### `POST /api/users/register`

Register a new user.

#### `POST /api/users/login`

Log in an existing user.

#### `GET /api/users/<int:user_id>/`

Get details of a specific user.

### Todos

#### `GET /api/users/<int:user_id>/todos/`

Get a list of todos for a specific user.

#### `POST /api/users/<int:user_id>/todos/`

Create a new todo for a specific user.

#### `PUT /api/users/<int:user_id>/todos/<int:todo_id>/`

Update details of a specific todo.

#### `DELETE /api/users/<int:user_id>/todos/<int:todo_id>/`

Delete a specific todo.

### Tasks

#### `GET /api/users/<int:user_id>/todos/<int:todo_id>/tasks/`

Get a list of tasks for a specific todo.

#### `POST /api/users/<int:user_id>/todos/<int:todo_id>/tasks/`

Create a new task for a specific todo.

#### `PUT /api/users/<int:user_id>/todos/<int:todo_id>/tasks/<int:task_id>/`

Update details of a specific task.

#### `DELETE /api/users/<int:user_id>/todos/<int:todo_id>/tasks/<int:task_id>/`

Delete a specific task.

#### `PATCH /api/users/<int:user_id>/todos/<int:todo_id>/tasks/<int:task_id>/`

Change the status of a specific task.

#### `GET /api/users/<int:user_id>/todos/<int:todo_id>/tasks/<int:task_id>/priorities/`

Get the priority of a specific task.

## Example Usage

Here are some examples of using the TaskManager API:

- Register a new user:
  ```bash
  POST /api/users/register
  Content-Type: application/json

  {
    "username": "new_user",
    "password": "secure_password"
  }
  ```

- Get all todos for a user:
  ```bash
  GET /api/users/<int:user_id>/todos
  Authorization: Bearer your_jwt_token
  ```

- Create a new task for a todo:
  ```bash
  POST /api/users/<int:user_id>/todos/<int:todo_id>/tasks
  Authorization: Bearer your_jwt_token
  Content-Type: application/json

  {
    "title": "New Task",
    "description": "Task details"
  }
  ```

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License
