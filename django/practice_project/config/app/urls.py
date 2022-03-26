from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(),name='employees'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(),name='employee'),
    path('employees/create/', views.EmployeeCreateView.as_view(),name='create'),
    path('employees/update/<int:pk>/', views.EmployeeUpdateView.as_view(),name='update'),
    path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(),name='delete'),

    path('departments/', views.DepartmentListView.as_view(),name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(),name='department'),
]