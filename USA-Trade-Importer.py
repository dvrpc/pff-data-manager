#!/usr/bin/python

##################################
#
#   Import script for USA Trade port commodity data
#   Author: Kristen Scudder, DVRPC
#   Date: April 3, 2020
#
#      Arguments
#      [1] =  windows directory location (cargo or trips folder)
#
#################################

import os
import sys
import psycopg2 as psql
import csv
from settings import conn_string
from itertools import islice

# check for necessary arguments before running
if (len(sys.argv) < 2 or  len(sys.argv) > 2):
    print """\
        ERROR: This script requires one argument:

        1 - file path for USA trade csv file

        Usage: USA-Trade-importer.py <file path>
        """
    sys.exit(1)

#accept arguments from command line
path = sys.argv[1]

# SQL statement for the two tables
SQL_INSERT_CARGO = """
INSERT INTO usa_trade_comm(portid, year, comm_code, import_kg, import_value, export_kg, export_value) 
VALUES (
    %s,%s,%s,%s,%s,%s,%s
);
"""
con = psql.connect(conn_string)
cur = con.cursor()



# parse the files
def parseAnnualData(annual_dir):
    for root, dirs, files in os.walk( annual_dir ):
        print(root)
        for file in files:
            with open(root +'/' + file, 'r') as f:
                data = csv.reader(islice(f, 1, None))
                for row in data:
                    #print row
                    portid = row[7]
                    year = row[2]
                    comm_code = row[1]
                    import_kg = row[4]
                    import_value = [3]
                    export_kg = [5]
                    export_value = [6]
                    print portid, year, comm_code, import_kg, import_value, export_kg, export_value
                    # cur.execute(SQL_INSERT_CARGO, (portid, year, comm_code, import_kg, import_value, export_kg, export_value))
                con.commit()
    return

#import file
parseAnnualData(path)           
