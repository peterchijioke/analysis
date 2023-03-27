from load_json_to_MySQL import load_json_into_mysql

from extract_file.extract_JSON import extract_json


def format_json():
    json_reader = extract_json()
    for row in json_reader:
        print(row)
        arr = []
        for key, value in row.items():
            if key == 'firstName':
                arr.append(value)
            elif key == 'lastName':
                arr.append(value)
            elif key == 'age':
                arr.append(int(value))
            elif key == 'iban':
                arr.append(value)
            elif key == 'credit_card_number':
                arr.append(value)
            elif key == 'credit_card_security_code':
                arr.append(int(value))
            elif key == 'credit_card_start_date':
                arr.append(value)
            elif key == 'credit_card_end_date':
                arr.append(value)
            elif key == 'address_main':
                arr.append(value)
            elif key == 'address_city':
                arr.append(value)
            elif key == 'address_postcode':
                arr.append(value)
            elif key == 'debt':
                if type(value) == str:
                    arr.append(value)
                else:
                    for r, z in value.items():
                        if r == 'amount':
                            arr.append(z)
        load_json_into_mysql(arr)
