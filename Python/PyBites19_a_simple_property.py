"""
Write a simple Promo class. Its constructor receives a name str and expires datetime.

Add a property called expired which returns a boolean value indicating whether the promo has expired or not.
"""
import datetime

class Promo(object):
    def __init__(self, name, expires):
        self._name = name
        self._expires = expires
    
    @property
    def expired(self):
        return self._expires - datetime.date.today() < datetime.timedelta(0)

a = Promo('sei la', datetime.date(2020, 5, 24))

print(a.expired)