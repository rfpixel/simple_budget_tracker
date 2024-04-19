from datetime import datetime
import csv 

class BudgetTracker:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.income = 0
        self.expenses = []
    
    def add_income(self, amount):
        self.income += amount
        self.balance += amount

    def add_expense(self, desc, amount, date):
        self.balance -= amount
        self.expenses.append((desc, amount, date))
    
    def get_balance(self):
        return self.balance
    
    def get_income(self):
        return self.income
    
    def get_expenses(self):
        return self.expenses
    
    def get_total_expenses(self):
        return sum([expense[1] for expense in self.expenses])
    
    def get_account_info(self):
        print(f"Balance: {self.balance}")
        print(f"Total Income: {self.income}")
        print(f"Total Expenses: {self.get_total_expenses()}")
        print("Expenses of the month")
        for expense in self.get_expenses():
            print(f"{expense[0]} --- $ {expense[1]} --- {expense[2]}")

    def get_expenses_month(self, month, year):
        total_by_month = 0
        for expense in self.expenses:
            date_string = expense[2]
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            if date_object.month == month and date_object.year == year:
                print(f"{expense[0]} --- $ {expense[1]} --- {expense[2]}")
                total_by_month += expense[1]
            
        print(f"Total by {self.get_month(month)} {year} --- ${total_by_month}")

    def get_month(self, month):
        if month < 1 and month > 12:
            return None
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        return  months[month-1].capitalize()
    
    def read_csv(self, csv_file_path):
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    #clean the row from csv file
                    cleaned_row = [t.strip() for t in row] 
                    print(cleaned_row)
                    self.add_expense(cleaned_row[0], float(cleaned_row[1]), cleaned_row[2])

rafa_tracking  = BudgetTracker(1000)
rafa_tracking.add_income(100)
rafa_tracking.add_income(100)
rafa_tracking.add_expense("Game",150,  "15/02/2024")
rafa_tracking.add_expense("Supermarket",150, "15/02/2024")
rafa_tracking.add_expense("Microsoft",150, "16/03/2024")
rafa_tracking.add_expense("Microsoft",250, "16/03/2024")
rafa_tracking.add_expense("Microsoft",350, "17/03/2024")
rafa_tracking.add_expense("Microsoft",150.05, "18/03/2024")
rafa_tracking.add_expense("Microsoft",10.01, "19/03/2024")
rafa_tracking.add_expense("Microsoft",10.99, "19/03/2024")

#rafa_tracking.get_account_info()
#rafa_tracking.get_expenses_month(3,2024)
rafa_tracking.read_csv('./expenses_december.csv')
#rafa_tracking.get_account_info()
rafa_tracking.get_expenses_month(12,2024)