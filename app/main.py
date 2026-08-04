from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    title = "Manage Employees App",
    description = "This is a simple FastAPI application to manage employees.",
    version = "1.0.0"
)

app.add_middleware(SessionMiddleware, 
secret_key="development-secret-key")


@app.get("/")
def home():
    return {
        "application": "Manage Employees App",
        "status": "running",
    }
