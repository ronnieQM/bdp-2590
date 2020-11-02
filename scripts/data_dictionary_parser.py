import os
import sys
import csv

import xml.etree.ElementTree as ET

import pandas as pd

################################
######### directories  & paths
################################

# change current directory to script directory
curr_dir = os.getcwd()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# home, this project's files
project_dir = os.path.dirname(curr_dir)
# scripts directory, inside of project directory
# DATA directories
data_dir = os.path.join(project_dir, 'data')
status_dir = os.path.join(data_dir, 'status')
xsds_dir = os.path.join(project_dir, 'xsds')

# XSD files
status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')


class StatusDataDictClass:
    """This is a representations of the StatusExportDataDict.xlsx file"""

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


class Status:
    """This is a instance of the any give STATUS xml file"""

    def __init__(self, contact_name, contact_type, control_point_stamp, control_point_type, phone_extension,
                 phone_number, phone_type, typeofloss_claimnumber,
                 xactnet_info_recipientsxnaddress, xactnet_info_recipientsxm8userid, xactnet_info_transactionid,
                 xactnet_info_origtransactionid):
        self.CONTACT_name = contact_name
        self.CONTACT_type = contact_type
        self.CONTROL_POINT_stamp = control_point_stamp
        self.CONTROL_POINT_type = control_point_type
        self.PHONE_extension = phone_extension
        self.PHONE_number = phone_number
        self.PHONE_type = phone_type
        self.TYPEOFLOSS_claimNumber = typeofloss_claimnumber
        self.XACTNET_INFO_recipientsXNAddress = xactnet_info_recipientsxnaddress
        self.XACTNET_INFO_recipientsXM8UserId = xactnet_info_recipientsxm8userid
        self.XACTNET_INFO_transactionId = xactnet_info_transactionid
        self.XACTNET_INFO_origTransactionId = xactnet_info_origtransactionid

    def __str__(self):
        return """
        CONTACT_name: {}
        """.format('asdf')


def read_xml(xsd_file):
    xsd_file = xsd_file
    status_tree = ET.parse(xsd_file, parser=None)
    print("""
        status tree path: {}
        print status tree: {},
        status tree type: {},"""
          .format(xsd_file, status_tree, type(status_tree)))

    root = status_tree.getroot()
    print("""
        root: {}
        type: {}
        root.tag: {}
        root.attribute: {}
    """.format(root, type(root), root.tag, root.attrib))
    print('iterating through root:')
    for i in root:
        print(i.tag, i.attrib)

    print('iterating through entire tree:')
    all_elements = [elem.tag for elem in root.iter()]
    for i in all_elements:
        print(type(i))
        print(i)


def metadata():
    print('#' * 40)
    print("""metadata
            there are {} xml files in the data/status dir

            this project directory: {} 
            this python script's directory: {}
    /metadata"""
          .format(len(files), project_dir, os.getcwd()))
    print('#' * 40)
    

def printing_class_init():
    print('.')
    # for i in list_of_data_dict:
    #     a = 'self.'
    #     x = i.element
    #     y = i.attribute
    #     j = a + x + '_' + y
    #     name = x + '_' + y
    #     name = name.lower()
    #     final = j + '=' + name
    #     print(final)

    # a = '(self, '
    # for i in list_of_data_dict:
    #     name = i.element + '_' + i.attribute
    #     name = name.lower()
    #     a += name
    #     a += ', '
    #     print(a)


def main():
    # read file
    standard_carrier_data_dic = '/home/rqm/main/dev/ace/bdp-2590/xact-edi/XactAnalysis Export Documentation/Estimate ' \
                                'Export/StandardCarrier data dictionary.xlsx '
    status_data_dict = '/home/rqm/main/dev/ace/bdp-2590/xact-edi/XactAnalysis Export Documentation/Status ' \
                       'Export/StandardStatusExportDataDictionary.xlsx'
    read_file = pd.read_excel(status_data_dict)
    read_file.to_csv('standard_status_data_dict.csv', index=None, header=True)

    # all example XML files in 'file'
    path, dirs, files = next(os.walk(status_dir))

    # get every possible data type from the documentation
    # get every row in the csv
    list_of_data_dict = []
    with open('standard_status_data_dict.csv')as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        pair = {}
        for row in csv_reader:
            if line_count == 0:
                print('Column names are {}'.format('| '.join(row)))
                line_count += 1
            else:
                x, y, z, a = row[0], row[1], row[2], row[3]

                temp = StatusDataDictClass(x, y, z, a)
                list_of_data_dict.append(temp)

    print(len(list_of_data_dict))
    test_file = files[5]
    z = os.path.join(path, test_file)
    test_file_tree = ET.parse(z, parser=None)
    root = test_file_tree.getroot()

    print('~ ' * 50)
    print('fuckin around with parsing an example XML:')
    print("""
test file path/name:            {}
test file root:                 {}
test file, # of child nodes:    {}
    """
          .format(z, root, 'tbd'))
    print('~ ' * 50)


if __name__ == '__main__':
    main()
