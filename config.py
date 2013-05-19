class Config:
    REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
    AUTHORIZE_URL = 'https://api.twitter.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
    CALLBACK_URL = 'http://fig.tomasino.org:8080/callback'

    _app_key = ''
    _app_secret = ''
    _oauth_token = ''
    _oauth_token_secret = ''
    _oauth_verifier = ''
    _user_id = ''
    _screen_name = ''

    def __init__(self, session):
        self.session = session
        if (self._app_key == '' and self._app_secret == ''):
            with open('config.txt') as config:
                config_data = [x.strip().split(':') for x in config.readlines()]

            for key,value in config_data:
                if (key == 'APP_KEY'):
                    self._app_key = value
                elif (key == 'APP_SECRET'):
                    self._app_secret = value

        self.load_all()
        #self.session.cleanup()

    def load_all(self):
        if hasattr(self.session, 'oauth_token'):
            self._oauth_token = self.session.oauth_token
        if hasattr(self.session, 'oauth_token_secret'):
            self._oauth_token_secret = self.session.oauth_token_secret
        if hasattr(self.session, 'oauth_verifier'):
            self._oauth_verifier = self.session.oauth_verifier
        if hasattr(self.session, 'user_id'):
            self._user_id = self.session.user_id
        if hasattr(self.session, 'screen_name'):
            self._screen_name = self.session.screen_name

    def save_all(self):
        self.session.oauth_token = self._oauth_token
        self.session.oauth_token_secret = self._oauth_token_secret
        self.session.oauth_verifier = self._oauth_verifier

    def is_logged_in(self):
        if ( self._user_id != '' and self._screen_name != ''):
            return True
        else:
            return False

    def get_app_key(self):
        return self._app_key

    def get_app_secret(self):
        return self._app_secret

    def set_oauth_token(self, val):
        self.session.oauth_token = self._oauth_token = val;

    def get_oauth_token(self):
        return self._oauth_token

    def set_oauth_token_secret(self, val):
        self.session.oauth_token_secret = self._oauth_token_secret = val;

    def get_oauth_token_secret(self):
        return self._oauth_token_secret

    def set_oauth_verifier(self, val):
        self.session.oauth_verifier = self._oauth_verifier = val;

    def get_oauth_verifier(self):
        return self._oauth_verifier

    def set_user_id(self, val):
        self.session.user_id = self._user_id = val;

    def get_user_id(self):
        return self._user_id

    def set_screen_name(self, val):
        self.session.screen_name = self._screen_name = val;

    def get_screen_name(self):
        return self._screen_name

