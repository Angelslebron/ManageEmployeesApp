# ManageEmployeesApp

ManageEmployeesApp is a web application for managing employee records through CRUD operations.

The application was developed with FastAPI, SQLAlchemy, Jinja2, and SQLite. It includes automated tests implemented with Selenium WebDriver and Pytest.

## Features

- Administrator login
- Employee creation and listing
- Employee information updates
- Employee deletion
- Duplicate email validation
- Happy path, negative, and boundary test scenarios
- Automated screenshots
- HTML test report

## Technologies

### Application

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Jinja2
- HTML and CSS

### Testing

- Selenium WebDriver
- Pytest
- Pytest HTML
- Page Object Model

## Project Structure

```text
ManageEmployeesApp/
├── app/
├── tests/
│   ├── pages/
│   └── utils/
├── reports/
├── screenshots/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Installation

Clone the repository:

```powershell
git clone REPOSITORY_URL
cd ManageEmployeesApp
```

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate it with PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create the administrator account:

```powershell
python -m app.seed
```

## Test Credentials

```text
Username: admin
Password: Admin123!
```

These credentials are intended exclusively for project demonstration and automated testing.

## Run the Application

Start the FastAPI server:

```powershell
python -m uvicorn app.main:app --reload
```

Open the application at:

```text
http://127.0.0.1:8000
```

The application must remain running while the Selenium tests are executed.

## Automated Tests

The test suite validates:

- Successful, negative, and boundary login scenarios
- Employee creation
- Employee listing and lookup
- Employee updates
- Employee deletion
- Duplicate email validation
- Boundary value validation

The project uses the Page Object Model. Page-specific browser interactions are located in:

```text
tests/pages/
```

Unique employee test data is generated from:

```text
tests/utils/employee_factory.py
```

## Run the Tests

Open a second terminal, activate the virtual environment, and execute:

```powershell
python -m pytest
```

To run a specific test file:

```powershell
python -m pytest tests/test_create.py
```

## HTML Test Report

Generate the HTML report with:

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

Open the report with:

```powershell
start reports\report.html
```

The generated report is stored at:

```text
reports/report.html
```

## Automated Screenshots

Automated screenshots are stored in:

```text
screenshots/
```

These images provide visual evidence of the automated test scenarios.

## Author

**Angel Duarte Montero Lebron**

Developed as part of an automated testing assignment using Selenium WebDriver and Pytest.