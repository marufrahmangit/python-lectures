from django.urls import path
from . import views

# TEMPALTE TAGGING
app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('other/', views.other, name='other'),
    path('relative_url/', views.relative_url, name='relative_url'),
]