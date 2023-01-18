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
INSERT STATEMENT
"""
SQL_INSERT_TRIPS= """
INSERT STATEMENT
"""

# parse the files
def parseAnnualData(annual_dir, year):
    for root, dirs, files in os.walk( annual_dir ):
        for file in files:
            dataType = os.path.basename(os.path.normpath( root ))
            
            ## DO SOMETHING WITH THE DATA
            #  file -> csv      [os.path.join(root, file)  <---  access the file with full path] 
            #  dataType -> cargo or trips (pulled from the directory name)
    return

# check type of request and execute data parsing
if sourceType == 'm':
    # loop all multiple year directories 
    dirs = os.listdir( path )
    for d in dirs:
        parseAnnualData(os.path.join(path, d), d)           
elif sourceType == 's':
    d = os.path.basename(os.path.normpath( path ))
    parseAnnualData(path, d)
else:
    print """\
        ERROR: This script requires two arguments:

        1 - type of import (m = multiple years or s = single year)
        2 - source directory of files

        Usage: pports-cargo-importer.py <type> <directory>
        """
    sys.exit(1)

