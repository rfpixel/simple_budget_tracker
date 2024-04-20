from datetime import datetime

#TODO: add validations like date, desc, amount
class Transaction:
    def __init__(self, desc, amount, date):
        self._description = desc
        self._amount = amount
        if self._is_date(date):
            self._date = date
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, desc):
        self._description = desc
    
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if self._is_date(date):
            self._date = date
    
    def _is_date(self, testdata):
        date_format = "%d/%m/%Y"
        try:
            bool(datetime.strptime(testdata, date_format))
            return True
        except ValueError:
            return False
    