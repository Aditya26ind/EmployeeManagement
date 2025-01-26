from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = "List all employees"

    def handle(self, *args, **kwargs):
        employees = Employee.objects.all().order_by('id')
        if employees:
            self.stdout.write(self.style.SUCCESS('ID | Name | Email | Department | Salary'))
            for employee in employees:
                self.stdout.write(f'{employee.id} | {employee.name} | {employee.email} | {employee.department} | {employee.salary}')
        else:
            self.stdout.write(self.style.WARNING('No employees found!'))