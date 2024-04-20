from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import csv
from expense import Expense

class ValidData:
    @staticmethod
    def is_string(testdata):
        if isinstance(testdata, str):
            return True
        else:
            return False
    
    @staticmethod
    def is_date(testdata):
        date_format = "%d/%m/%Y"
        try:
            bool(datetime.strptime(testdata, date_format))
            return True
        except ValueError:
            return False
    @staticmethod
    def is_number(testdata):
        if isinstance(testdata, (int,float)):
            return True
        else:
            return False

class CSVContext:
    def __init__(self, strategy: CSVStrategy):
        self._strategy = strategy
        self._filepath = ''
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: CSVStrategy):
        self._strategy = strategy

    def read_csv(self, filepath):
        self._filepath = filepath
        return self._strategy.read_csv(self._filepath)

class CSVStrategy(ABC):
    @abstractmethod
    def read_csv(self, filepath):
        pass

class CSVIncome(CSVStrategy):
    def read_csv(self, filepath):
        #do something
        print("reading Income file")

class CSVExpense(CSVStrategy):
    def _is_valid_expense(self, row):
        return ValidData.is_string(row[0]) and ValidData.is_number(row[1]) and ValidData.is_date(row[2]) and ValidData.is_string(row[3]) 
    
    def _create_expense(self, row):
        expense = Expense(row[0],row[1],row[2],row[3])
        return expense
    
    def read_csv(self, filepath):
        #do something
        expenses = []
        with open(filepath, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    #clean the row from csv file
                    cleaned_row = [t.strip() for t in row]
                    #convert price to a float
                    cleaned_row[1] = float(cleaned_row[1])

                    #check if the row is valid format
                    if self._is_valid_expense(cleaned_row):
                        #print(cleaned_row)
                        #expenses.append(cleaned_row)
                        e = self._create_expense(cleaned_row)
                        expenses.append(e)
                    else:
                        print("invalid csv data. Check format: shop name,price,date")
                        print(f"Please check the following line: {cleaned_row}\n")
                    #self.add_expense(cleaned_row[0], float(cleaned_row[1]), cleaned_row[2])
        #print(expenses)
        return expenses

""" if __name__ == "__main__":
   context = CSVContext(CSVIncome())
   context.read_csv('./incomes_december.csv')

   context.strategy = CSVExpense()
   context.read_csv('./expenses_december.csv') """