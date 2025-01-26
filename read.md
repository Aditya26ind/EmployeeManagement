Employee Management System API

This is a simple Employee Management System built using Django and Django REST Framework (DRF). It provides a RESTful API to manage employee records and calculate average salaries by department.

Features
CRUD Operations:

Add a new employee.

Update employee details.

Delete an employee.

List all employees.

Calculate Average Salary:

Fetch the average salary for each department.

API Endpoints
Employees
Add a New Employee:

POST /api/employees/

Body: { "name": "John Doe", "email": "john@example.com", "department": "Engineering", "salary": 75000 }

List All Employees:

GET /api/employees/

Retrieve an Employee:

GET /api/employees/<id>/

Update an Employee:

PATCH /api/employees/<id>/

Body: { "name": "Jane Doe", "salary": 80000 }

Delete an Employee:

DELETE /api/employees/<id>/

Average Salary
Calculate Average Salary by Department:

GET /api/average-salary/

Setup
Clone the repository:



git clone <repository-url>
cd employee-management
Install dependencies:



pip install -r requirements.txt
Run migrations:



python manage.py migrate
Start the server:



python manage.py runserver
Access the API at http://127.0.0.1:8000/api/.

Example Requests
Add a New Employee


curl -X POST http://127.0.0.1:8000/api/employees/ \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com", "department": "Engineering", "salary": 75000}'
List All Employees


curl -X GET http://127.0.0.1:8000/api/employees/
Calculate Average Salary by Department


curl -X GET http://127.0.0.1:8000/api/average-salary/
Technologies Used
Django: Web framework.

Django REST Framework (DRF): For building RESTful APIs.

PostgreSQL : Database

