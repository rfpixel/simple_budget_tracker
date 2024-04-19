from datetime import datetime
from income import Income
from expense import Expense
from csvtracker import CsvTracker

class BudgetTracker:
    def __init__(self, name):
        self.expenses = []
        self.incomes = []
        self.name = name
    
    def get_budget_name(self):
        return self.name
    
    def add_income(self, income):
        if not isinstance(income, Income):
            print("Invalid income object")
            return
        self.incomes.append(income)
    
    def get_incomes(self):
        return self.incomes
    
    def calculate_income_by_month(self, month, year):
        total_by_month = 0
        for income in self.incomes:
            date_string = income.get_date()
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            if date_object.month == month and date_object.year == year:
                total_by_month += income.get_amount()
        return total_by_month

    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            print("Invalid expense object")
            return

        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses
       
    def calculate_expenses_by_month(self, month, year):
        total_by_month = 0
        for expense in self.expenses:
            date_string = expense.get_date()
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            if date_object.month == month and date_object.year == year:
                total_by_month += expense.get_amount()
        return total_by_month
    
    def _get_month(self, month):
        if month < 1 and month > 12:
            return None
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        return  months[month-1].capitalize()

    def load_csv_expenses(self, file_path):
        #csvtracking = CsvTracker('./expenses_december.csv')
        csvtracking = CsvTracker(file_path)
        expenses = csvtracking.read_csv_expenses()
        for e in expenses:
            self.add_expense(e)

    def calculate_balance_month(self, month, year):
        total_expense = self.calculate_expenses_by_month(month, year)
        total_income = self.calculate_income_by_month(month,year)
        return total_income - total_expense