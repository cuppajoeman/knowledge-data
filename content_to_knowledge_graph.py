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
import pprint
project_id = q.get_user_projects()[0]['projectId']

project_schema = q.get_schema(project_id)

project_tables = project_schema['tables']

tables = {}

# Update text representations of kg

for table_data in project_tables:
    name = table_data['displayName']
    with open("kgbase_data/" + name + ".txt", 'w') as f:
        f.write("Table Name: " + name + ", ID: " + table_data['tableId'] + '\n')
        s = pprint.pformat(q.get_graph(project_id, table_data['tableId']))
        f.write(s)

# Create a new node

table_to_id = {
        'Structure':  'tab-MVVF6vQI4G2jDqgcLJM',
        'Knowledge': 'tab-MVVDy_ojQuAFVL6HAK1'
        }

values = {
    'col-0': 'Test',
    'col-2': 'https://gitlab.com/cuppajoeman/...',
    'col-7': True
}

edges = [
        # Property - do this dynamically next time
        ("Type", "row-MVrlg2B1NM57XhEZeZm"),
        ("Status", "row-MVXhdD9Mbtt901kMYRX"),
        ("Parent", "row-MVVGSO2GHfyB6ZfxkhD")
]

result = q.create_vertex(
    project_id,
    table_to_id['Knowledge'],
    values,
    edges
)


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

