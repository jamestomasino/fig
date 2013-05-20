# TODO: Replace this part with web.py template render stuff.
PAGE_TEMPLATE = """
<!DOCTYPE HTML>

<html>

    <head>
        <title>Fig - %s</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" media="screen" charset="utf-8">
    </head>

    <body>

        <div class="tweets">
        %s
        </div>

        <script type="text/javascript" src="js/main.js"></script>

    </body>

</html>
"""

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

        page = PAGE_TEMPLATE % ( 'Home', xhtml )
        return page
