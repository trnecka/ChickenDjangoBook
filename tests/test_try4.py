import pytest
from accounts.models import User
    
@pytest.mark.django_db
def test_new_user(new_user1):
    user = new_user1.email
    print(user)
    assert new_user1.email == 'test2@test2.com'
