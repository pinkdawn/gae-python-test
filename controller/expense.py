# -*- coding: utf-8 -*-

from base import BaseController
from google.appengine.ext import ndb
from model import Car, Expense
from datetime import datetime

class ExpenseController(BaseController):
    def rootKey(self, car_id):
        return ndb.Key(Car, int(car_id))

    def Get(self, car_id, expense_id):
        _expense = ndb.Key(Car, int(car_id), Expense, int(expense_id)).get()
        context = {
          '_expense': _expense,
          '_carID': car_id,
          '_types': {'refuel':u'加油', 'washing':u'洗车', 'parking':u'泊车', 'insurance':u'保险',
                     'ticket':u'罚单', 'other':u'其他'}
        }
        self.render('expense/edit', context)

    def Post(self, car_id, expense_id = None):
        if expense_id:
            _expense = ndb.Key(Car, int(car_id), Expense, int(expense_id)).get()
        else:
            _expense = Expense(
                parent = self.rootKey(car_id),
            )
        _expense.type = self.request.get('type')
        _expense.amount = float(self.request.get('amount'))
        _expense.date = datetime.strptime(self.request.get('date'), "%Y-%m-%d")
        _expense.address = self.request.get('address')

        _lng = self.request.get('lng')
        _lat = self.request.get('lat')

        if _lng and _lat:
            _expense.location = ndb.GeoPt(_lat, _lng)

        self.response.write(_expense.put())
        if not self.request.get('ajax'):
            self.redirect('/car')

    def Delete(self, car_id, expense_id):
        ndb.Key(Expense, int(expense_id), parent=self.rootKey(car_id)).delete()