from income import Income
from expense import Expense
from tracker import BudgetTracker


tracking_rafael = BudgetTracker("Rafael")

i = Income("salary",1000, "12/01/2024")
tracking_rafael.add_income(i)
i = Income("pc repair",1000, "13/01/2024")
tracking_rafael.add_income(i)
e = Expense("Supermarket", 200, "20/01/2024", "Visa debit card")
tracking_rafael.add_expense(e)
e = Expense("Supermarket", 300, "20/01/2024", "Visa debit card")
tracking_rafael.add_expense(e)
e = Expense("Supermarket", 300, "20/01/2024", "Visa debit card")
tracking_rafael.add_expense(e)

# tracking_rafael.load_csv_expenses('./expenses_december.csv')

# total_expense = tracking_rafael.calculate_expenses_by_month(12,2024)
# print(f"Expense: {total_expense}")

# total_income = tracking_rafael.calculate_income_by_month(1,2024)
# print(f"Income: {total_income}")

balance = tracking_rafael.calculate_balance_month(1,2024)
print(f"Balance: {balance}")