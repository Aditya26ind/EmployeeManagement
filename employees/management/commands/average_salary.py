from django.core.management.base import BaseCommand
from django.db.models import Avg
from employees.models import Employee

class Command(BaseCommand):
    help = "Calculate average salary by department"

    def handle(self, *args, **kwargs):
        result = Employee.objects.values('department').annotate(avg_salary=Avg('salary')).order_by('department')
        if result:
            self.stdout.write(self.style.SUCCESS('Department | Average Salary'))
            for entry in result:
                self.stdout.write(f"{entry['department']} | {entry['avg_salary']:.2f}")
        else:
            self.stdout.write(self.style.WARNING('No employees found!'))