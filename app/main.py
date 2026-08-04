from fastapi import FastAPI

app = FastAPI(
    title = "Manage Employees App",
    description = "This is a simple FastAPI application to manage employees.",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "application": "Manage Employees App",
        "status": "running",
    }
