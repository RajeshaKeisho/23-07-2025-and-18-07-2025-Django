from django.shortcuts import render
from django.views.generic import ListView
from .models import EmployeePorxy, CustomerPorxy
# Create your views here.
class EmployeeListView(ListView):
    model = EmployeePorxy
    template_name = 'people/employee_list.html'
    context_object_name = 'employees'

class CustomerListView(ListView):
    model = CustomerPorxy
    template_name = 'people/customer_list.html'
    context_object_name = 'customers'