from datetime import datetime
from income import Income
from expense import Expense
#from csvtracker import CsvTracker
from csvtracker import CSVContext, CSVIncome, CSVExpense

class BudgetTracker:
    def __init__(self, name):
        self._expenses = []
        self._incomes = []
        self._name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    def add_income(self, income):
        if not isinstance(income, Income):
            print("Invalid income object")
            return
        self._incomes.append(income)
    
    def get_incomes(self):
        return self._incomes
    
    def calculate_income_by_month(self, month, year):
        total_by_month = 0
        for income in self._incomes:
            date_string = income.get_date()
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            if date_object.month == month and date_object.year == year:
                total_by_month += income.get_amount()
        return total_by_month

    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            print("Invalid expense object")
            return

        self._expenses.append(expense)

    def get_expenses(self):
        return self._expenses
       
    def calculate_expenses_by_month(self, month, year):
        total_by_month = 0
        for expense in self._expenses:
            date_string = expense.date
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            if date_object.month == month and date_object.year == year:
                total_by_month += expense.amount
        return total_by_month
    
    def _get_month(self, month):
        if month < 1 and month > 12:
            return None
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        return  months[month-1].capitalize()

    def calculate_balance_month(self, month, year):
        total_expense = self.calculate_expenses_by_month(month, year)
        total_income = self.calculate_income_by_month(month,year)
        return total_income - total_expense
    
    def load_csv_income(self, filepath):
        context = CSVContext(CSVIncome())
        context.read_csv(filepath)
    
    def load_csv_expenses(self, filepath):
        context = CSVContext(CSVExpense())
        expenses = context.read_csv(filepath)
        for e in expenses:
            self.add_expense(e)

"""     def load_csv_expenses(self, file_path):
        #csvtracking = CsvTracker('./expenses_december.csv')
        csvtracking = CsvTracker(file_path)
        expenses = csvtracking.read_csv_expenses()
        for e in expenses:
            self.add_expense(e)
 """

    