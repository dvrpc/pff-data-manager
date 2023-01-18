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
from settings import conn_string

errorPrompt = """\
        ERROR: This script requires one arguments:

        1 - source directory of files

        Usage: pports-cargo-importer.py <directory>
        """

# check for necessary arguments before running
if (len(sys.argv) < 2 or  len(sys.argv) > 2):
    print errorPrompt
    sys.exit(1)

#accept arguments from command line
path = sys.argv[1]


# data cell clean-up
def cleanValue( val ):
    clean = val.replace('-','0').replace(',','').split('.')[0]
    return clean

# SQL statement for the two tables
SQL_INSERT_ACTIVITY = """
INSERT INTO pports_act(year, portid, domestic, import, export) 
VALUES (
    %s,%s,%s,%s,%s
)
"""
con = psql.connect(conn_string)
cur = con.cursor()

files = os.listdir( path )

# create archive for cleanup
archive = os.path.join(path,'archive')
if not os.path.exists(archive):
    os.makedirs(archive)

# parse the files
for file in files:
    with open(os.path.join(path,file), 'r') as f:
        data = csv.reader(f, delimiter=",")
        year = os.path.splitext(file)[0][2:]
        print 'Processing '+year+' data'
        for row in data:
            if row:
                portid = row[0]
                domestic = cleanValue(row[5])
                imports = cleanValue(row[7])
                export = cleanValue(row[8])
                cur.execute(SQL_INSERT_ACTIVITY, (year, portid, domestic, imports, export))
        print 'Principal Port activity for '+year+' added to database'
        con.commit()
    # cleanup and archive the data
    shutil.move(os.path.join(path,file), archive)

cur.close()
con.close()