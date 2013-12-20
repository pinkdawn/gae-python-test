from google.appengine.ext import ndb

class BaseModel(ndb.Model):
    id = ndb.KeyProperty

    @classmethod
    def all(cls, key = None, order = None):
        _query = cls.query(ancestor=key)
        if order:
            _query = _query.order(order)

        return _query


