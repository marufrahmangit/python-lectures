from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department,related_name='employees',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:employee',kwargs={'pk':self.pk})

