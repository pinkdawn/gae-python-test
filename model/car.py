from google.appengine.ext import ndb
from base import BaseModel

class Car(BaseModel):
    owner = ndb.UserProperty()
    name = ndb.StringProperty()
    date = ndb.DateProperty(auto_now_add=False)
    mile = ndb.IntegerProperty()
    price = ndb.FloatProperty()

    _fields = ('name', 'date', 'mile', 'price')

    def expenses(self, type=None):
        if type:
            _query = Expense.all(Expense.type == type, key=ndb.Key(Car, self.key.id()))
        else:
            _query = Expense.all(key=ndb.Key(Car, self.key.id()))
        return _query.fetch()

    def sum(self, type):
        _sum = 0
        if type != 'other':
            _exps = self.expenses(type)
        else:
            _query = ndb.AND(
                Expense.type != 'refuel',
                Expense.type != 'parking',
                Expense.type != 'insurance',
                Expense.type != 'washing',
                Expense.type != 'ticket',
            )
            _exps = Expense.all(_query, key=ndb.Key(Car, self.key.id()))
        for exp in _exps:
            _sum = _sum + exp.amount
        return _sum

class Expense(BaseModel):
    amount = ndb.FloatProperty()
    type  = ndb.StringProperty()
    date = ndb.DateProperty()

    _fields = ('amount', 'type', 'date')