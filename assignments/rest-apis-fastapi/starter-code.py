"""
FastAPI Todo Application - Starter Code

Build a Todo management API with CRUD operations using FastAPI.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple Todo management API built with FastAPI",
    version="1.0.0"
)

# Pydantic model for Todo
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoBase):
    id: int

# In-memory storage for todos
todos_db = []
next_id = 1

# TODO: Implement GET /todos endpoint
# Return all todos from the database
@app.get("/todos", response_model=List[Todo])
async def get_todos():
    """
    Retrieve all todos.
    
    Returns:
        List of all todos
    """
    pass

# TODO: Implement POST /todos endpoint
# Create a new todo and return it with assigned ID
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoBase):
    """
    Create a new todo.
    
    Args:
        todo: Todo data to create
        
    Returns:
        Created todo with assigned ID
    """
    pass

# TODO: Implement GET /todos/{todo_id} endpoint
# Retrieve a specific todo by ID or raise 404 if not found
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    """
    Retrieve a specific todo by ID.
    
    Args:
        todo_id: ID of the todo to retrieve
        
    Returns:
        The requested todo
        
    Raises:
        HTTPException: If todo not found
    """
    pass

# TODO: Implement PUT /todos/{todo_id} endpoint
# Update an existing todo or raise 404 if not found
@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoBase):
    """
    Update an existing todo.
    
    Args:
        todo_id: ID of the todo to update
        todo_update: Updated todo data
        
    Returns:
        Updated todo
        
    Raises:
        HTTPException: If todo not found
    """
    pass

# TODO: Implement DELETE /todos/{todo_id} endpoint
# Delete a todo or raise 404 if not found
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """
    Delete a todo.
    
    Args:
        todo_id: ID of the todo to delete
        
    Raises:
        HTTPException: If todo not found
    """
    pass

# Run the application with: uvicorn starter-code:app --reload
