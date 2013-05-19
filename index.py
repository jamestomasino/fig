#!/usr/local/bin/python

import web
import urlparse
import oauth2 as oauth

from config import Config

__author__ = 'james@tomasino.org'


class index:

    def GET(self):
        if (config.is_logged_in() ):
            print 'going to home'
            web.seeother('/home')
        else:
            print 'going to login'
            web.seeother('/login')
        return

class login:
    def GET(self):
        consumer = oauth.Consumer(key=config.get_app_key(),
                                  secret=config.get_app_secret())
        client = oauth.Client(consumer)
        resp, content = client.request(config.REQUEST_TOKEN_URL, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        request_token = dict(urlparse.parse_qsl(content))
        config.set_oauth_token(request_token['oauth_token'])
        config.set_oauth_token_secret(request_token['oauth_token_secret'])
        auth_url = "%s?oauth_token=%s" % (config.AUTHORIZE_URL,
                                          request_token['oauth_token'])
        web.seeother(auth_url)
        return 'Redirecting to Twitter for OAuth: %s' % auth_url

class callback:
    def GET(self):
        params = web.input()
        if hasattr(params, 'denied'):
            return 'Authentication Denied'

        if hasattr(params, 'oauth_verifier'):
            config.set_oauth_verifier(params.oauth_verifier)

        consumer = oauth.Consumer(
            key=config.get_app_key(),
            secret=config.get_app_secret())
        token = oauth.Token(
            config.get_oauth_token(),
            config.get_oauth_token_secret())
        token.set_verifier(config.get_oauth_verifier())
        client = oauth.Client(consumer, token)
        resp, content = client.request(config.ACCESS_TOKEN_URL, "POST")
        access_token = dict(urlparse.parse_qsl(content))

        # Use these credentials from now on
        config.set_oauth_token(access_token['oauth_token'])
        config.set_oauth_token_secret(access_token['oauth_token_secret'])
        config.set_user_id(access_token['user_id'])
        config.set_screen_name(access_token['screen_name'])

        web.seeother('/')
        return access_token

class home:
    def GET(self):
        return 'Home'


class logout:
    def GET(self):
        if 'session' in globals():
            session.kill()
        return

if __name__ == "__main__":
    urls = (
        '/', 'index',
        '/home', 'home',
        '/callback', 'callback',
        '/login', 'login',
        '/logout', 'logout'
    )

    app = web.application(urls, globals())

    if web.config.get('_session') is None:
        db = web.database(dbn='sqlite', db='web.db')
        store = web.session.DBStore(db, 'sessions')
        session = web.session.Session(app, store)
        web.config._session = session
    else:
        session = web.config._session

    config = Config(session)
    app.run()
