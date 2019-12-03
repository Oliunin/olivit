from urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2


class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('picture', 'picture'),
        ('email', 'email')
    ]

    def authorization_url(self):
        return 'https://dev-zx1aq66u.eu.auth0.com'  + '/authorize'
        #return 'https://blabla' + '/authorize'

    def access_token_url(self):
        return 'https://dev-zx1aq66u.eu.auth0.com' + '/oauth/token'

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['user_id']

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get('id_token')
        jwks = request.urlopen('https://' + 'dev-zx1aq66u.eu.auth0.com' + '/.well-known/jwks.json')
        issuer = 'https://' + 'dev-zx1aq66u.eu.auth0.com' + '/'
        audience = self.setting('KEY')  # CLIENT_ID
        payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)

        return {'username': payload['nickname'],
                'first_name': payload['name'],
                'picture': payload['picture'],
                'user_id': payload['sub'],
                'email': payload['email']}
