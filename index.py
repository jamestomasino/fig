#!/usr/local/bin/python

import web
#import twitter
import urlparse
import oauth2 as oauth
#import json

from config import Config

__author__ = 'james@tomasino.org'


urls = (
    '/', 'index',
    '/callback', 'callback',
    '/logout', 'logout'
)

app = web.application(urls, globals())

web.config.db_printing = True
web.config.db_parameters = {
    'dbn' : 'sqlite',
    'db' : 'web.db'
}
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = session
else:
    session = web.config._session

class index:
    config = Config()

    def GET(self):
        consumer = oauth.Consumer(key=self.config.APP_KEY,
                                  secret=self.config.APP_SECRET)
        client = oauth.Client(consumer)
        resp, content = client.request(self.config.REQUEST_TOKEN_URL, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        request_token = dict(urlparse.parse_qsl(content))
        self.config.OAUTH_TOKEN = request_token['oauth_token']
        self.config.OAUTH_TOKEN_SECRET = request_token['oauth_token_secret']
        auth_url = "%s?oauth_token=%s" % (self.config.AUTHORIZE_URL, request_token['oauth_token'])
        web.seeother(auth_url)
        return 'Redirecting to Twitter for OAuth: %s' % auth_url


class callback:
    config = Config()

    def GET(self):
        params = web.input()
        output = ''
        if hasattr(params, 'denied'):
            return 'Authentication Denied'
        if hasattr(params, 'oauth_token'):
            output += 'OAuth Token: %s \n' % params.oauth_token
        if hasattr(params, 'oauth_verifier'):
            output += 'OAuth Verifier: %s \n' % params.oauth_verifier
        if (output == ''):
            output = 'Not a real response from Twitter.'

        #token = oauth.Token(request_token['oauth_token'],
                            #request_token['oauth_token_secret'])
        #token.set_verifier(oauth_verifier)
        #client = oauth.Client(consumer, token)

        #resp, content = client.request(access_token_url, "POST")
        #access_token = dict(urlparse.parse_qsl(content))
        return output

class logout:
    def GET(self):
        web.ctx.session.start()
        web.ctx.session.destroy()
        web.seeother('/')
        return

if __name__ == "__main__":
    app.run()
