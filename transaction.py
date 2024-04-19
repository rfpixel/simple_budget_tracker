from datetime import datetime

#TODO: add validations like date, desc, amount
class Transaction:
    def __init__(self, desc, amount, date):
        self.description = desc
        self.amount = amount
        if self._is_date(date):
            self.date = date
        
    def get_description(self):
        return self.description
    
    def get_amount(self):
        return self.amount
    
    def get_date(self):
        return self.date
    
    def _is_date(self, testdata):
        date_format = "%d/%m/%Y"
        try:
            bool(datetime.strptime(testdata, date_format))
            return True
        except ValueError:
            return False
    