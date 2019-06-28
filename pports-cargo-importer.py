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
location = sys.argv[2]

# parse the files
# def parseFiles():




# if sourceType == 'm':
#        print 'Importing Principal Ports data for multiple years...'
#        # loop all files in specified directory
#        for file in os.listdir(location):


# elif sourceType == 's':
#        print 'Importing Principal Ports data for a single year...'

con = psql.connect(conn_string)
cur = con.cursor()

