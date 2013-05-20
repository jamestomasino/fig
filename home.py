TWEET_TEMPLATE = """
<div class="tweet">
  <span class="twitter-user"><a href="http://twitter.com/%s">%s</a>: </span>
  <span class="twitter-text">%s</span>
  <span class="twitter-relative-created-at"><a href="http://twitter.com/%s/statuses/%s">Posted %s</a></span>
</div>
"""

class Home:
    def __init__(self, api, id, user):
        self.api = api
        self.id = id
        self.user = user

    def render(self):
        statuses = self.api.GetFriendsTimeline(user=self.user, count=50)
        xhtml = ''
        for s in statuses:
            xhtml += TWEET_TEMPLATE % (s.user.screen_name, s.user.screen_name, s.text, s.user.screen_name, s.id, s.relative_created_at)
        return xhtml
