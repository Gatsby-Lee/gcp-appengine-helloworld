import os
import json

import webapp2

from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class MainPage(BaseHandler):
    def get(self):
        context = {'message': 'Hello, world!'}
        self.render_response('index.jinja2', **context)


class EnvPage(BaseHandler):
    def get(self):
        r = {}
        for k, v in os.environ.items():
            r[k] = str(v)
        content = json.dumps(r)
        self.response.headers['Content-Type'] = 'text/json'
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/env', EnvPage),
], debug=True)
