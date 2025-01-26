from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from django.db.models import Avg

# Create and List Employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer

# Retrieve, Update, and Delete an Employee
class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

# Calculate Average Salary by Department
class AverageSalaryView(generics.GenericAPIView):
    def get(self, request):
        result = Employee.objects.values('department').annotate(avg_salary=Avg('salary')).order_by('department')
        return Response(result)