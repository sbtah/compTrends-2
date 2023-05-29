'''
Tests for users API
'''
import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


TOKEN_URL = reverse("users:token")


class TestUserPublicAPI:
    '''Test cases related to authentication views.'''

    def test_creating_token_for_user(
            self,
            example_user,
            example_user_payload,
            api_client,
        ):
        '''Test generating token for valid credentials is successful.'''

        user = example_user
        payload_data = example_user_payload
        payload = {
            'email': payload_data['email'],
            'password': payload_data['password'],
        }
        res = api_client.post(TOKEN_URL, payload)
        assert 'token' in res.data
        assert res.status_code == status.HTTP_200_OK

    def test_creating_token_with_bad_credentials(
            self,
            example_user,
            api_client
        ):
        '''Test that you can't get token with bad credentials.'''

        user = example_user
        payload = {
            "email": user.email,
            "password": 'badpass',
        }
        res = api_client.post(TOKEN_URL, payload)

        assert 'token' not in res.data
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_token_blank_password(self, api_client):
        '''Test posting a blank password returns an error.'''

        payload = {
            'email': 'test@example.com',
            "password": '',
        }
        res = api_client.post(TOKEN_URL, payload)

        assert 'token' not in res.data
        assert res.status_code == status.HTTP_400_BAD_REQUEST
