from fastapi import FastAPI
from db import get_db_connection

from model import ProjectCreate, TaskCreate, TaskUpdate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get all projects
@app.get("/projects")
def get_projects():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return projects

# Add a project
@app.post("/projects")
def add_project(project: ProjectCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (title) VALUES (%s)", (project.title,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Project added successfully"}

# Delete a project and its tasks
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = %s", (project_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Project and its tasks deleted"}

# Get all tasks
@app.get("/tasks")
def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

# Get tasks for a project
@app.get("/projects/{project_id}/tasks")
def get_tasks_by_project(project_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE project_id = %s", (project_id,))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

# Add a task
@app.post("/tasks")
def add_task(task: TaskCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, start_date, end_date, status, project_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (task.title, task.start_date, task.end_date, task.status, task.project_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task added successfully"}

# Update a task
@app.put("/tasks")
def update_task(task: TaskUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks SET title = %s, start_date = %s, end_date = %s, status = %s
        WHERE id = %s
    """, (task.title, task.start_date, task.end_date, task.status, task.id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task updated successfully"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully"}
