#!/usr/bin/python

##################################
#
#   Import script for USACE individual principal ports data (cargo+trips)
#   Author: Kristen Scudder, DVRPC
#   Date: April 1, 2020
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

        1 - source directory of files (cargo or trip folder)

        Usage: pports-cargo-importer.py <directory>
        """
    sys.exit(1)

#accept arguments from command line
path = sys.argv[1]

# SQL statement for the two tables
SQL_INSERT_CARGO = """
INSERT INTO pports_cargo(portid, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment) 
VALUES (
    %s,%s,%s,%s,%s,%s,%s,%s
);
"""
con = psql.connect(conn_string)
cur = con.cursor()



# parse the files
def parseAnnualData(annual_dir):
    for root, dirs, files in os.walk( annual_dir ):
        print(root)
        for file in files:
            filename = os.path.basename(os.path.splitext(file)[0])
            filename_split = filename.split('.')
            year = filename_split[1]
            #print("year =" + year)
            port = filename_split[2]
            #print("port =" + port)
            with open(root +'/' + file, 'r') as f:
                data = csv.reader(islice(f, 1, None))
                for row in data:
                    #print row
                    pub_group = row[0]
                    dom_intraport = row[1]
                    dom_receipt = row[2]
                    dom_shipment = row[3]
                    for_receipt = row[4]
                    for_shipment = row[5]
                    print port, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment
                    # cur.execute(SQL_INSERT_CARGO, (port, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment))
                con.commit()
    return

# loop through all files in directory
#d = os.path.basename(os.path.normpath( path ))
parseAnnualData(path)           



    # sys.exit(1)
