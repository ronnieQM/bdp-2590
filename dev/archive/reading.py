import os
import sys
import csv

import xml.etree.ElementTree as ET

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




def main():
    print('inside of main')
    read_xsds(status_xsd)

    count = 1
    for i in files:
        x = os.path.join(status_dir, i)
        read_xsd(x)
        count += 1


if __name__ == '__main__':
    main()
