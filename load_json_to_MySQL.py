from pony.orm import Database, db_session, commit
from pony import orm
from models.jsonEntity import json_entity
user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'student_229016929'


def load_json_into_mysql(file):
    try:
        db = Database()
        db.bind(provider='mysql', host=host, user=user, passwd=password, db=database)
        file_entity = json_entity(db, orm)
        db.generate_mapping(create_tables=True)
        with db_session:
            # since some row does not have the dept entry so,  a conditional statement is used to prevent an out
            # of range error which is caused as a result of accessing a value with an index that does not exist
            # in the list.
            if len(file) == 12:
                file_entity(first_name=file[0], second_name=file[1], age=file[2],
                            iban=file[3], credit_card_number=file[4], credit_card_security_code=file[5],
                            credit_card_start_date=file[6],
                            credit_card_end_date=file[7],
                            address_main=file[8], address_city=file[9], address_post_code=file[10],
                            debt=file[11])
                commit()
            else:
                file_entity(first_name=file[0], second_name=file[1], age=file[2],
                            iban=file[3], credit_card_number=file[4], credit_card_security_code=file[5],
                            credit_card_start_date=file[6],
                            credit_card_end_date=file[7],
                            address_main=file[8], address_city=file[9], address_post_code=file[10])
                commit()
        db.disconnect()

    except Exception as error:
        print("Data error " + str(error))
