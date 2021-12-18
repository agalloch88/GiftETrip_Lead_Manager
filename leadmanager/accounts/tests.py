from django.conf.urls import url
from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
def test_register_access():
    url = reverse('knox_register')
    assert url == '/api/auth/register'
    
    
def test_login_access():
    url = reverse('knox_login')
    assert url == '/api/auth/login'
    
    
def test_user_access():
    url = reverse('knox_user')
    assert url == '/api/auth/user'
    
    
def test_logout_access():
    url = reverse('knox_logout')
    assert url == '/api/auth/logout'