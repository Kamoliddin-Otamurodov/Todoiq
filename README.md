# Todoiq - Todo LIst

Todoiq is a simple and efficient Note Management System designed to help users create, organize, and manage their notes seamlessly. This README provides an overview of the Todoiq project, including its features, installation instructions, and usage guidelines.

## Features

- **Create Todos and Tasks:** Easily create new notes with titles, content, and optional category assignments.
- **Update Todos and Tasks:** Modify existing notes by updating their titles, content, categories, or completion status.
- **Delete Todos and Tasks:** Permanently remove unwanted notes, ensuring a clutter-free experience.
- **Categories:** Organize your notes by assigning them to specific categories.
- **List Notes:** Retrieve a list of all notes for the authenticated user with optional filtering by category and completion status.

## Requirements

- **Python:** 3.9 or later
- **Django:** 5.0
- **Django Rest Framework:** 3.14.0

## Installation

To set up the Todoiq project on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Kamoliddin-Otamurodov/Todoiq.git
   cd Todoiq
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows, use `venv\bin\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The server will run on http://localhost:8000 by default.

## Usage

Before using the Todoiq API, make sure by sending a POST request to `/api/v1/users/login/` with your username and password. Include the obtained token in the `Authorization` header for all subsequent requests.

Refer to the provided API documentation for detailed information on available endpoints, request formats, and responses.

## API Documentation

Explore the [Todoiq REST API Documentation](api-docs.md) for comprehensive details on using the API, including authentication, available endpoints, and example requests and responses.

## Database Design

![db-design](Todoiq-database-design.jpg)