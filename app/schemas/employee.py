from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):

    first_name: str = Field(
        min_length=2,
        max_length=50
    )

    last_name: str = Field(
        min_length=2,
        max_length=50
    )

    email: EmailStr

    position: str = Field(
        min_length=2,
        max_length=100
    )

    salary: float = Field(
        gt=0
    )