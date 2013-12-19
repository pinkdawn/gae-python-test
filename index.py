import webapp2
from controller import BaseController, CarController


application = webapp2.WSGIApplication([
                                          ('/', CarController),
                                          (r'/car', CarController),
                                      ], debug=True)

