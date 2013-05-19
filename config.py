import web

# if you are going to use FileHandler
#web.config.session_parameters.handler = 'file'
# set the file prefix
#web.config.handler_parameters.file_prefix = 'sess'
# and directory
#web.config.handler_parameters.file_dir = '/tmp'

class Config:
    REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
    AUTHORIZE_URL = 'https://api.twitter.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
    CALLBACK_URL = 'http://fig.tomasino.org:8080/callback'
    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    oauth_verifier = ''

    def __init__(self):
        if (self.APP_KEY == '' and self.APP_SECRET == ''):
            with open('config.txt') as config:
                config_data = [x.strip().split(':') for x in config.readlines()]

            for key,value in config_data:
                if (key == 'APP_KEY'):
                    self.APP_KEY = value
                elif (key == 'APP_SECRET'):
                    self.APP_SECRET = value
