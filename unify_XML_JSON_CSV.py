from pony.orm import db_session, commit, Database
from format_file.format_XML import format_xml
from format_file.format_CSV import format_csv
from extract_file.extract_JSON import extract_json
from extract_file.extract_XML import extract_xml
from pony import orm
from models.unifyEntity_XML_JSON_CSV import json_xml_csv_combine_entity

user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'student_229016929'


def unify_json_xml_csv():
    db = Database()
    db.bind(provider='mysql', host=host, user=user, passwd=password, db=database)
    file_entity = json_xml_csv_combine_entity(db, orm)
    db.generate_mapping(create_tables=True)

    #   get formatted .xml list
    xml_list = format_xml()
    # get formatted .csv list
    csv_list = format_csv()
    final_list = []

    #  loop through the csv list to get each list in the list then append it to the final list
    for xml_child_list in xml_list:
        final_list.append(xml_child_list)

    #  loop through the csv list to get each list in the list then append it to the final list
    for csv_child_list in csv_list:
        final_list.append(csv_child_list)

    # get extracted json file, then format the .json file, to conform with our entity structure
    json_reader = extract_json()
    for row in json_reader:
        arr = []
        for x, y in row.items():
            if x == 'firstName':
                arr.append(y)
            elif x == 'lastName':
                arr.append(y)
            elif x == 'age':
                arr.append(int(y))
        final_list.append(arr)
    print(final_list)

    for item in final_list:
        # Loads the formated unified columns data into the database
        with db_session:
            file_entity(first_name=item[0], second_name=item[1], age=item[2])
            commit()
