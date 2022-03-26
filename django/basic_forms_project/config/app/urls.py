from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form_page/', views.form_name_view, name='form_name'),
]