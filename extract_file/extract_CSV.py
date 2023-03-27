import csv
import os

dir = r'/Users/peterchukwu/Desktop/CETM50'

def extract_csv_x():
    try:
        directory = dir
        for file_name in os.listdir(directory):
            if file_name.endswith(".csv"):
                f = os.path.join(directory, file_name)
                if os.path.isfile(f):
                    csv_file = open(f)
                    csvreader = csv.reader(csv_file)
                    return csvreader
    except Exception as error:
        print("Data error " + str(error))
