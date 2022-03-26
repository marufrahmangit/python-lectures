from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy

# Create your views here.

# Employees
class EmployeeListView(ListView):
    context_object_name = 'employees'
    model = models.Employee


class EmployeeDetailView(DetailView):
    # context_object_name = 'employee_detail'
    model = models.Employee
    template_name ='app/employee_detail.html'


class EmployeeCreateView(CreateView):
    model = models.Employee
    fields = ('name','email','phone','department')


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    fields = ('name','email','phone','department')


class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy('app:employees')


# Departments
class DepartmentListView(ListView):
    context_object_name = 'departments'
    model = models.Department


class DepartmentDetailView(DetailView):
    # context_object_name = 'employee_detail'
    model = models.Department
    template_name = 'app/department_detail.html'