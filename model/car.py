from google.appengine.ext import ndb
from base import BaseModel
import datetime

class Car(BaseModel):
    owner = ndb.UserProperty()
    name = ndb.StringProperty()
    date = ndb.DateProperty()
    mile = ndb.IntegerProperty()
    price = ndb.FloatProperty()

    _fields = ('name', 'date', 'mile', 'price')

    def expenses_last_year(self, type=None):
        return self.expenses(type, datetime.datetime.now() - datetime.timedelta(days=3*365))

    def expenses(self, type=None, begin=None, end=None):
        _key = ndb.Key(Car, self.key.id())
        _order = -Expense.date

        _query = []

        if type:
            _query.append(Expense.type == type)
        if begin:
            _query.append(Expense.date >= begin)
        if end:
            _query.append(Expense.date <= end)

        if len(_query) == 1:
            _query = _query[0]
        elif len(_query) > 1:
            _query = ndb.AND(*_query)

        _query = Expense.all(_query, key=_key, order=_order)
        return _query

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