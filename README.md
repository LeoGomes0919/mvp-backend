# .Finance API

## Description

.Finance is a simple API built with Python and Flask that allows you to manage your finances effortlessly. It leverages Flask, flask_openapi, sqlalchemy, and sqlite3 to provide a robust backend for handling financial data.

## Features

- **User-Friendly**: Simplifies financial management tasks.
- **Flexible Database**: Uses SQLAlchemy and SQLite3 for efficient and flexible data storage.
- **OpenAPI Specification**: Built with flask_openapi3, providing a swagger documentation API.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LeoGomes0919/mvp-backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mvp-backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
Run the follxowing command in your terminal:

#### Linux and macOS

```bash
python3 app.py
```

#### Windows

```bash
py app.py
```

## Accessing the API Documentation

Once the application is running, open your browser and navigate to http://localhost:5000/openapi/swagger to explore the API documentation and interact with the available endpoints.

### API Endpoints

- ***POST  /users:*** 
  - Create a new users
- ***POST /auth/login:*** 
  - Auth users
- ***GET /users/profile:*** 
  - Returns the logged in user profile.
- ***POST /categories/:*** 
  - Add a new category.
- ***GET /categories/:*** 
  - Returns all categories
- ***POST /finances/:*** 
  - Create a new finance
- ***GET /finances/{finance_id}:*** 
  - Returns the finance by id
- ***DELETE /finances/{finance_id}:*** 
  - Delete the finance by id
- ***GET /finances/filters:*** 
  - Returns finances by filter and pagination
- ***PUT /finances/{finance_id}:*** 
  - Update a finance

## License
This project is licensed under the MIT License