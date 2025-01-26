from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = "Update employee details"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Employee ID')
        parser.add_argument('--name', type=str, help='New employee name')
        parser.add_argument('--email', type=str, help='New employee email')
        parser.add_argument('--department', type=str, help='New employee department')
        parser.add_argument('--salary', type=float, help='New employee salary')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        try:
            employee = Employee.objects.get(id=id)
            if kwargs['name']:
                employee.name = kwargs['name']
            if kwargs['email']:
                employee.email = kwargs['email']
            if kwargs['department']:
                employee.department = kwargs['department']
            if kwargs['salary']:
                employee.salary = kwargs['salary']
            employee.save()
            self.stdout.write(self.style.SUCCESS(f'Employee {id} updated successfully!'))
        except Employee.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Employee with ID {id} does not exist!'))