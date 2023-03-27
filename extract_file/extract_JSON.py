import json
import os

dir = r'/Users/peterchukwu/Desktop/CETM50'


def extract_json():
    try:
        directory = dir
        # look into the directory get all the files
        for file_name in os.listdir(directory):
            # get file without extension
            if file_name.endswith(".json"):
                f = os.path.join(directory, file_name)
                # check if it is a file
                if os.path.isfile(f):
                    json_file = open(f)
                    json_reader = json.load(json_file)
                    return json_reader
    except Exception as error:
        print("Data error " + str(error))
