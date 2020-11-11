import sys
import os
from prettytable import PrettyTable
os.chdir((os.path.dirname(os.path.abspath(__file__))))  # change dir to dir where python scripts reside # project/scripts
sys.path.insert(1,os.path.dirname(os.getcwd()))

from solutions.xlm2rdbs import *
from solutions.sql_formatter import field_formatter, generate_create_query, values_formatter,generate_insert_query
from solutions.quick_tools import breakout,clearit,breakpoint

t = '\t'
n = '\n'

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
customDoc_data_dir= os.path.join(data_dir, 'customDoc')
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

def demo2():
    """ XML DATA --> DATABASE """
    print('--inside demo--')
    path, dirs, files = next(os.walk(status_dir))
    mc = len(files) - 1
    rows = []

    c = 0
    headers = []
    list_of_all_possible_headers = []
    list_of_value_dicts = []
    for file in files:
        file = os.path.join(path, file)
        # print(file)
        headers, row, value_dict = data2db(file)
        rows.append(row)
        list_of_value_dicts.append(value_dict)
        print('~~~~~~ files remaining: ', mc, '~~~~~~~~')
        mc -= 1
        c += 1

    # if not os.path.isfile('status_list_of_value_dicts.pkl'):
    #     with open('status_list_of_value_dicts.pkl', 'wb') as f:
    #         pickle.dump(list_of_value_dicts, f)
    # else:
    #     print('pickle exists')

    """
    print(c)
    headers = list(list_of_value_dicts[0].keys())
    prettyprint = PrettyTable(headers)
    c = 0
    for i in list_of_value_dicts:
        row = list(i.values())
        prettyprint.add_row(row)
        c += 1
    print(prettyprint)
    """

    header_list = []
    # headers = list([0].keys())
    print(headers)
    print(headers)
    print(headers)
    vals = []
    for i in list_of_value_dicts:
        row = list(i.values())
        vals.append(row)

    for i in vals:
        print(i)

    xheaders = []
    # print('!!!!!!!!!!!!!!!!!!!!!!11')
    # for i in headers:
    #     print(i)
    #     v = 'VARCHAR(255)'
    #     i = i + ' ' + v
    #     xheaders.append(i)
    # for i in xheaders:
    #     print(i)
    # create_table(xheaders, 'some_table')
    # print('!!!!!!!!!!!!!!!!!!!!!!11')
    print('!!!!!!!!!!!!!!!!!!!!!!11')
    this_list =[]
    for i in vals[0]:
        # print(i,' | ', type(i))
        v = ' VARCHAR(255), '
        if i is not None:
            i = i + v
        else:
            i = ' '
        this_list.append(i)
    print(this_list)


    print('!!!!!!!!!!!!!!!!!!!!!!11')

    # def insterter(row):


    print(len(vals))
    print('TOTAL FILES PROCESSED')
    print('Length of list: ', len(list_of_value_dicts))

    # read header from list of value dicts

    headers = list(list_of_value_dicts[0].keys())
    print(headers)
    # use that to create 'create' query

    table_name = 'some_table'
    x = 'CREATE TABLE ' + table_name + ' ('
    for i in headers:
        i = i + ' VARCHAR(255), '
        # print(i)
        x = x + i
    print(x)

    # read first 500 values |  read all the values
    print('!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!')
    print_list = []
    big_text =""
    for i in list_of_value_dicts:
        tlist = []
        some_list = list(i.values())
        for j in some_list:
            if j is None:
                j = ' '
            tlist.append(j)
        z = str(tuple(tlist))
        z = z + ', '
        big_text = big_text + z
    print(big_text)



    # row = tuple((i.values()))
    # print(row)

    # add values to 'insert' query


def demo1():
    print('--- inside demo1 ---')
    file = standard_status_xsd
    tree = ET.parse(file, parser=None)
    root = tree.getroot()

    # if file == generic_first_draft_xsd:
    #     print('!!!!!!!!!')
    #     try:
    #         with open('list_of_dll.pkl', 'rb') as f:
    #             list_of_dll = pickle.load(f)
    #             print('opened pickle!')
    #     except Exception as ex:
    #         print(ex)
    # else:
    #     xcount, list_of_elems_w_type, list_of_dll = get_parent_of_type(root)
    xcount, list_of_elems_w_type, list_of_dll = get_parent_of_type(root)

    print('this is how many elements there are according to etree.iter(): {}'.format(tree_iter(tree)))
    print('this is how many element get_parents_of_type iterates through: {}'.format(xcount))
    print('this is how many things there are in list_of_dlls: {}'.format(len(list_of_dll)))

    # with open('list_of_dll.pkl', 'wb') as f:
    #     pickle.dump(list_of_dll, f)

    tables = []

    elems_with_type = list_of_elems_w_type

    # for i in dll_list:
    #     print('- ' * 45)
    #     dll_node = i.head
    #     while dll_node is not None:
    #         etree_elem = dll_node.data
    #         print(etree_elem.tag.split('}')[1], ' | ', etree_elem.attrib)
    #         dll_node = dll_node.next
    #     print(' ')



    for child in elems_with_type:
        if child.attrib['type'].startswith('xs:'):
            attr = child.attrib
            attr_name = attr['name']
            attr_type = attr['type']
            type_of_element = child.tag.split('}')[1]
            #################### LOGIC ###########################3
            if attr_type in convert_data_dict.keys():
                sql_data_type = convert_data_dict[attr_type]
                temp = attr_name + ' ' + sql_data_type
                header_list.append(temp)

    create_table(headers, test_table)
def main():
    print('- - - - inside main - - - -')

if __name__ == '__main__':
    main()
    # create_table(these_columns, this_table)
