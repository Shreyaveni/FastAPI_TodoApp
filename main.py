from fastapi import FastAPI, HTTPException
from models import Todo
from database import todo_list

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/todos")
def get_todos():
    print("Fetching todos...")
    return todo_list

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos")
def create_todo(todo: Todo):
    todo_list.append(todo)
    return {"message": "Todo added successfully", "todo": todo}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
