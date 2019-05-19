import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        res = 'Hello, World! - webapp2 {}'.format(webapp2.__version__)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(res)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
