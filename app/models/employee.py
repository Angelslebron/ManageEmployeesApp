from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(50),
        nullable=False
    )

    last_name = Column(
        String(50),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )

    position = Column(
        String(100),
        nullable=False
    )

    salary = Column(
        Float,
        nullable=False
    )