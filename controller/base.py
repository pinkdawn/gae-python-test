import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from model import BaseModel
from classes.jinja2 import jj2

class BaseController(webapp2.RequestHandler):
    def before(self):
        self.user = users.get_current_user()
        if not self.user:
            self.redirect(users.create_login_url(self.request.uri))

    def after(self):
        pass

    def rootKey(self, _id='root'):
        if not ndb.Key(BaseModel, _id).get():
            _root = BaseModel(id=_id)
            _root.put()
            return _root.key
        return ndb.Key(BaseModel, _id)

    def render(self, view, context):
        #TODO add cache to template file
        template = jj2.get_template('%s.html' % view)
        self.response.write(template.render(context))

    def get(self, *args, **kwargs):
        self.before()
        self.Get(*args, **kwargs)
        self.after()

    def post(self, *args, **kwargs):
        self.before()
        self.Post(*args, **kwargs)
        self.after()

    def delete(self, *args, **kwargs):
        self.before()
        self.Delete(*args, **kwargs)
        self.after()