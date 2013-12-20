from google.appengine.ext import ndb
from base import BaseModel

class Car(BaseModel):
    owner = ndb.UserProperty()
    name = ndb.StringProperty()
    buy_time = ndb.DateTimeProperty(auto_now_add=False)

class Expense(BaseModel):
    price = ndb.FloatProperty
    type  = ndb.StringProperty