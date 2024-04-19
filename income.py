from transaction import Transaction

class Income(Transaction):
    def __init__(self, desc, amount, date):
        super().__init__(desc, amount, date)
