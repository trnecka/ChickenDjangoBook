import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client

@pytest.mark.django_db
def test_login_view(new_user1):
    user = new_user1
    client = Client()

    login_url = reverse('login')  # Replace 'login' with the actual name of your login view
    response = client.post(login_url, {'username': user.email, 'password': 'Ahoj12345'})

    assert response.status_code == 302  # Check if the login redirects
    print('login ok')
    assert response.url == reverse('chicken-book')  # Replace 'cards' with the actual name of the target view after login
    print('redirect ok')

    # You can also check if the user is authenticated
    assert client.session['_auth_user_id'] == str(user.id)
    print('auth ok')

    # Check if the user is logged in
    response = client.get(reverse('user_profile'))  # Replace 'cards' with the actual name of the target view after login
    assert response.status_code == 200  # Assuming 'cards' view returns a 200 status code for an authenticated user

@pytest.mark.skip(reason='redirect after wrong creditionals')
@pytest.mark.django_db
def test_login_view_invalid_credentials():
    client = Client()

    login_url = reverse('login')  # Replace 'login' with the actual name of your login view
    response = client.post(login_url, {'username': 'nonexistent@example.com', 'password': 'wrongpassword'})

    assert response.status_code == 302  # Check if the login redirects
    assert response.url == reverse('login')  # Replace 'login' with the actual name of your login view

    # Check if an error message is present in the response (assuming you are using messages framework)
    assert 'Wrong credentials' in [msg.message for msg in response.context['messages']]
    print('worng credentials ok')
    