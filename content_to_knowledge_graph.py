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

table_to_id = {
        'Structure':  'tab-MVVF6vQI4G2jDqgcLJM',
        'Knowledge': 'tab-MVVDy_ojQuAFVL6HAK1'
        }

# The first layer is a directory of the tables, the second layer shows the rows of the table and their associated ids
tables = {}

# Update text representations of kg

cols = ["Type", "Status", "Parent", "Knowledge_Used"]


# A vertex represents a row, they are the same thing

for table_data in project_tables:
    table_name = table_data['displayName']
    table_id = table_data['tableId'] 

    # Instantiate table to empty dictionary
    tables[table_name] = {}

    #pprint.pprint(q.get_graph(project_id, table_id))
    vertices = q.get_graph(project_id, table_id, limit=9999999)['vertices']
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

# Also write it to a file, because why not
with open("kgbase_data/tables.txt", "w") as f:
    s = pprint.pformat(tables)
    f.write(s)

# Create a new node - in the Knowledge table

# Read lines from file

argfile = open("kgbase_data/arguments.txt")

# TODO: Dynamically construct this
args = [ "Title", "Type", "Content", "Status", "Parent", "Knowledge Used", "Formatted"]

argument_to_column= {
     "Title": "col-0" ,
     "Type": "col-8" ,
     "Content": "col-2" ,
     "Status": "col-3" ,
     "Parent": "col-4" ,
     "Knowledge Used": "col-6",
     "Formatted": "col-7"
 }

argument_is_relationship = {
     "Title": False, # string
     "Type": True, # enum
     "Content": False, # url
     "Status": True, # enum
     "Parent": True, # Points to a structure
     "Knowledge Used": True, # Points to many knowledge
     "Formatted": False, # url
 }

relationship_arg_to_table_name = {
    "Type": "Type",
    "Status": "Status",
    "Parent": "Structure",
    "Knowledge Used": "Knowledge"
}

values = {}
edges = []

for i, line in enumerate(argfile):
    rhs_of_equality = line.split("=")[1].strip()
    arg_values = [x.strip() for x in rhs_of_equality.split(",")]
    arg_name = args[i]
    if argument_is_relationship[arg_name]:
        # Create the edges
        if arg_values != ['']:
            for v in arg_values:
                # Assuming one to one relations between title and id
                table_name = relationship_arg_to_table_name[arg_name]
                edge_id = tables[table_name][v]
                edges.append((arg_name, edge_id))
    else:
        # When it's not an edge, then there is only one value for it.
        if arg_name != "Formatted":
            values[argument_to_column[arg_name]] = arg_values[0]
        else:
            values[argument_to_column[arg_name]] = False if arg_values[0] == "False" else True

pprint.pprint(values)
pprint.pprint(edges)

while "the answer is invalid":
    reply = str(input("Are you ok with pushing this to the kg?"+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        result = q.create_vertex(
            project_id,
            table_to_id['Knowledge'],
            values,
            edges
        )
        print("Responce: ")
        pprint.pprint(result)
        # LEAVE THIS HERE!!!!
        break
    if reply[0] == 'n':
        break
