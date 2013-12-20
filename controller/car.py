from base import BaseController
from model import Car
from datetime import datetime
from google.appengine.ext import ndb

class CarController(BaseController):
    def Get(self):
        cars = Car.all(key=self.rootKey()).fetch()
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
            _car.buy_time = datetime.strptime(self.request.get('buy_date'), "%Y-%m-%d")

        self.response.write(_car.put())
        self.redirect('/car')

    def Delete(self):
        ndb.Key(Car, int(self.request.get('id')), parent=self.rootKey()).delete()