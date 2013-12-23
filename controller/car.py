from base import BaseController
from model import Car, Expense
from datetime import datetime
from google.appengine.ext import ndb

import json

class ExportController(BaseController):
    def Get(self):
        _result = []
        cars = Car.all(Car.owner==self.user, key=self.rootKey()).fetch()
        for car in cars:
            _car = car.json()
            _car['expenses'] = []
            for _exp in Expense.all(key=ndb.Key(Car, car.key.id())).fetch():
                _car['expenses'].append(_exp.json())
            _result.append(_car)
        self.response
        self.response.write(json.dumps(_result))

class ImportController(BaseController):
    def Post(self):
        pass

class CarController(BaseController):
    def Get(self):
        cars = Car.all(Car.owner==self.user, key=self.rootKey()).fetch()
        context = {
            'user': self.user,
            'cars': cars,
            'now' : datetime.now()
        }
        self.render('car/index', context)

    def Post(self, _id=None):
        if _id:
            _car = ndb.Key(Car, int(_id), parent=self.rootKey()).get()
        else:
            _car = Car(
                parent = self.rootKey(),
                owner = self.user,
            )

        _car.name = self.request.get('name')
        if self.request.get('buy_date'):
            _car.date = datetime.strptime(self.request.get('buy_date'), "%Y-%m-%d")
        if self.request.get('mile'):
            _car.mile = int(self.request.get('mile'))
        if self.request.get('price'):
            _car.price = float(self.request.get('price'))

        self.response.write(_car.put())
        self.redirect('/car')

    def Delete(self, _id):
        ndb.Key(Car, int(_id), parent=self.rootKey()).delete()