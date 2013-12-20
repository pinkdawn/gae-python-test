from base import BaseController
from google.appengine.ext import ndb
from model import Car, Expense

class ExpenseController(BaseController):
    def rootKey(self, car_id):
        return ndb.Key(Car, int(car_id))

    def Get(self, car_id):
        pass

    def Post(self, expense_id = None):
        pass