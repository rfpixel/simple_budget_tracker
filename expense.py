from datetime import datetime
from transaction import Transaction

class Expense(Transaction):
    def __init__(self, desc, amount, date, payment):
        #self.expenses = []
        super().__init__(desc, amount, date)
        #self.add_expense(desc, amount, date)
        self.payment = payment
    
    def get_payment(self):
        return self.payment