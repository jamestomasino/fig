from twython import Twython

class OAuth:

    request_token_url = 'https://api.twitter.com/oauth/request_token'
    access_token_url = 'https://api.twitter.com/oauth/authorize'
    authorize_url = 'https://api.twitter.com/oauth/access_token'
    app_key = ''
    app_secret = ''
    oauth_token = ''
    oauth_token_secret = ''
    oauth_verifier = ''

    def __init__(self):
        pass

    def get_auth(self):
        with open('config.txt') as config:
            config_data = [x.strip().split(':') for x in config.readlines()]

        for key,value in config_data:
            if (key == 'app_key'):
                self.app_key = value
            elif (key == 'app_secret'):
                self.app_secret = value

    def authorize(self):
        self.get_auth()
        t = Twython(self.app_key, self.app_secret)
        auth_props = t.get_authentication_tokens(
            callback_url='http://fig.tomasino.com'
        )
        self.oauth_token = auth_props['oauth_token']
        self.oauth_token_secret = auth_props['oauth_token_secret']

        print 'Connect to Twitter via: %s' % auth_props['auth_url']

    def callback(self, oauth_token, oauth_verifier):
        self.get_auth()
        self.oauth_token = oauth_token
        self.oauth_verifier = oauth_verifier
        t = Twython(self.app_key, self.app_secret,
            self.oauth_token, self.oauth_token_secret)
        self.auth_tokens = t.get_authorized_tokens(self.oauth_verifier)
