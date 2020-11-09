import os
import sys
import csv
import time
import json
import xml.dom.minidom

import xml.etree.ElementTree as ET

import pandas as pd
from quick_tools import breakout, clearit

this_table = 'test table'
these_columns = [
    'DOB DATETIME',
    'tile VARCHAR(225)',
    'due_data DATE', 'description TEXT'
]

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
note_dir = os.path.join(data_dir, 'note')
estimate_dir = os.path.join(data_dir, 'estimate')
customDoc_dir = os.path.join(data_dir, 'customDoc')

# xsds_dir, data_dict_dir
xsds_dir = os.path.join(project_dir, 'xsds')
data_dict_dir = os.path.join(project_dir, 'data_dicts')
status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')


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


def firstpass():
    print('--inside firstpass--')
    #############################
    #         sample files      #
    #############################
    path, dirs, files = next(os.walk(xsds_dir))

    # status_schema = files[0]
    status_schema = files[0]
    status_schema_path = os.path.join(path, status_schema)
    tree = ET.parse(status_schema_path, parser=None)
    root = tree.getroot()

    c1 = []
    c2 = []
    c3 = []

    elems_with_bi_types = []
    elems_with_global_types = []
    elems_simple = []
    elems_with_base = []
    ##############################################################
    #
    #       how to get all values & attributes / header
    #
    ##############################################################
    for node in tree.iter():
        tag = node.tag
        tag = tag.split('}')[1]  # type: str
        # elems w/ built-in types
        if 'type' in node.attrib.keys():
            if node.attrib['type'].startswith('xs:'):
                elems_with_bi_types.append(node)
                print(node)
                print(ET.tostring(node))
            else:
                # elems w/ global types
                elems_with_global_types.append(node)
        # elems simple
        if tag == 'simpleType':
            elems_simple.append(node)
        # elems w/ base / restriction
        if 'base' in node.attrib.keys():
            elems_with_base.append(node)
    temp_list = elems_with_bi_types + elems_with_global_types + elems_simple + elems_with_base

    # for elem in elems_with_global_types:
    #     global_type = elem.attrib['type']
    #     print('------->', global_type)
    #     for i in tree.iter():
    #         tag_type = i.tag.split('}')[1]
    #         if 'TYPESOFLOSS' in i.attrib.values(): #and 'type' not in i.attrib.values():
    #             if tag_type== 'complexType' or tag_type == 'simpleType':
    #                 print(i.tag.split('}')[1])
    #                 print('number of children: ', len(i))
    #                 print(i.attrib)
    #                 print(ET.tostring(i))
    #                 print(' ')

    # for elem in elems_with_global_types:
    #     global_type= elem.attrib['type']
    #     print('--------------> type: ', elem.attrib['type'])
    #     for node in tree.iter():
    #         tag_type = node.tag.split('}')[1]
    #         if global_type in node.attrib.values():
    #             # if tag_type == 'complexType' or tag_type == 'simpleType':
    #             print(tag_type)
    #             print('number of children: ', len(node))
    #             print(node.attrib)
    #             print(node.tag)
    #             print(ET.tostring(node))
    #             print(' ')


tracking_list = []
d_list = []  # duplicates
def get_tid(file_name):
    tid = file_name
    tid = '.'.join(tid.split('.', 2)[:2])

    if tid not in tracking_list:
        tracking_list.append(tid)
    else:
        print('!!!!!!!!!!!1')
        if tid not in d_list:
            d_list.append(tid)
    return tid              # type: str

