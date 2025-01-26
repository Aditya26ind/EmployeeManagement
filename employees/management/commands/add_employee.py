from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = "Add a new employee"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Employee name')
        parser.add_argument('email', type=str, help='Employee email')
        parser.add_argument('department', type=str, help='Employee department')
        parser.add_argument('salary', type=float, help='Employee salary')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        department = kwargs['department']
        salary = kwargs['salary']

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary
        )
        self.stdout.write(self.style.SUCCESS(f'Employee {name} added successfully!'))