import boto3

# variables
database ='energy'
region = 'us-east-1'
raw_table='raw_residential_load_data_e_plus_output'

# initial load
print ('INITIAL LOAD...')
glue = boto3.client(service_name='glue', region_name=region)
tables = glue.get_tables(DatabaseName=database)
deprecated_tables = []
# Iterate through all pages
print ('ITERATING THROUGH PAGES. THIS MIGHT TAKE A WHILE..')
while True:
    table_list = tables['TableList']
    for table in table_list:
        if table['Name'] == raw_table:
            print ("NOT DELETING --- " + table['Name'])
        else:
            deprecated_tables.append(table['Name'])
    print ('DELETENG TABLES:')
    print (deprecated_tables)
    glue.batch_delete_table(DatabaseName=database, TablesToDelete=deprecated_tables)
    print ('DELETE_COMPLETE')
    if 'NextToken' not in tables:
        break
    else:
        tables = glue.get_tables(DatabaseName=database, NextToken=tables['NextToken'])
        deprecated_tables = []
