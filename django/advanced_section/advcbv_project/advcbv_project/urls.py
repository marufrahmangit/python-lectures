from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('basic_app/', include('basic_app.urls')),
    path('',views.HomeView.as_view(),name="home"),
    path('admin/', admin.site.urls),
]
