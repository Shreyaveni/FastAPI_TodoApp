FastAPI Todo API
This is a simple Todo API built with FastAPI. It allows users to create, read, update, and delete (CRUD) todo items.

🚀 Features
Get all todos: Fetch a list of todos.
Get a single todo: Retrieve details of a specific todo by ID.
Create a todo: Add a new todo to the list.
Update a todo: Modify an existing todo.
Delete a todo: Remove a todo from the list.
🛠 Tech Stack
FastAPI - High-performance Python web framework.
Pydantic - Data validation and serialization.
Uvicorn - ASGI server for FastAPI.
🔧 Setup & Run
1. Clone the repository: 
git clone https://github.com/Shreyaveni/TodoAPI.git
cd TodoAPI
Install dependencies:
sh
Copy
Edit
pip install fastapi uvicorn
Run the API server:
sh
Copy
Edit
uvicorn main:app --reload
Access the API at:
cpp
Copy
Edit
http://127.0.0.1:8000
View API documentation:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
📌 Notes
The Todo model is stored in models.py.
The todo list is managed in database.py.
This project uses an in-memory list for todos.
