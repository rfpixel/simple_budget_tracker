from datetime import datetime
import csv

class CsvTracker:
    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        
    def read_csv(self):
        expense_list = []
        with open(self.file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    #clean the row from csv file
                    cleaned_row = [t.strip() for t in row]
                    #convert price to a float
                    cleaned_row[1] = float(cleaned_row[1])

                    #check if the row is valid format
                    if self._is_valid(cleaned_row):
                        #print(cleaned_row)
                        expense_list.append(cleaned_row)
                    else:
                        print("invalid csv data. Check format: shop name,price,date")
                        print(f"Please check the following line: {cleaned_row}\n")
                    #self.add_expense(cleaned_row[0], float(cleaned_row[1]), cleaned_row[2])
        #print(expense_list)
        return expense_list

    def _is_valid(self, row):
        return self._is_string(row[0]) and self._is_number(row[1]) and self._is_date(row[2])
    
    def _is_string(self, testdata):
        if isinstance(testdata, str):
            return True
        else:
            return False
        
    def _is_date(self, testdata):
        date_format = "%d/%m/%Y"
        try:
            bool(datetime.strptime(testdata, date_format))
            return True
        except ValueError:
            return False

    def _is_number(self, testdata):
        if isinstance(testdata, (int,float)):
            return True
        else:
            return False

#test_csv = CsvTracker('./expenses_december.csv')
#test_csv.read_csv()