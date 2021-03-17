# settings.py
from dotenv import load_dotenv
load_dotenv()

import os

from kgbase import Query
q = Query()

q.login(
    username = os.getenv("username"),
    password = os.getenv("password")
)

from pprint import pprint
project_id = q.get_user_projects()[0]['projectId']

project_schema = q.get_schema(project_id)

project_tables = project_schema['tables']

tables = {}

for table_data in project_tables:
    name = table_data['displayName']
    tables[name] = table_data

kt = tables['Knowledge']
tt = tables['Type']
st = tables['Status']
strt = tables['Structure']

kt_id = kt['tableId']
tt_id = tt['tableId']
st_id = st['tableId']
strt_id = strt['tableId']

pprint(q.get_graph(project_id, strt_id))

values={
    'col-0': 'Test',
    'col-2': 'https://gitlab.com/cuppajoeman/...',
    'col-7': True
}

#("column8", "row-M587jZETRpuCBIXUfw6"),
edges = [
        # Property - do this dynamically next time
        ("Type", "row-MVrlg2B1NM57XhEZeZm"),
        ("Status", "row-MVrlg2B1NM57XhEZeZm")
]

#result = q.create_vertex(
#    project_id,
#    kt_id,
#    values,
#    edges
#)
#
#print(result)

# Title = 
# Type = 
# Content = 
# Status =  
# Parent = 
# Knowledge_Used = 
# Formatted = 
# 

# col-0 Title
# col-8 Type
# col-2 Content
# col-3 Status
# col-4 Parent
# col-6 Knowledge Used
# col-7 Formatted

 # OUTPUT OF TYPE TABLE
 #'vertices': [{'contextId': None,
 #              'id': 'row-MVXSSn_vJuk_qhboEni',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Theorem'}]},
 #             {'contextId': None,
 #              'id': 'row-MVXSSn_vJuk_qhboEnj',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Definition'}]},
 #             {'contextId': None,
 #              'id': 'row-MVc4yXdAM-raLkjVgZp',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Device'}]},
 #             {'contextId': None,
 #              'id': 'row-MVc51vyjRNGEHuiVDQ6',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Machine'}]},
 #             {'contextId': None,
 #              'id': 'row-MVoAVO12AKScs-d2ECR',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Proposition'}]},
 #             {'contextId': None,
 #              'id': 'row-MVrlg2B1NM57XhEZeZm',
 #              'label': 'tab-MVXSHAoNLpA0Cc-atfi',
 #              'values': [{'key': 'col-0', 'value': 'Property'}]}]}

# OUTPUT OF STATUS TABLE
#{'edges': [],
# 'total': 2,
# 'vertexIds': ['row-MVXhdD9Mbtt901kMYRX', 'row-MVXhee-z7QrOpFkA0FX'],
# 'vertices': [{'contextId': None,
#               'id': 'row-MVXhdD9Mbtt901kMYRX',
#               'label': 'tab-MVXh1EVi97AWenYKjUp',
#               'values': [{'key': 'col-0', 'value': 'Complete'}]},
#              {'contextId': None,
#               'id': 'row-MVXhee-z7QrOpFkA0FX',
#               'label': 'tab-MVXh1EVi97AWenYKjUp',
#               'values': [{'key': 'col-0', 'value': 'Work In Progress'}]}]}


#pprint(q.get_graph(project_id, tables['Type']['tableId']))
#pprint(q.get_graph(project_id, kt_id))
