from pony.orm import db_session, commit, Database
from extract_file.extract_JSON import extract_json
from extract_file.extract_XML import extract_xml
from pony import orm
from models.unifyEntity_XML_JSON import json_xml_combine_entity

user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'student_229016929'


def unify_xml_json():
    db = Database()
    # This is used to bind the database management system to ponyORM
    db.bind(provider='mysql', host=host, user=user, passwd=password, db=database)
    file_entity = json_xml_combine_entity(db, orm)
    db.generate_mapping(create_tables=True)

    #         format xml file to conform to entity structure
    root = extract_xml()
    final_list = []
    for child in root:
        arr = []
        for x, y in child.attrib.items():
            # loop through dictionary to create table columns from item
            if x == 'firstName':
                arr.append(y)
            elif x == 'lastName':
                arr.append(y)
            elif x == 'age':
                arr.append(int(y))
            elif x == 'address_postcode':
                arr.append(y)
        final_list.append(arr)


    # format json file to conform to entity structure
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
            elif x == 'address_postcode':
                arr.append(y)
        final_list.append(arr)
        # print(final_list)

# loop through the final list to pick each row, then store it into the databse
    for item in final_list:
        with db_session:
            file_entity(first_name=item[0], second_name=item[1], age=item[2], address_post_code=item[3])
            commit()
