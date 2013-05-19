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
    '/callback', 'callback'
)


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
        print
        print resp
        print
        print content
        print
        print request_token
        auth_url = "%s?oauth_token=%s" % (self.config.AUTHORIZE_URL, request_token['oauth_token'])
        web.seeother(auth_url)
        return 'Redirecting to Twitter for OAuth: %s' % auth_url

class callback:
    config = Config()

    def GET(self):
        return 'Callback.'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
