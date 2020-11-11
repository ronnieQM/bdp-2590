import os
import sys
import csv
import time
import json
import copy
import pickle
# import xml.dom.minidom
from xml.dom import minidom
import xml.etree.ElementTree as ET


import pandas as pd
from sql_formatter import field_formatter, generate_create_query, values_formatter, generate_insert_query
from quick_tools import breakout, clearit, breakpoint

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

