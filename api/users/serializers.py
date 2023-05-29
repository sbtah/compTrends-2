from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    '''Serializer for the user auth token.'''

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, data):
        '''Validate and authenticate the user.'''

        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
