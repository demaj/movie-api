from datetime import datetime

import factory
from factory import faker

from accounts.models import CustomUser


class UserFactory(factory.Factory):
    class Meta:
        model = CustomUser

    first_name = 'John'
    last_name = 'Doe'
    username = faker.Faker('username')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())
    date_joined = factory.LazyFunction(datetime.now)


class AdminFactory(UserFactory):
    admin = True
    group = 'admins'
