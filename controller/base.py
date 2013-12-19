import webapp2, os, jinja2
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/../views' % os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseController(webapp2.RequestHandler):
    def before(self):
        self.user = users.get_current_user()
        if not self.user:
            self.redirect(users.create_login_url(self.request.uri))

    def after(self):
        pass

    def render(self, view, context):
        template = JINJA_ENVIRONMENT.get_template('%s.html' % view)
        self.response.write(template.render(context))

    def get(self):
        self.before()
        self.Get()
        self.after()

    def post(self):
        self.before()
        self.Post()
        self.after()

    def delete(self):
        self.before()
        self.Delete()
        self.after()