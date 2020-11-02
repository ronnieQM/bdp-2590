import os
import sys
import csv

import xml.etree.ElementTree as ET

import pandas as pd

# change current directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
################################
######### directories  & paths
################################
# scripts directory, inside of project directory
curr_dir = os.getcwd()
# home, this project's files
project_dir = os.path.dirname(curr_dir)
# project_path/data
data_dir = os.path.join(project_dir, 'data')
status_dir = os.path.join(data_dir, 'status')
xsds_dir = os.path.join(project_dir, 'xsds')
status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')

################################
######## metadata
################################
path, dirs, files = next(os.walk(status_dir))
print('#' * 40)
print("""
        there are {} xml files in the data/status dir

        this project directory: {} 
        this python script's directory: {}"""
      .format(len(files), project_dir, os.getcwd()))
print('#' * 40)

standard_carrier_data_dic = '/home/rqm/main/dev/ace/bdp-2590/xact_minus/XactAnalysis Export Documentation/Estimate Export/StandardCarrier data dictionary.xlsx'


def read_xmls():
    pass


def read_xsds(xsd_file):
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


def something(xml_file):
    x = xml_file

    status_dir = os.path.join(data_dir, 'status')
    path, dirs, file = next(os.walk(status_dir))
    print(file[0])

    # get every possible data type from the documentation
    # get every row in the csv

    list_of_data_dict = []
    with open('test.csv')as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        pair = {}
        for row in csv_reader:
            if line_count == 0:
                print('Column names are {}.'.format(', '.join(row)))
                line_count += 1
            else:
                # print(row[0])
                # print(row[1])
                pair[row[0]] = row[1]
                list_of_data_dict.append(pair)

        print('row count: {}'.format(line_count))

        for x in list_of_data_dict:
            for i, j in x.items():
                print(i, ' : ', j)


def main():
    # read file
    read_file = pd.read_excel(standard_carrier_data_dic)
    read_file.to_csv('test.csv', index=None, header=True)
    print('shit!')

    something('asdf ')


if __name__ == '__main__':
    main()
