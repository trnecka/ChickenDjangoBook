import pytest
    
@pytest.mark.django_db
def test_new_user(new_user1):
    user = new_user1
    print('User creation')
    assert user.email == 'test2@test2.com'
    assert user.first_name == 'PrveMeno'
    assert user.last_name == 'DruheMeno'
    assert user.phone_number is None
    assert user.check_password('Ahoj12345')
    assert user.is_superuser is False
    assert user.is_active is True # malo by byt False ?
    assert user.is_staff is False
    assert user.about is None
