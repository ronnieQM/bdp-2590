import os
import sys
import csv
import time
import json
import copy
# import xml.dom.minidom
from xml.dom import minidom
import xml.etree.ElementTree as ET
from quick_tools import breakout, clearit, breakpoint

import pickle

import pandas as pd
from prettytable import PrettyTable

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

schema_dictionary = {
    "name": None,
    "attrs_list": [],
    "unique_attrs": {},
    "element_list": [],
    "unique_elements": {},
    "values": []
}

convert_data_dict = {
    "xs:string": "VARCHAR(255)",
    "xs:dateTime": "DATETIME",
    "xs:decimal": "FLOAT",
    "xs:integer": "INT"
    # "xs:boolean
    # xs:date
    # xs:time
}

# elements with NO elements
indicator_list = []
table_list = []
allelems = []
type_elems = []
dll_list = []
elems_with_bi_types = []
elems_with_global_types = []
elems_simple = []
elems_with_base = []

rcount = 0

class Node:
    def __init__(self, data):
        """Initialize this node with the given dataa"""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """"Return a string representation of this node"""
        return 'Node {}'.format(self.data)

class DLL:
    def __init__(self):
        self.head = None
        self.length = 0
        self.order = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def listprint(self, node=None):
        if node is None:
            node = self.head
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def iterate(self, node=None):
        elem_list = []
        if node is Node:
            node = self.head
        while node is not None:
            elem_list.append(node)
            node = node.next
        return elem_list

    def getlen(self):
        # print(self.length)
        return self.length

    def __len__(self, node=None):
        if node is None:
            node = self.head
        c = 0
        while node is not None:
            c += 1
            node = node.next
        return c


    def __str__(self):
        return "asdfasdfasdfasdf"

    def __repr__(self):
        # return self.head.data
        return "asdfasdf"

def recursive_iterate(node, level=0):
    """takes in element xml.etree.ElementTree.Element | ET.parse(XML_file).getroot()"""
    global rcount
    global allelems
    level += 1

    for subnode in node:
        print('count: ', rcount)
        # print('level: ', level)
        rcount += 1
        allelems.append(subnode)
        if len(subnode) != 0:
            another_one(subnode, level)
    return rcount, allelems

def get_parent_of_type(etree_elem, level=0, iter_count=1, dll=None):
    """takes in element xml.etree.ElementTree.Element | ET.parse(XML_file).getroot()"""
    global type_elems
    global dll_list
    level += 1
    iter_count+=1
    print("-----------------inside of 'get_parent_of_type, level: {}--------------".format(level))
    if dll is None:
        dll = DLL()
        dll.push(etree_elem)
    else:
        dll = dll
    for subnode in etree_elem:
        iter_count += 1
        new_dll = copy.deepcopy(dll)
        new_dll.push(subnode)
        if 'type' in subnode.attrib.keys():
            type_elems.append(subnode)  # list of elements with 'type' in it
            dll_list.append(new_dll)  # list of DLLs
        else:
            if len(subnode) >= 1:
                # iter_count += 1
                get_parent_of_type(subnode, level,iter_count, new_dll)

    return iter_count, type_elems, dll_list

def tree_iter(tree):
    """ returns # of elems in XML """
    c=0
    for i in tree.iter():
        c+=1
    return c

def create_table(list_of_columns, table_name):
    table_name = table_name.replace(" ", "_")
    l = len(list_of_columns) - 1
    s = ""
    for i in list_of_columns:
        if list_of_columns.index(i) != l:
            s += i + ', \n'
        else:
            s += i

    x = 'CREATE TABLE ' + table_name + ' ('
    y = x + s + ');'
    print(y)
    return

def insert_query(table, list_of_vals):
    a = 'INSERT INTO '

def get_tid(file_name):
    tracking_list = []
    d_list = []  # duplicates

    tid = file_name
    tid = '.'.join(tid.split('.', 2)[:2])

    if tid not in tracking_list:
        tracking_list.append(tid)
    else:
        print('!!!!!!!!!!!1')
        if tid not in d_list:
            d_list.append(tid)
    return tid  # type: str

def data2db(xml_file):
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
    # value_dict = {
    #     'pk': 'id',
    #     'transactionId': 'VARCHAR(255)',
    #     'recipientsXNAddress': 'VARCHAR(255)',
    #     'recipientsXM8UserId': 'VARCHAR(255)' ,
    #     'stamp': 'VARCHAR(255)',
    #     'CONTROL_POINT_type':'VARCHAR(255)',
    #     'CONTACT_type': 'VARCHAR(255)',
    #     'contact_name':'VARCHAR(255)',
    #     'PHONE_type': 'VARCHAR(255)',
    #     'number': 'VARCHAR(255)',
    #     'extension': 'VARCHAR(255)',
    #     'claimNumber': 'VARCHAR(255)',
    #     'origTransactionId': 'VARCHAR(255)',
    # }



    print(dummy_list)
    headers = ['ID']
    list_of_headers = []
    values = []
    for x in dummy_list:
        templist = [pk]
        print('     -----------------> looking for {} <-------------------'.format(x))
        for node in root.iter(x):
            # print(node)
            # print(node.attrib)
            # print(ET.tostring(node))
            for i, j in node.attrib.items():
                print(i, len(i), ' : ', j, len(j))
                if i not in headers:
                    headers.append(i)
                templist.append(j)
                values.append(templist)
        # print(headers)
        # print(values)

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
            # print('going to look for ', i, 'in node #', temp_count)
            if i == tag:
                print(t, ET.tostring(node))
                for key, value in node.attrib.items():
                    if key == 'type':
                        key = tag + '_' + key
                    if key not in headers:
                        headers.append(key)
                    # print(t, key, ' : ', value)
                    templist.append(value)
                    reallist.append(value)
                    # print(t, 'headers', headers)
                    # print(t, 'values', reallist)

                    print(key, value)
                    if key in value_dict.keys():
                        value_dict['pk'] = pk
                        value_dict[key] = value

                values.append(templist)

    # print(' ')
    # print(' ')
    # print(' ')
    # print(headers)
    # print(reallist)
    # print(len(headers))
    # print(len(reallist))
    #
    # prettyprint = PrettyTable(headers)
    # prettyprint.add_row(reallist)
    # print(prettyprint)
    print('-----------------------------------------------^^^^^----------------------------------------------')

    rows = reallist
    return headers, rows, value_dict

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

    print(len(vals))
    print('TOTAL FILES PROCESSED')
    print('Length of list: ', len(list_of_value_dicts))



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

if __name__ == '__main__':
    # main()
    # demo1()
    demo2()
    # create_table(these_columns, this_table)
