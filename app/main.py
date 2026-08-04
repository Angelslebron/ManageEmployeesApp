from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import Base, engine, SessionLocal
from app.services.auth_service import authenticate_user


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="ManageEmployeesApp",
    description="Employee management application",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

@app.get(
    "/",
    response_class=HTMLResponse
)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.get(
    "/login",
    response_class=HTMLResponse
)
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.post(
    "/login",
    response_class=HTMLResponse
)
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    db = SessionLocal()

    user = authenticate_user(
        db,
        username,
        password
    )

    db.close()

    if not user:

        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={
                "error": "Invalid username or password.",
                "username": username
            },
            status_code=401
        )

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "success": f"Welcome, {user.username}!",
            "username": username
        }
    )