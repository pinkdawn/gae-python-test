from base import BaseController
from model import Car
from datetime import datetime
from google.appengine.ext import ndb

class CarController(BaseController):
    def Get(self):
        cars = Car.all(key=self.rootKey()).fetch()
        context = {
            'user': self.user,
            'cars': cars
        }
        self.render('car/index', context)

    def Post(self):
        new_car = Car(
            parent = self.rootKey(),
            owner = self.user,
            name = self.request.get('name'),
            buy_time = datetime.strptime(self.request.get('buy_date'), "%Y-%m-%d")
        )
        self.response.write(new_car.put())
        self.redirect('/car')

    def Delete(self):
        ndb.Key(Car, int(self.request.get('id')), parent=self.rootKey()).delete()