# Generated by Django 4.0 on 2021-12-14 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_department_employee_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employees', to='app.department'),
        ),
    ]
