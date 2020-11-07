import os
import sys
import csv
import time
import json
# import xml.dom.minidom
from xml.dom import minidom
import xml.etree.ElementTree as ET

import pandas as pd
from quick_tools import breakout, clearit, breakpoint

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
status_dir = os.path.join(data_dir, 'status_test')
note_dir = os.path.join(data_dir, 'note')
estimate_dir = os.path.join(data_dir, 'estimate')
customDoc_dir = os.path.join(data_dir, 'customDoc')

# xsds_dir, data_dict_dir
xsds_dir = os.path.join(project_dir, 'xsds')
data_dict_dir = os.path.join(project_dir, 'data_dicts')
status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')

schema_dictionary = {
    "name": None,
    "attrs_list": [],
    "unique_attrs": {},
    "element_list": [],
    "unique_elements": {},
    "values": []
}

# elements with NO elements
indicator_list = []
table_list = []
column1 = []
column2 = []
column3 = []
column4 = []

convert_data_dict = {
    "xs:string": "VARCHAR(255)",
    "xs:dateTime": "DATETIME",
    "xs:decimal": "FLOAT",
    "xs:integer": "INT"
    # "xs:boolean
    # xs:date
    # xs:time
}

type_elems = []
another_list = []
xcount = 0

rcount = 0
allelems = []


class GenericDataDictionaryClass:
    """This is a representations of a generic class file"""

    def __init__(self, elem, attr, val, desc):
        self.element = elem
        self.attribute = attr
        self.value = val
        self.description = desc

    def __str__(self):
        return """
            element: {}
            attribute: {}
            value: {}
            description: {}
            """.format(self.element, self.attribute, self.value, self.description)


