#!/usr/bin/python

##################################
#
#   Import script for Waterborne Commerce Activity for Principal Ports
#   Author: Michael Ruane, DVRPC
#   Date: June 28, 2019
#
#      Arguments
#      [1] = windows directory location
#
#       table - pports_act
#
#################################

import os
import sys
import psycopg2 as psql
import csv
import shutil
from utils.settings import FREIGHTDB_CONN

errorPrompt = """\
        ERROR: This script requires one arguments:

        1 - source file

        Usage: pports-dict-importer.py <source data>
        """

# check for necessary arguments before running
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(errorPrompt)
    sys.exit(1)

# accept arguments from command line
file = sys.argv[1]

# SQL statement for the two tables
SQL_INSERT_PORTS = """
INSERT INTO pports_dict(portid, lat, lon, port_name) 
VALUES (
    %s,%s,%s,%s
)
"""
con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()


# parse the files
with open(file, "r") as f:
    data = csv.reader(f, delimiter=",")
    next(data)  # skip header
    for row in data:
        if row:
            portid = row[1]
            lat = row[2]
            lon = row[3]
            port_name = row[4]
            # print portid, lat, lon, port_name
            cur.execute(SQL_INSERT_PORTS, (portid, lat, lon, port_name))
    con.commit()

cur.close()
con.close()
