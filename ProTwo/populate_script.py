import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from faker import Faker
from AppTwo.models import User

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]


if __name__ == "__main__":
    print("\nPopulating Script")
    populate(10)
    print("\nPopulate complete")