def main():
    print('--inside main--')
    #############################
    #         sample files      #
    #############################
    path, dirs, files = next(os.walk(xsds_dir))

    status_schema = files[0]
    status_schema_path = os.path.join(path, status_schema)
    status_schema_tree = ET.parse(status_schema_path, parser=None)
    root = status_schema_tree.getroot()

    print(status_schema_path)
    print(status_schema_tree)
    print(status_schema)
    print('-------------')

    v = 0
    for i in status_schema_tree.iter():
        v += 1
    print(v)

    # generic_rough_draft_schema= files[4]
    # generic_rough_draft_path = os.path.join(path, generic_rough_draft_schema)
    # rough_draft_tree = ET.parse(generic_rough_draft_path, parser=None)
    # status_schema_tree = rough_draft_tree
    # root = rough_draft_tree.getroot()

    # # sample_status = files[5]
    # sample_status_path = os.path.join(path, sample_status)
    # sample_status_tree = ET.parse(sample_status_path, parser=None)
    # root = sample_status_tree.getroot()

    #######################################
    #   manually iterate through entire tree
    #   61 elements in tree - total
    #   7 elements in root - first lever
    #######################################

    # ---------> get list of all types
    list_of_all_data_types = []
    list_of_built_in_data_types = []
    list_of_global_types = []
    type_count = {}

    all_attrs_w_type = []  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    elems_with_type = []
    elems_no_type_with_name = []
    elems_no_type_no_name = []

    c = 0
    print(' ')
    print('elements with built-in data type')
    for child in status_schema_tree.iter():
        attr = child.attrib
        tag_type = child.tag.split('}')[1]
        if 'type' in child.attrib.keys():
            if attr['type'].startswith('xs:'):
                c += 1
                print(ET.tostring(child))

    print(' ')
    print('elements with built global type')
    for child in status_schema_tree.iter():
        attr = child.attrib
        tag_type = child.tag.split('}')[1]
        if 'type' in child.attrib.keys():
            if not attr['type'].startswith('xs:'):
                c += 1
                print(ET.tostring(child))

    print(' ')
    print('elements with base restriction')
    for child in status_schema_tree.iter():
        attr = child.attrib
        tag_type = child.tag.split('}')[1]
        if 'base' in child.attrib.keys():
            print(ET.tostring(child))
            c += 1

    print(' ')
    print('elements that are simpleType')
    for child in status_schema_tree.iter():
        attr = child.attrib
        tag_type = child.tag.split('}')[1]
        if tag_type == 'simpleType':
            print(ET.tostring(child))
            c += 1

    print(c)
    # 61 elements total
    # 23 elements with TYPE
    # 8 elements with built in type
    # 15 global type

    for child in status_schema_tree.iter():
        attr = child.attrib
        type_of_element = child.tag.split('}')[1]

        ################################# THESE ARE ALL TYPES
        if 'type' in attr.keys():

            elems_with_type.append(child)

            attr_name = attr['name']
            attr_type = attr['type']
            # print(ET.tostring(child))
            # print(child.tag)
            # print(attr)
            # print('TYPE OF ELEMENT: ', type_of_element)
            # print('THIS IS THE DATA TYPE: ', attr_type)
            # print('- ')

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
                type_count[r] = 0
            else:
                type_count[r] += 0

            # ***********

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

    header_list = []
    test_table = 'status export'
    temp_dictionary = {
        "table": None,
        "column": None,
        "value": None,
        "xmlDataType": None,
        "sqlDataType": None,

    }
    temp_list = []
    for child in elems_with_type:
        if child.attrib['type'].startswith('xs:'):
            attr = child.attrib
            attr_name = attr['name']
            attr_type = attr['type']
            type_of_element = child.tag.split('}')[1]
            # print(ET.tostring(child))
            # print(child.tag)
            # print(attr)
            # print('TYPE OF ELEMENT: ', type_of_element)
            # print('THIS IS THE DATA TYPE: ', attr_type)
            # print('ATTR NAME NAME: ', attr_name )
            # print('- ')
            #################### LOGIC ###########################3

            # * grab all attr['names']
            # * grab XML datatype & convert to mySQL
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

    create_table(header_list, test_table)

    dummy = []
    # for i in elems_no_type_no_name:
    #     type_of_element = i.tag.split('}')[1]
    #     if type_of_element not in dummy:
    #         print(type)
    #         print(ET.tostring(i))
    #         dummy.append(type_of_element)
    #         print(' ')

    # z, y, x = len(elems_with_type), len(element_no_type_with_name), len(elems_no_type_no_name)
    # print('elems: ', str(x + y + z))


if __name__ == '__main__':
    main()
    firstpass()

    # create_table(these_columns, this_table)
