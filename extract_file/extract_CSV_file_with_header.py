import csv
import os
from extract_file.extract_CSV import extract_csv_x

dir = r'/Users/peterchukwu/Desktop/CETM50'


def extract_csv_headers():
    try:
        directory = dir
        data = extract_csv_x()
        HEADER_S = next(data)
        for file_name in os.listdir(directory):
            if file_name.endswith(".csv"):
                f = os.path.join(directory, file_name)
                if os.path.isfile(f):
                    csv_file = open(f)
                    csvreader = csv.DictReader(csv_file, HEADER_S)
                    return csvreader
    except Exception as error:
        print("Data error " + str(error))
