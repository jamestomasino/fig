#!/usr/local/bin/python

import web
import twitter

__author__ = 'james@tomasino.org'

urls = (
    '/', 'index'
)

TEMPLATE = """
<div class="twitter">
  <span class="twitter-user"><a href="http://twitter.com/%s">Twitter</a>: </span>
  <span class="twitter-text">%s</span>
  <span class="twitter-relative-created-at"><a href="http://twitter.com/%s/statuses/%s">Posted %s</a></span>
</div>
"""

def FetchTwitter(user):
  assert user
  statuses = twitter.Api().GetUserTimeline(id=user, count=1)
  s = statuses[0]
  xhtml = TEMPLATE % (s.user.screen_name, s.text, s.user.screen_name, s.id, s.relative_created_at)
  return xhtml

class index:
    def GET(self):
        return FetchTwitter('mr_ino')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
