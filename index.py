import webapp2
from controller import BaseController, CarController


application = webapp2.WSGIApplication([
                                          (r'/', CarController),
                                          (r'/car', CarController),
                                          (r'/car/(\d+)', CarController),
                                      ], debug=True)

