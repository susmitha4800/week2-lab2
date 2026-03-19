# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to understand HTTP methods, routing, request/response handling, and data validation. Create a functional API server that handles CRUD operations with proper error handling and documentation.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description
Build a FastAPI application that implements a simple Todo management system with endpoints for creating, reading, updating, and deleting todos. Use Pydantic models for data validation and list-based in-memory storage.

#### Requirements
Completed program should:

- Use FastAPI to create a web server with proper routing
- Implement GET endpoint to retrieve all todos
- Implement POST endpoint to create a new todo
- Implement GET endpoint to retrieve a single todo by ID
- Implement PUT endpoint to update an existing todo
- Implement DELETE endpoint to remove a todo
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include error handling for invalid requests

### 🛠️ Add API Documentation

#### Description
Leverage FastAPI's automatic documentation features to provide interactive API documentation for users testing the endpoints.

#### Requirements
Completed program should:

- Enable Swagger UI at `/docs` endpoint
- Enable ReDoc at `/redoc` endpoint
- Include descriptive docstrings for each endpoint
- Use proper response models for documentation clarity
- Verify documentation displays all endpoints and expected data formats

## 🐍 Python Concepts Covered

- RESTful API design principles
- HTTP methods (GET, POST, PUT, DELETE)
- Web frameworks and routing
- Request/response validation with Pydantic
- Status codes and error handling
- JSON data serialization

## 📁 Files

- `starter-code.py` — FastAPI application skeleton with endpoint stubs
