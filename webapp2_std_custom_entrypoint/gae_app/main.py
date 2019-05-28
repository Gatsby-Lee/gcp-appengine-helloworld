import os
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        res = 'Hello, World! - webapp2 {}'.format(webapp2.__version__)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(res)

class ListEnv(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        for k,v in os.environ.items():
            self.response.write('{}: {}\n'.format(k,v))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/env', ListEnv),
], debug=True)
