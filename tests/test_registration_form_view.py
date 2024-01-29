import pytest
from django.core import mail
from accounts.views import RegistrationFormView
from django.core.mail import EmailMultiAlternatives

def test_send_registration_email_number_of_email_is_1():
    """Při odeslání emailu pomocí metody send_registration_email() ve třídě RegistrationFormView() bude počet emailů 1"""
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        'John',
        'Deer',
        'jd@chickenbook.com'
    )
    assert len(mail.outbox) == 1

@pytest.mark.parametrize('subject', ["Chicken Book Registration"])
def test_send_registration_email_email_subject_is(subject):
    """Při odeslání emailu pomocí metody send_registration_email() ve třídě RegistrationFormView() bude počet emailů 1"""
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        'John',
        'Deer',
        'jd@chickenbook.com'
    )
    assert mail.outbox[0].subject == subject

def test_send_registration_email_email_is_EmailMultiAlternatives():
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        'John',
        'Deer',
        'jd@chickenbook.com'
    )    
    assert isinstance(mail.outbox[0], EmailMultiAlternatives)

@pytest.mark.parametrize('email', ['jd@chickenbook.com'])
def test_send_registration_email_receiver_email_is(email):
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        'John',
        'Deer',
        email
    )        
    assert [email] == mail.outbox[0].to
    
@pytest.mark.parametrize('first_name', ['John'])
def test_send_registration_email_first_name_in_body_is(first_name):
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        first_name,
        'Deer',
        'jd@chickenbook.com'
    )        
    assert mail.outbox[0].body.find(first_name) > -1
    
@pytest.mark.parametrize('last_name', ['Deer'])
def test_send_registration_email_last_name_in_body_is(last_name):
    registration_form = RegistrationFormView()
    registration_form.send_registration_email(
        'John',
        last_name,
        'jd@chickenbook.com'
    )        
    assert mail.outbox[0].body.find(last_name) > -1