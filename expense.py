from datetime import datetime
from transaction import Transaction

class Expense(Transaction):
    def __init__(self, desc, amount, date, type_payment):
        #self.expenses = []
        super().__init__(desc, amount, date)
        #self.add_expense(desc, amount, date)
        self._payment = type_payment
    
    @property
    def payment(self):
        return self._payment
    @payment.setter
    def payment(self, type_payment):
        self._payment = type_payment