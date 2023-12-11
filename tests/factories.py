import factory
from faker import Faker
from accounts.models import User

faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    email = 'test2@test2.com'
    is_staff = 'True'
    first_name = faker.name()