import factory
from faker import Faker
from accounts.models import User
from django.contrib.auth.hashers import make_password

faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    email = 'test2@test2.com'
    password = make_password('Ahoj12345')
    first_name = 'PrveMeno'
    last_name = 'DruheMeno'
    