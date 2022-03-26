# GENERATE DUMMY DATA

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from app.models import Department, Employee
from faker import Faker

fakegen = Faker()
departments = ['Marketing','Sales','Administration','Finance','Development']

def add_department():
    d = Department.objects.get_or_create(name=random.choice(departments))[0]
    d.save()
    return d

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        dept = add_department()

        # create fake data for that entry
        fake_name = fakegen.company()
        fake_email = fakegen.email()
        fake_phone = fakegen.phone_number()

        # create the new webpage entry
        emp = Employee.objects.get_or_create(
            department=dept,
            name=fake_name,
            email=fake_email,
            phone=fake_phone
        )[0]


if __name__ == '__main__':
    print('Populating scripts')
    populate(20)
    print("Populating completed")