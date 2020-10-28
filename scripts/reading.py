import os
import sys
import csv

import xml.etree.ElementTree as ET

# scripts directory, inside of project directory
curr_path =os.getcwd()
# home this project files
project_path = os.path.dirname(curr_path)
# project_path/data
data_path = os.path.join(project_path, 'data')

path,dirs,files=next(os.walk(data_path))

print(len(files))
print('there are {} xml files in the data dir')