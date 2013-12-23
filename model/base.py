from google.appengine.ext import ndb
import datetime

class BaseModel(ndb.Model):
    id = ndb.KeyProperty

    def json(self):
        if not self._fields:
            return {}
        _result = {}
        for _f in self._fields:
            _result[_f] = getattr(self, _f)
            if isinstance(_result[_f], datetime.datetime) \
                or isinstance(_result[_f], datetime.date):
                _result[_f] = str(_result[_f])
        return _result

    @classmethod
    def all(cls, query = None, key = None, order = None):
        if query:
            _query = cls.query(query, ancestor=key)
        else:
            _query = cls.query(ancestor=key)
        if order:
            _query = _query.order(order)

        return _query


