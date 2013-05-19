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
        output = ''
        if hasattr(params, 'denied'):
            return 'Authentication Denied'
        if hasattr(params, 'oauth_token'):
            output += 'OAuth Token: %s \n' % params.oauth_token
        output += 'OAuth Token Secret: %s \n' % config.get_oauth_token_secret();
        if hasattr(params, 'oauth_verifier'):
            output += 'OAuth Verifier: %s \n' % params.oauth_verifier

        #token = oauth.Token(request_token['oauth_token'],
                            #request_token['oauth_token_secret'])
        #token.set_verifier(oauth_verifier)
        #client = oauth.Client(consumer, token)

        #resp, content = client.request(access_token_url, "POST")
        #access_token = dict(urlparse.parse_qsl(content))
        return output

class home:
    def GET(self):
        return 'Home'


class logout:
    def GET(self):
        web.ctx.session.start()
        web.ctx.session.destroy()
        web.seeother('/')
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
