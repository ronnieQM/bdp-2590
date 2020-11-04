import os
import sys
import csv
import time
import json

import xml.etree.ElementTree as ET

import pandas as pd
from quick_tools import breakout

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


def snips():
    pass
    # manual iter()
    """
    c = 0
    alL_elements = 0
    for child in root:
        attr = child.attrib
        element_name = child.tag.split('}')[1]
        element_list.append(element_name)
        num_child = len(child)

        # create iterators for metadata/validation
        if element_name not in unique_elements.keys():
            unique_elements[element_name] = 1
        else:
            unique_elements[element_name] += 1

        # print('# ' * 15)
        # print('ELEMENT NAME: ', element_name)
        # print(child.tag)
        # print(attr)
        # print('# of children: ', len(child))

        alL_elements += 1
        c += 1
        print('FIRST LEVEL-------------')
        if num_child >= 1:
            print(child)
            print('# of children: ', len(child))
            print('   SECOND LEVEL-------------')
            for child1 in child:
                num_child1 = len(child1)
                print('   -', child1)
                print('    ', '# of children: ', len(child1))
                alL_elements += 1
                if num_child1 >= 1:
                    print('      THIRD LEVEL-------------')
                    for child2 in child1:
                        print('      -', child2)
                        print('       ', '# of children: ', len(child2))
                        num_child2 = len(child2)
                        alL_elements += 1
                        if num_child2 >= 1:
                            print('         FOURTH LEVEL-------------')
                            for child3 in child2:
                                print('         -', child3)
                                print('          ', '# of children: ', len(child3))
                                num_child3 = len(num_child3)
                                alL_elements += 1
                                if num_child3 >= 1:
                                    print('            FIFTH LEVEL-------------')
                                    for child4 in child3:
                                        print('         -', child4)
                                        print('          ', '# of children: ', len(child4))
                                        num_child4 = len(num_child4)
                                        alL_elements += 1
        print(' ')
    print('counted elements: ', alL_elements)

    # print('for loop count result', c)
    print('\nunique elements/counts')
    for i, j in unique_elements.items():
        print(i, ' : ', j)
    """
    # # get repeating list of types
    # for child in status_schema_tree.iter():
    #     if 'type' in attr.keys():
    #         r = attr['type']
    #         if r not in list_of_types:
    #             list_of_types.append(r)
    #         # create UNIQUE list of built in data types & global types
    #         if r.startswith('xs:'):
    #             if r not in built_in_types:
    #                 built_in_types.append(r)
    #         # create UNIQUE list of global(custom) types
    #         else:
    #             global_types.append(r)
    #         if r not in type_count.keys():
    #             type_count[r] = 0
    #         else:
    #             type_count[r] += 0

    # try:
    #     ################################# THESE ARE ALL TYPES
    #     r = attr['type']
    #     attr_name = attr['name']
    #     # print(r)
    #     print('THIS IS THE ELEMENT NAME: ', attr_name)
    #     print("element/tag type: ",child.tag.split('}')[1])
    #
    #     print(ET.tostring(child))
    #     print(' ')
    #     # create list of ATTRIBUTES that have a type
    #     all_attrs_w_type.append(attr)
    #
    #     # get repeating list of types
    #     if r not in list_of_types:
    #         list_of_types.append(r)
    #     # create UNIQUE list of built in data types & global types
    #     if r.startswith('xs:'):
    #         if r not in built_in_types:
    #             built_in_types.append(r)
    #     # create UNIQUE list of global(custom) types
    #     else:
    #         global_types.append(r)
    #     if r not in type_count.keys():
    #         type_count[r] = 1
    #     else:
    #         type_count[r] += 1
    # except Exception as ex:
    #     pass

    # SEE ALL FIELDS
    # print('FIELD WITH BUILT IN DATA TYPES')
    # for i in all_attrs_w_type:
    #     if i['type'].startswith('xs:'):
    #         print(i)
    # print('')
    # print('')
    # print('FIELDS WITH GLOBAL DATA TYPES')
    # for i in all_attrs_w_type:
    #     if i['type'].startswith('xs:'):
    #         pass
    #     else:
    #         print(i)

    # empty_elem = 0
    # for elem in status_schema_tree.iter():
    #     elem_num_child = len(elem)
    #     # if elem_num_child == 0:
    #     #     element_name = elem.tag.split('}')[1]
    #     #     # print('ELEMENT: ', element_name)
    #     #     j = ET.tostring(elem)
    #     #     print(j)
    #     #     empty_elem += 1
    #     if elem_num_child == 1:
    #         j = ET.tostring(elem)
    #         print(elem.attrib)
    #         print(j)
    # print('EMPTY ELEMS: ', empty_elem)


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

    status_schema = files[0]
    # generic_rough_draft_schema= files[4]
    # generic_rough_draft_path = os.path.join(path, generic_rough_draft_schema)
    # rough_draft_tree = ET.parse(generic_rough_draft_path, parser=None)
    # root = rough_draft_tree.getroot()

    # # sample_status = files[5]
    # sample_status_path = os.path.join(path, sample_status)
    # sample_status_tree = ET.parse(sample_status_path, parser=None)
    # root = sample_status_tree.getroot()

    # loop through root
    # if it has a child, keep going
    # keep track of the relationships
    # X has

    #######################################
    #   manually iterate through entire tree
    #   61 elements in tree - total
    #   7 elements in root - first lever
    #######################################



    # ---------> get list of all types
    list_of_all_types = []
    built_in_types = []
    global_types = []
    type_count = {}

    all_attrs_w_type = []  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    element_no_type_with_name = []

    elems_with_type = []
    elems_no_type_with_name = []
    elems_no_type_no_name = []

    for child in status_schema_tree.iter():
        attr = child.attrib
        type_of_element = child.tag.split('}')[1]

        ################################# THESE ARE ALL TYPES
        if 'type' in attr.keys():
            attr_name = attr['name']
            attr_type = attr['type']
            print(ET.tostring(child))
            print(child.tag)
            print(attr)
            print('TYPE OF ELEMENT: ', type_of_element)
            print('THIS IS THE DATA TYPE: ', attr_type)
            print('- ')

            all_attrs_w_type.append(attr)

            # get repeating list of types
            r = attr_name
            if r not in list_of_all_types:
                list_of_all_types.append(r)
            # create UNIQUE list of built in data types & global types
            if r.startswith('xs:'):
                if r not in built_in_types:
                    built_in_types.append(r)
            # create UNIQUE list of global(custom) types
            else:
                global_types.append(r)
            if r not in type_count.keys():
                type_count[r] = 0
            else:
                type_count[r] += 0

            # ***********
            elems_with_type.append(child)

        # this DOESN'T have a TYPE but it DOES have a NAME
        if 'type' not in attr.keys():
            if 'name' in attr.keys():
                attr_name = attr['name']
                print(ET.tostring(child))
                print(child.tag)
                print(attr)
                print('TYPE OF ELEMENT: ', type_of_element)
                print('THIS IS THE ELEMENT NAME: ', attr_name)
                print('- ')
                # create list of elements that DON'T have type
                if type_of_element not in element_no_type_with_name:
                    element_no_type_with_name.append(child.tag)

            # ***********
                elems_no_type_with_name.append(child)

            # NO type NO name | indicators
            if 'name' not in attr.keys():
                if type_of_element not in indicator_list:
                    indicator_list.append(type_of_element)
                elems_no_type_no_name.append(child)

        # INDICATOR ELEMENTS
        # for i in indicator_list:
        #     print(i)
        # ELEMENTS WITH NO TYPE
        for i in elems_no_type_no_name:
            print(i)

    z,y,x = len(elems_with_type),len(element_no_type_with_name),len(elems_no_type_no_name)
    print('elems: ', str(x+y+z))

    # 61 elements in this particular XSD (status)


if __name__ == '__main__':
    main()
