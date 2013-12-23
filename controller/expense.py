from base import BaseController
from google.appengine.ext import ndb
from model import Car, Expense
from datetime import datetime

class ExpenseController(BaseController):
    def rootKey(self, car_id):
        return ndb.Key(Car, int(car_id))

    def Get(self, car_id, expense_id = None):
        pass

    def Post(self, car_id, expense_id = None):
        if expense_id:
            pass
        else:
            _expense = Expense(
                parent = self.rootKey(car_id),
                type = self.request.get('type'),
                amount = float(self.request.get('amount')),
                date = datetime.strptime(self.request.get('date'), "%Y-%m-%d")
            )
        self.response.write(_expense.put())
        self.redirect('/car')

    def Delete(self, car_id, expense_id):
        ndb.Key(Expense, int(expense_id), parent=self.rootKey(car_id)).delete()