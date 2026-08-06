import re
import unicodedata
import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class EmployeeData:
    first_name: str
    last_name: str
    email: str
    position: str
    salary: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def normalize_for_email(value: str) -> str:
    normalized = unicodedata.normalize(
        "NFKD",
        value,
    )

    without_accents = "".join(
        character
        for character in normalized
        if not unicodedata.combining(character)
    )

    return re.sub(
        r"[^a-z0-9]+",
        ".",
        without_accents.lower(),
    ).strip(".")


def create_employee_data(
    first_name: str = "Laura",
    last_name: str = "Martinez",
    position: str = "QA Analyst",
    salary: str = "3200",
) -> EmployeeData:
    unique_id = uuid.uuid4().hex[:8]

    normalized_first_name = normalize_for_email(
        first_name
    )

    normalized_last_name = normalize_for_email(
        last_name
    )

    email = (
        f"{normalized_first_name}."
        f"{normalized_last_name}."
        f"{unique_id}@test.com"
    )

    return EmployeeData(
        first_name=first_name,
        last_name=last_name,
        email=email,
        position=position,
        salary=salary,
    )