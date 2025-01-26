from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    AverageSalaryView,
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:id>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('average-salary/', AverageSalaryView.as_view(), name='average-salary'),
]