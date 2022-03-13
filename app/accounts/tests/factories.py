import factory
from accounts.models import CustomUser
from factory import faker


class UserFactory(factory.Factory):
    class Meta:
        model = CustomUser

    first_name = "John"
    last_name = "Doe"
    username = faker.Faker("username")
    email = factory.LazyAttribute(lambda a: "{}.{}@example.com".format(a.first_name, a.last_name).lower())


class AdminFactory(UserFactory):
    admin = True
    group = "admins"
