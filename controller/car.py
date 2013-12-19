from base import BaseController
from model import Car
from datetime import datetime
from google.appengine.ext import ndb

class CarController(BaseController):
    def Get(self):
        cars = Car.all()
        context = {
            'user': self.user,
            'cars': cars
        }
        self.render('car/index', context)

    def Post(self):
        new_car = Car(
            parent=ndb.Key("Car", "%s %s" % (self.user.email(), self.request.get('name'))),
            owner = self.user,
            name = self.request.get('name'),
            buy_time = datetime.strptime(self.request.get('buy_date'), "%Y-%m-%d")
        )
        self.response.write(new_car.put())
        self.redirect('/car')

    def Delete(self):
        _car = Car.get_by_id(int(self.request.get('id')))
        if _car:
            _car.key.delete()
