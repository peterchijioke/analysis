from unify_json_xml import unify_xml_json
from format_file.format_XML import format_xml
from format_file.format_CSV import format_csv
from format_file.format_JSON import format_json
from unify_XML_JSON_CSV import unify_json_xml_csv
from extract_file.extract_TXT import extract_text

try:
    # uncomment the below function to see extracted json data on console
    # this function also output the json data into the database
    # format_json()

    # uncomment the below function to unify xml and json
    # unify_xml_json()

    # uncomment the below function to unify xml, csv and json
    # unify_json_xml_csv()

    # uncomment the below function to see extracted csv data on console
    format_csv()

    # This line extracts the text from text file.
    # This can not be unified with the other files because it does not have any column that is unifiable
    # extract_text()
except Exception as e:
    print("Data error " + str(e))
