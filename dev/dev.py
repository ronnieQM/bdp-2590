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



def main():
    read_xsds()


if __name__ == "__main__":
    logging.basicConfig()
    logging.root.setLevel(logging.DEBUG)
    main()
