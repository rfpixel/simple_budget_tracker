from datetime import datetime
import csv

class CsvTracker:
    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        
    def read_csv(self):
        with open(self.file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    #clean the row from csv file
                    cleaned_row = [t.strip() for t in row]
                    #convert price to a float
                    cleaned_row[1] = float(cleaned_row[1])

                    #check if the row is valid format
                    if self.is_valid(cleaned_row):
                        print(cleaned_row)
                    else:
                        print("invalid csv data. Check format: shop name,price,date")
                    #self.add_expense(cleaned_row[0], float(cleaned_row[1]), cleaned_row[2])

    def is_valid(self, row):
        return self.is_string(row[0]) and self.is_number(row[1]) and self.is_date(row[2])
    
    def is_string(self, testdata):
        if isinstance(testdata, str):
            return True
        else:
            return False
        
    def is_date(self, testdata):
        date_format = "%d/%m/%Y"
        try:
            bool(datetime.strptime(testdata, date_format))
            return True
        except ValueError:
            return False

    def is_number(self, testdata):
        if isinstance(testdata, (int,float)):
            return True
        else:
            return False

test_csv = CsvTracker('./expenses_december.csv')
test_csv.read_csv()

""" 
print(test_csv.is_date('12/04/2024'))
print(test_csv.is_number('test'))
print(test_csv.is_string('200')) 
"""