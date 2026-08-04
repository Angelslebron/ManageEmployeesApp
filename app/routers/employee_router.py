from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.employee import EmployeeCreate
from app.services.employee_service import create_employee, get_employees


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


templates = Jinja2Templates(
    directory="app/templates"
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False
)
def list_employees(
    request: Request,
    db: Session = Depends(get_db)
):

    username = request.session.get("username")

    if not username:

        return RedirectResponse(
            url="/login",
            status_code=303
        )

    employees = get_employees(db)

    return templates.TemplateResponse(
        request=request,
        name="employees/list.html",
        context={
            "username": username,
            "employees": employees
        }
    )

@router.get(
    "/create",
    response_class=HTMLResponse,
    include_in_schema= False
)
def create_employee_page(request: Request):

    username = request.session.get("username")

    if not username:

        return RedirectResponse(
            url="/login",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="employees/create.html",
        context={
            "username": username
        }
    )

@router.post(
    "/",
    response_class=HTMLResponse
)
def create_employee_route(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    position: str = Form(...),
    salary: float = Form(...),
    db: Session = Depends(get_db)
):

    username = request.session.get("username")

    if not username:

        return RedirectResponse(
            url="/login",
            status_code=303
        )

    employee_data = EmployeeCreate(
        first_name=first_name,
        last_name=last_name,
        email=email,
        position=position,
        salary=salary
    )

    employee = create_employee(
        db,
        employee_data
    )

    if not employee:

        return templates.TemplateResponse(
            request=request,
            name="employees/create.html",
            context={
                "error": "An employee with that email already exists.",
                "username": username
            },
            status_code=400
        )

    request.session["success"] = (
        "Employee created successfully."
    )

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )