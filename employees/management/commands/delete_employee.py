from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = "Delete an employee"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Employee ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            self.stdout.write(self.style.SUCCESS(f'Employee {id} deleted successfully!'))
        except Employee.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Employee with ID {id} does not exist!'))