#!/usr/bin/python

##################################
#
#   Import script for USACE Published Commodity Codes
#   Author: Kristen Scudder, DVRPC
#   Date: April 2, 2020
#
#      Arguments
#      [1] =  file location
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

        1 - file location

        Usage: pport-dict-importer.py <file location>
        """
    sys.exit(1)

#accept arguments from command line
path = sys.argv[1]

# SQL statement for the two tables
SQL_INSERT_CODE = """
INSERT INTO pports_dict(portid, lat, lon, port_name, dvrpc_port, msa_id) 
VALUES (
    %s,%s,%s,%s,%s,%s
);
"""
con = psql.connect(conn_string)
cur = con.cursor()

with open(path) as f:
    data = csv.reader(islice(f, 1, None))
    for row in data:
        # print row
        portid = row[1]
        lat = row[2]
        lon = row[3]
        port_name = row[4]
        dvrpc_port = row[5]
        msa_id = row[6]
        #geom = row[7]

        print portid, lat, lon, port_name, dvrpc_port, msa_id
        cur.execute(SQL_INSERT_CODE, (portid, lat, lon, port_name, dvrpc_port, msa_id))
    con.commit()
