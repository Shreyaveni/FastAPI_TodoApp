# Todo API

## Description
This is a simple **Todo API** built with [FastAPI](w) that supports **CRUD (Create, Read, Update, Delete)** operations for managing todo items. It provides endpoints to fetch all todos, retrieve a specific todo by ID, add new todos, update existing ones, and delete them. The API uses **Pydantic** for data validation and runs on **Uvicorn**.

## Setup & Run

### Clone the repository:
```sh
git clone https://github.com/Shreyaveni/TodoAPI.git
cd TodoAPI
```

### Install dependencies:
```sh
pip install fastapi uvicorn
```

### Run the API server:
```sh
uvicorn main:app --reload
```

### Access the API at:
```
http://127.0.0.1:8000
```

### API Documentation:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

