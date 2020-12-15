#!/usr/bin/python

##################################
#
#   Import script for US Commodity Codes
#   Author: Kristen Scudder, DVRPC
#   Date: April 6, 2020
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

        Usage: hs-comm-code-importer.py <file location>
        """
    sys.exit(1)

#accept arguments from command line
path = sys.argv[1]

# SQL statement for the two tables
SQL_INSERT_CODE = """
INSERT INTO hs_comm_code(hs_group, hs_name) 
VALUES (
    %s,%s
);
"""
con = psql.connect(conn_string)
cur = con.cursor()

with open(path) as f:
    data = csv.reader(islice(f, 1, None))
    for row in data:
        # print row
        hs_group = row[0]
        hs_name = row[1]

        #print hs_group, hs_name
        cur.execute(SQL_INSERT_CODE, (hs_group, hs_name))
    con.commit()
