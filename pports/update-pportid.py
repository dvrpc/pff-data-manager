#!/usr/bin/python

##################################
#
#   Update WCSC data to correct for 4 character port ids missing leading zero
#   Author: Michael Ruane, DVRPC
#   Date: June 28, 2019
#
#################################

import os
import sys
import psycopg2 as psql
from utils.settings import FREIGHTDB_CONN


# SQL statement
SQL_QUERY = """
SELECT oid, portid FROM pports_act
WHERE length(portid)<5 
"""
SQL_UPDATE = """
UPDATE pports_act
SET portid = %s
WHERE oid = %s
"""
con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()

cur.execute(SQL_QUERY)
data = cur.fetchall()

for line in data:
    oid = line[0]
    prefix = line[1][:1]
    code = line[1][1:]
    fullid = prefix + "0" + code
    cur.execute(SQL_UPDATE, (fullid, oid))

cur.close()
con.commit()
con.close()