from extract_file.extract_CSV_file_with_header import extract_csv_headers
def format_csv():
    extracted_csv_with_headers_in_list_of_dictionary = extract_csv_headers()
    rows = []
    for row in extracted_csv_with_headers_in_list_of_dictionary:
        arr = []
        # Dictionary comprehension could not be used here,
        # It is because of the multiple if clauses in the dictionary comprehension.They are equivalent to and operation
        # where all conditions have to be true.
        # arr = {x: y for (x, y) in row.items() if x == 'First Name' if x == 'Second Name' if x == 'Age (Years)'}
        for x, y in row.items():
            # print(y)
            if x == 'First Name':
                arr.append(y)
            elif x == 'Second Name':
                arr.append(y)
            elif x == 'Age (Years)':
                arr.append(y)
        rows.append(arr)
    rows.pop(0)
    print(rows)
    return rows

