import os
import xml.etree.ElementTree as ET

dir = r'/Users/peterchukwu/Desktop/CETM50'
def extract_xml():
    try:
        directory = dir
        for file_name in os.listdir(directory):
            if file_name.endswith(".xml"):
                f = os.path.join(directory, file_name)
                # check if it is a file
                if os.path.isfile(f):
                    xml_file = open(f)
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    return root
    except Exception as error:
        print("Data error " + str(error))
