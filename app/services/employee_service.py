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