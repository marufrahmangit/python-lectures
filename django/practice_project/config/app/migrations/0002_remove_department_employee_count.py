# Generated by Django 4.0 on 2021-12-14 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='employee_count',
        ),
    ]