class Node:
    def __init__(self, data):
        """Initialize this node with the given dataa"""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """"Return a string representation of this node"""
        return 'Node {}'.format(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.length += 1
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def getlen(self, node):
        print(self.length)


def another_one(node, level=0):
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


def get_parent_of_type(node, level=0):
    """takes in element xml.etree.ElementTree.Element | ET.parse(XML_file).getroot()"""
    global xcount
    global type_elems
    global another_list
    level += 1
    for subnode in node:
        newnode = DoublyLinkedList()
        newnode.push(node)
        if 'type' in subnode.attrib.keys():
            xcount += 1
            type_elems.append(subnode)
            newnode.push(subnode)
            another_list.append(newnode)
        if len(subnode) != 0:
            get_parent_of_type(subnode)
    return xcount, type_elems, another_list


def firstpass():
    print('--inside firstpass--')
    #############################
    #         sample files      #
    #############################
    path, dirs, files = next(os.walk(xsds_dir))
    status_schema = files[0]
    status_schema_path = os.path.join(path, status_schema)
    tree = ET.parse(status_schema_path, parser=None)
    root = tree.getroot()

    elems_with_bi_types = []
    elems_with_global_types = []
    elems_simple = []
    elems_with_base = []
    typescount, y, z = get_parent_of_type(root)
    print(len(z))
    slist = []
    for i in z:
        # i.listprint(i.head)
        etree_element = i.head.data
        parent_element = i.head.next.data
        # print('parent element', ET.tostring(parent_element))
        try:
            x = parent_element.attrib['name']
            print(x)
            slist.append(x)
        except:
            print('!')
    print(slist)

    print('!')
    print('!')
    print('!')
    print('!')
    print('!')
    print('!')
    print('!')
    print('!')
    print('!')
    # print(t, 'type element', ET.tostring(etree_element))
    # print(t, etree_element)
    return None
    for node in tree.iter():
        for subnode in node:
            if 'type' in subnode.attrib.keys():
                print('~ ' * 15)
                print('parent node:')
                print(node)
                try:
                    print(node.attrib['name'])
                except:
                    print('NO NAME')

                print(node.attrib)
                print('node that has a type:')
                print(subnode)
                print(subnode.attrib)
                print(' ')

        # for subnode in node:
        #     if 'type' in subnode.attrib.keys():

    # print(attrib)
    # print('# of nodes: ', len(node))
    # print('node:')
    # print(node)
    # if runner node.!= 0:
    #     if node in runner:
    #         print(t, '--- runner:')
    #         print(t, runner)
    #         print(t, 'bing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #         print(t, i.tag.split('}')[1])
    # counter = 0
    #
    # runner = node
    # c += 1
    # if c == 14:
    #     quit()
    #
    # tag = node.tag.split('}')[1]  # type: str
    # # elems w/ built-in types
    # if 'type' in node.attrib.keys():
    #     if node.attrib['type'].startswith('xs:'):
    #         elems_with_bi_types.append(node)
    #         parent_child[node] = parentX
    #         elems_with_bi_types_parents.append(parent_child)
    #         print(node.attrib)
    #         print('parent: ', node.tag.split('}')[1])
    #         print('parent: ', parentX.attrib['name'])
    #         print(' ')
    #     else:
    #         # elems w/ global types
    #         elems_with_global_types.append(node)
    # # elems simple
    # if tag == 'simpleType':
    #     elems_simple.append(node)
    # # elems w/ base / restriction
    # if 'base' in node.attrib.keys():
    #     elems_with_base.append(node)
    # runner = node
    # parentX = node
    #
    # for i in elems_with_bi_types:
    #     print(ET.tostring(i))
    #
    # for i in elems_with_bi_types_parents:
    #     for x, y in i.items():
    #         x = ET.tostring(x)
    #         y = ET.tostring(y)
    # temp_list = elems_with_bi_types + elems_with_global_types + elems_simple + elems_with_base


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


def main():
    print('--inside main--')
    header_list = ['ID int']
    temp_dictionary = {
        "table": None,
        "column": None,
        "value": None,
        "xmlDataType": None,
        "sqlDataType": None,
    }

    path, dirs, files = next(os.walk(xsds_dir))
    xml_schema = files[0]
    xml_schema_path = os.path.join(path, xml_schema)
    tree = ET.parse(xml_schema_path, parser=None)
    root = tree.getroot()

    v = 0
    for i in tree.iter():
        v += 1
    print('-----------------------------------')
    print(t, 'XSD files (xml schemas):')
    for i in files:
        print(t, t, i)
    print(' ')
    print(t, 'Current file: ', xml_schema)
    print(t, xml_schema_path)
    print(t, tree)
    print(t, 'node count:', v)
    print('-----------------------------------')

    breakpoint()
    clearit()
    time.sleep(.0005)

    all_attrs_w_type = []  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    list_of_all_data_types = []
    elems_with_type = []
    elems_no_type_with_name = []
    elems_no_type_no_name = []
    list_of_built_in_data_types = []
    list_of_global_types = []
    type_count = {}

    # parse through tree and gather elements for later
    for child in tree.iter():
        attr = child.attrib
        type_of_element = child.tag.split('}')[1]

        ################################# THESE ARE ALL TYPES
        if 'type' in attr.keys():

            elems_with_type.append(child)

            attr_name = attr['name']
            attr_type = attr['type']

            # get repeating list of types
            r = attr_type
            all_attrs_w_type.append(attr)
            if r not in list_of_all_data_types:
                list_of_all_data_types.append(r)
            # create UNIQUE list of built in data types & global types
            if r.startswith('xs:'):
                if r not in list_of_built_in_data_types:
                    list_of_built_in_data_types.append(r)
            # create UNIQUE list of global(custom) types
            else:
                list_of_global_types.append(r)
            if r not in type_count.keys():
                type_count[r] = 1
            else:
                type_count[r] += 1

        ################################# THESE ARE ALL TYPES
        if 'type' not in attr.keys():
            if 'name' in attr.keys():

                elems_no_type_with_name.append(child)

                attr_name = attr['name']
                # print(ET.tostring(child))
                # print(child.tag)
                # print(attr)
                # print('TYPE OF ELEMENT: ', type_of_element)
                # print('THIS IS THE ELEMENT NAME: ', attr_name)
                # print('- ')
                # create list of elements that DON'T have type
                if type_of_element not in elems_no_type_with_name:
                    elems_no_type_with_name.append(child.tag)

                # ***********

            # NO type NO name | indicators
            if 'name' not in attr.keys():
                if type_of_element not in indicator_list:
                    indicator_list.append(type_of_element)
                elems_no_type_no_name.append(child)

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
        # else:
        #     print('!!!!!!!!!!!!!!!!!!!!!!!!')
        #     attr = child.attrib
        #     attr_name = attr['name']
        #     type_of_element = child.tag.split('}')[1]
        #     attr_type = attr['type']
        #     print(ET.tostring(child))
        #     print(child.tag)
        #     print(attr)
        #     print('TYPE OF ELEMENT: ', type_of_element)
        #     print('THIS IS THE DATA TYPE: ', attr_type)
        #     print('ATTR NAME NAME: ', attr_name)
        #     print('- ')
        #     ########################### More Logic
        #     # table, column, value, xmlDataType, sqlDataType

    # create_table(header_list, test_table)
    field_list = header_list

    print('\nall elements with type')
    for i in elems_with_type:
        print(i)

    print('\nlist of data types uses in this schema')
    for i in list_of_all_data_types:
        print(i)

    print('\nlist of global data types')
    for i in list_of_global_types:
        print(i)

    breakpoint()
    clearit()
    time.sleep(.005)

    print('\ntype count:')
    for i, j in type_count.items():
        print(i, ' : ', j)

    breakpoint()
    clearit()
    time.sleep(.005)

    print('~ ' * 70)
    print('this function returns this: \n')
    with open('sql_create_table statement.txt', 'w')as f:
        for i in field_list:
            f.write('%s\n' % i)
    for i in header_list:
        print(i)
    print('~ ' * 70)
    return header_list

def data2db(xml_file: str):
    xf = os.path.basename(xml_file)
    pk = get_tid(xf)
    # print(xml_file)
    tree = ET.parse(xml_file, parser=None)
    root = tree.getroot()
    dummy_list = ['name', 'stamp', 'claimNumber', 'recipientsXM8UserId', 'recipientsXNAddress', 'origTransactionId']
    dummy_list =['CONTACT', 'CONTACT', 'CONTROL_POINT', 'CONTROL_POINT', 'PHONE', 'PHONE', 'PHONE', 'TYPEOFLOSS', 'XACTNET_INFO', 'XACTNET_INFO', 'XACTNET_INFO', 'XACTNET_INFO']


    x = dummy_list[5]
    # x = 'XACTNET_INFO'
    headers = ['ID']
    values = []
    for x in dummy_list:
        templist= [pk]
        print('     -----------------> looking for {} <-------------------'.format(x))
        for node in root.iter(x):
            print(node)
            print(node.attrib)
            print(ET.tostring(node))
            for i, j in node.attrib.items():
                print(i,len(i),' : ',j,len(j))
                if i not in headers:
                    headers.append(i)
                templist.append(j)
                values.append(templist)
        print(headers)
        print(values)



    return 'something'


def demo():
    print(')98(((((((((((((((((((((((((')
    path, dirs, files = next(os.walk(status_dir))
    c = 0
    mc = len(files) -1
    for file in files:
        file = os.path.join(path, file)
        print('\n~~~~~~~~~~~~~~~~')
        # print(file)
        data2db(file)
        print('~~~~~~ files remaining: ', mc,'~~~~~~~~')
        mc-=1
        c += 1
    print('TOTAL FILES PROCESSED')
    print(c)


if __name__ == '__main__':
    # main()
    firstpass()
    demo()

    # create_table(these_columns, this_table)
