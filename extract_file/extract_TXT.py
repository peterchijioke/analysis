
import os

dir = r'/Users/peterchukwu/Desktop/CETM50'


def extract_text():
    try:
        directory = dir
        for file_name in os.listdir(directory):
            file_ext = os.path.splitext(file_name)[0]

            if file_name.endswith(".txt"):
                file_directory = os.path.join(directory, file_name)
                file = open(file_directory, 'r')

                # List comprehension offers a shorter syntax when you want to create a new list based on the values
                # of an existing list.
                # Split on any whitespace (including tab characters) row = x.split() Append to
                # our list of lists:

                rows = [x.split() for x in file]

                print(rows)

                # This can not be unified with the other files because it does not have unifying columns


    except Exception as error:
        print("Data error " + str(error))
