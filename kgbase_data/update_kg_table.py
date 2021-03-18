# settings.py
from dotenv import load_dotenv
load_dotenv()

# to print table
import yaml

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

# The first layer is a directory of the tables, the second layer shows the rows of the table and their associated ids
tables = {}

for table_data in project_tables:
    table_name = table_data['displayName']
    table_id = table_data['tableId'] 

    # Instantiate table to empty dictionary
    tables[table_name] = {}

    vertices = q.get_graph(project_id, table_id, limit=99999)['vertices']
    #pprint.pprint(vertices)
    # Generate the table 
    for row in vertices:
        # This code will break when we have two vertices with the same name
        for row_entry in row['values']:
            # We are looking at it's title
            if row_entry['key'] == 'col-0':
                title = row_entry['value']
                tables[table_name][title] = row['id']
                # Exits inner loop, outer continues
                break

#pprint.pprint(tables)
# Also write it to a file, because why not, relative to proj root
with open("kgbase_data/tables.txt", "w") as f:
    s = pprint.pformat(tables)
    s =  yaml.dump(tables, default_flow_style=False, indent=4)
    f.write(s)

