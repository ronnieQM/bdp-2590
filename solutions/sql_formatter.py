def field_formatter(field_list, type_dictionary):
    output = []
    for field in field_list:
        if field in type_dictionary.keys():
            field = field + type_dictionary[field]
            output.append(field)
        else:
            field = field + ' VARCHAR(255)'
            output.append(field)

    output = str(tuple(output)).replace("'",'')
    # output.replace("\"",'')
    return output

def generate_create_query(table_name, columns_with_type):
    query = 'CREATE TABLE IF NOT EXISTS {} {}'.format(table_name, columns_with_type)
    return query

def generate_insert_query(table_name, rows):
    text = 'INSERT INTO {} VALUES {}'.format(table_name, rows)
    return text

def values_formatter(value_list):
    output=[]
    if all(isinstance(i, list) for i in value_list):
        for row in value_list:
            row = tuple(row)
            output.append(row)
        # print('its a list of lists!')
        output=str(output).replace("[",'')
        output = output.replace("]",'')
        return output
    else:
        # print('its a list of values!')
        output = str(tuple(value_list)).replace("'", '')
        return output
