import mysql.connector
import sys
import os

os.chdir((os.path.dirname(os.path.abspath(__file__))))  # change dir to dir where python scripts reside # project/scripts
sys.path.insert(1,os.path.dirname(os.getcwd()))

from solutions.sql_formatter import field_formatter, generate_create_query, values_formatter, generate_insert_query



mydb = mysql.connector.connect(
    host="localhost",
    user="root2",
    password="root",
    # database="scratch_db",
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

type_dictionary = {
    "name": " VARCHAR(25)",
    "age": " INT",
    "phone": ' VARCHAR(45)',
}


dummy_fields = ['name', 'age', 'phone', 'email']

arow = ['robert', '39', '5144076571', 'juan@gmail.com']
brows =[
    ['mark', '21', '232-343-1236', ' '],
    ['eric', '51', '839-446-1786', 'eric@gmail.com'],
    ['mark', '21', '232-343-1236', 'mark@gmail.com']
]
dummy_table = 'scratch_db.clients'
# ------------------------------------------------ insert values into table -----------------------------------------------
x = values_formatter(brows)
c = generate_insert_query(dummy_table, x)
print(c)

cursor.execute(c)
mydb.commit()

query = r"""
SELECT *
FROM scratch_db.clients
"""
cursor.execute(query)
print('select * from scratch_db.clients')
for i in cursor:
    print(i)

quit()
# ------------------------------------------------ create table -----------------------------------------------

dummy_table= 'scratch_db.clients'
# print('example fields list: ', dummy_fields)
formatted_fields= field_formatter(dummy_fields)
# print('formatted fields: ', formatted_fields)
return_query = generate_create_query(dummy_table, formatted_fields)
# print('return query: ', return_query)

cursor.execute(return_query)

print('after')
cursor.execute('show tables from scratch_db')
for i in cursor:
    print(i)
