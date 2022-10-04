import csv
import os

class Dataset():
    files_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'/file')

    def read_file(self,name_file):
        file_path = os.path.join(self.files_path,f'{name_file}')
        
        with open(file_path, encoding='utf-8') as file:
            readlines = csv.DictReader(file)
            for line in readlines:
                print(line)


dataset = Dataset()
dataset.read_file('Suicide_Detection.csv')