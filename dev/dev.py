import os
import sys
import logging
import logging.handlers as handlers

os.chdir(
    (os.path.dirname(os.path.abspath(__file__))))  # change dir to dir where python scripts reside # project/scripts
sys.path.insert(1, os.path.dirname(os.getcwd()))
from xml_framework import get_tid, data2db, get_elem_count, recursive_search, recursive_iterate, get_parent_of_type
from xml_framework import field_formatter,generate_insert_query, generate_create_query, values_formatter,generate_bd_schema

t = '\t'
n = '\n'

logger = logging.getLogger('xml2db').setLevel(level=logging.DEBUG)
###############################
#    define directories
###############################
os.chdir(
    (os.path.dirname(os.path.abspath(__file__))))  # change dir to dir where python scripts reside # project/scripts
script_dir = os.getcwd()  # define projects/scripts
project_dir = os.path.dirname(script_dir)  # define projects/
data_dir = os.path.join(project_dir, 'data')  # define data/

# data subdirectories
status_dir = os.path.join(data_dir, 'status')
# status_dir = os.path.join(data_dir, 'status_test')
customDoc_data_dir = os.path.join(data_dir, 'customDoc')
estimate_data_dir = os.path.join(data_dir, 'estimate')
note_data_dir = os.path.join(data_dir, 'note')

# xsds_dir, data_dict_dir
data_dict_dir = os.path.join(project_dir, 'data_dicts')
xsds_dir = os.path.join(project_dir, 'xsds')

# XSD paths
generic_first_draft_xsd = os.path.join(xsds_dir, 'generic_roughdraft_7.9.18.xsd')
standard_carrier_xsd = os.path.join(xsds_dir, 'StandardCarrierExport-v1.7.xsd')
standard_status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')
activity_diary_xsd = os.path.join(xsds_dir, 'DefaultActivityDiaryExport.xsd')
standard_note_xsd = os.path.join(xsds_dir, 'StandardNoteExport.xsd')
custom_doc_xsd = os.path.join(xsds_dir, 'CustomDocExport.xsd')

# print(standard_carrier_xsd)
# print(project_dir)
# print(data_dict_dir)
# print(data_dir)
# print(script_dir)


def read_xsds():
    logging.info('inside dev.read_xsds')
    # list of XSD files
    path, dirs, files = next(os.walk(xsds_dir))
    # for file in files:
    #     print(os.path.join(path, file))
    # iter_count,type_elems,dll_list= get_parent_of_type(standard_status_xsd)
    # print(len(dll_list))
    # for i in dll_list:
    #     i.listprint()
    #     print('---------')
    generate_bd_schema(standard_status_xsd)

def data2db(xml_file: str):
    print('--inside data2db --')
    xf = os.path.basename(xml_file)
    pk = get_tid(xf)
    # print(xml_file)
    tree = ET.parse(xml_file, parser=None)
    root = tree.getroot()

    # print('--------------------------------------------------------------------------------------------------------')
    nothing = ['name', 'stamp', 'claimNumber', 'recipientsXM8UserId', 'recipientsXNAddress', 'origTransactionId']
    some_list = ['CONTACT', 'CONTACT', 'CONTROL_POINT', 'CONTROL_POINT', 'PHONE', 'PHONE', 'PHONE', 'TYPEOFLOSS',
                 'XACTNET_INFO', 'XACTNET_INFO', 'XACTNET_INFO', 'XACTNET_INFO']
    dummy_list = ['CONTACT', 'CONTROL_POINT', 'PHONE', 'TYPEOFLOSS', 'XACTNET_INFO']
    value_dict = {
        'pk': None,
        'transactionId': None,
        'recipientsXNAddress': None,
        'recipientsXM8UserId': None,
        'stamp': None,
        'CONTROL_POINT_type': None,
        'CONTACT_type': None,
        'contact_name': None,
        'PHONE_type': None,
        'number': None,
        'extension': None,
        'claimNumber': None,
        'origTransactionId': None,
    }
    list_of_format_dict = []
    print(dummy_list)
    headers = ['ID']
    list_of_headers = []
    values = []
    for x in dummy_list:
        templist = [pk]
        print('     -----------------> looking for {} <-------------------'.format(x))
        for node in root.iter(x):
            print(node)
            print(node.attrib)
            print(ET.tostring(node))
            for i, j in node.attrib.items():
                print(i, len(i), ' : ', j, len(j))
                if i not in headers:
                    headers.append(i)
                templist.append(j)
                values.append(templist)
        print(headers)
        print(values)

    print(
        '----------------------------------------------------THIS IS A NEW FILE---------------------------------------------')
    print('filename: ', xf, 'pk: ', pk)
    temp_count = 0
    reallist = [pk]
    for node in root.iter():
        temp_count += 1
        templist = [pk]
        tag = node.tag
        for i in dummy_list:
            print('going to look for ', i, 'in node #', temp_count)
            time.sleep(.05)
            if i == tag:
                print(t, ET.tostring(node))
                for key, value in node.attrib.items():
                    if key == 'type':
                        key = tag + '_' + key
                    if key not in headers:
                        headers.append(key)
                    print(t, key, ' : ', value)
                    templist.append(value)
                    reallist.append(value)
                    print(t, 'headers', headers)
                    print(t, 'values', reallist)

                    print(key, value)
                    if key in value_dict.keys():
                        value_dict['pk'] = pk
                        value_dict[key] = value

                values.append(templist)

    print(' ')
    print(' ')
    print(' ')
    # print(headers)
    # print(reallist)
    # print(len(headers))
    # print(len(reallist))
    #
    # prettyprint = PrettyTable(headers)
    # prettyprint.add_row(reallist)
    # print(prettyprint)
    # print('-----------------------------------------------^^^^^----------------------------------------------')

    rows = reallist
    return headers, rows, valu


def main():
    read_xsds()


if __name__ == "__main__":
    logging.basicConfig()
    logging.root.setLevel(logging.DEBUG)
    main()
