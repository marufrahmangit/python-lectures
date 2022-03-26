# GENERATE DUMMY DATA

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from user_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_full_name = fakegen.name().split()
        fake_first_name = fake_full_name[0]
        fake_last_name = fake_full_name[1]
        fake_email = fakegen.email()

        # create the new user entry
        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]


if __name__ == '__main__':
    print('Populating database')
    populate(20)
    print("Populating completed")




