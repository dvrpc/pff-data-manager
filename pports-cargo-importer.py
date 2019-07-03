#!/usr/bin/python

##################################
#
#   Import script for USACE individual principal ports data (cargo+trips)
#   Author: Michael Ruane, DVRPC
#   Date: June 28, 2019
#
#      Arguments
#      [1] = type of import
#             m = multi-year
#             s = single year
#      [2] = windows directory location
#
#################################

import os
import sys
import psycopg2 as psql
import csv
from settings import conn_string
from itertools import islice

# check for necessary arguments before running
if (len(sys.argv) < 3 or  len(sys.argv) > 3):
    print """\
        ERROR: This script requires two arguments:

        1 - type of import (m = multiple years or s = single year)
        2 - source directory of files

        Usage: pports-cargo-importer.py <type> <directory>
        """
    sys.exit(1)

#accept arguments from command line
sourceType = sys.argv[1]
path = sys.argv[2]

# SQL statement for the two tables
SQL_INSERT_CARGO = """
INSERT INTO pports_cargo(portid, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment) 
VALUES (
    %s,%s,%s,%s,%s,%s,%s,%s
);
"""
SQL_INSERT_TRIPS= """
INSERT INTO pports_trips(portid, year, receipt_trip, shipment_trip, traffic_type) 
VALUES (
    %s,%s,%s,%s,%s
);
"""
con = psql.connect(conn_string)
cur = con.cursor()



# parse the files
def parseAnnualData(annual_dir, year):
    for root, dirs, files in os.walk( annual_dir ):
        for file in files:
            dataType = os.path.basename(os.path.normpath( root ))
            print (dataType)
            print (d)
            # port = os.path.basename(os.path.normpath( root ))
            # year = os.path.basename(os.path.normpath( root ))
            port = os.path.basename(os.path.splitext(file)[0][:5])
            if dataType == 'cargo':
                with open(root +'/' + file, 'r') as f:
                    data = csv.reader(islice(f, 3, None))
                    for row in data:
                        print row
                        pub_group = row[0]
                        dom_intraport = row[7]
                        dom_receipt = row[8]
                        dom_shipment = row[9]
                        for_receipt = row[12]
                        for_shipment = row[13]
                        print port, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment
                        # cur.execute(SQL_INSERT_CARGO, (port, year, pub_group, dom_intraport, dom_receipt, dom_shipment, for_receipt, for_shipment))
                    # con.commit()
            elif dataType == 'trips':
                with open(root +'/' + file, 'r') as f:
                    data = csv.reader(islice(f, 2, None))
                    for row in data:
                        for i in range(5,6) + range(8,9) + range(11,12) + range(14,15) + range(17,18):
                            fieldNames = {
                                5 : '01',
                                8 : '02',
                                11 : '03',
                                14 : '04',
                                17 : '05'                             
                            }
                            receipt_trip = row[i]
                            shipment_trip = row[i+1]
                            traffic_type = fieldNames[i]
                            print port, year, receipt_trip, shipment_trip, traffic_type
                            # cur.execute(SQL_INSERT_TRIPS, (port, year, receipt_trip, shipment_trip, traffic_type))
                    # con.commit()

    return

# check type of request and execute data parsing
if sourceType == 'm':
    # loop all multiple year directories 
    dirs = os.listdir( path )
    print(dirs)
    for d in dirs:
        parseAnnualData(os.path.join(path, d), d)           
elif sourceType == 's':
    d = os.path.basename(os.path.normpath( path ))
    print (d)
    parseAnnualData(path, d)
else:
    print """\
        ERROR: This script requires two arguments:

        1 - type of import (m = multiple years or s = single year)
        2 - source directory of files

        Usage: pports-cargo-importer.py <type> <directory>
        """
    sys.exit(1)
