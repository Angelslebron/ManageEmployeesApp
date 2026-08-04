from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


def create_employee(
    db: Session,
    employee_data: EmployeeCreate
):

    existing_employee = (
        db.query(Employee)
        .filter(Employee.email == employee_data.email)
        .first()
    )

    if existing_employee:
        return None

    employee = Employee(
        first_name=employee_data.first_name,
        last_name=employee_data.last_name,
        email=employee_data.email,
        position=employee_data.position,
        salary=employee_data.salary
    )

    try:

        db.add(employee)
        db.commit()
        db.refresh(employee)

    except IntegrityError:

        db.rollback()

        return None

    return employee


def get_employees(
    db: Session
):

    return (
        db.query(Employee)
        .order_by(Employee.id)
        .all()
    )


def get_employee_by_id(
    db: Session,
    employee_id: int
):

    return (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )


def update_employee(
    db: Session,
    employee: Employee,
    employee_data: EmployeeCreate
):

    existing_employee = (
        db.query(Employee)
        .filter(
            Employee.email == employee_data.email,
            Employee.id != employee.id
        )
        .first()
    )

    if existing_employee:
        return None

    employee.first_name = employee_data.first_name
    employee.last_name = employee_data.last_name
    employee.email = employee_data.email
    employee.position = employee_data.position
    employee.salary = employee_data.salary

    try:

        db.commit()
        db.refresh(employee)

    except IntegrityError:

        db.rollback()

        return None

    return employee

def delete_employee(
    db: Session,
    employee: Employee
):

    try:

        db.delete(employee)
        db.commit()

    except IntegrityError:

        db.rollback()

        return False

    return True