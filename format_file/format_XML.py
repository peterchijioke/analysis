from extract_file.extract_XML import extract_xml


def format_xml():
    root = extract_xml()
    final_list=[]
    for child in root:
        arr = []
        # print(child.attrib)
        
        for x, y in child.attrib.items():
            # print(y)
            if x == 'firstName':
                arr.append(y)
            elif x == 'lastName':
                arr.append(y)
            elif x == 'age':
                arr.append(int(y))
        final_list.append(arr)
    print(final_list)
    return final_list
