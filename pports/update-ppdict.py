#!/usr/bin/python

##################################
#
#   Finds updated port dirctionary data based on missing ports. Uses current year arcgis service
#   Author: Michael Ruane, DVRPC
#   Date: June 28, 2019
#
#################################

import os
import sys
import psycopg2 as psql
import requests
from utils.settings import FREIGHTDB_CONN


# SQL statement
SQL_QUERY = """
SELECT pports_act.portid from pports_act
LEFT OUTER JOIN pports_dict on pports_act.portid = pports_dict.portid
WHERE pports_dict.portid is null
"""

SQL_UPDATE = """
UPDATE pports_act
SET portid = %s
WHERE oid = %s
"""
con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()
cur2 = con.cursor()

cur.execute(SQL_QUERY)
data = cur.fetchall()
cur.close()

SQL_ADD_PORTS = """
INSERT INTO pports_dict(portid, lat, lon, port_name)
VALUES (
    %s,%s,%s,%s
)
"""

missing_ids = []

for line in data:
    if not line[0] in missing_ids:
        missing_ids.append(line[0])
print(len(missing_ids))
for port in missing_ids:
    print(port)
    response = requests.get(
        "https://geo.dot.gov/server/rest/services/NTAD/Ports_Major/MapServer/0/query?where=UPPER(PORT)LIKE%27"
        + port
        + "%27&outFields=PORT,PORT_NAME&outSR=4326&f=json"
    )
    portinfo = response.json()
    if portinfo["features"]:
        newport = portinfo["features"][0]["attributes"]["PORT"]
        lon = portinfo["features"][0]["geometry"]["y"]
        lat = portinfo["features"][0]["geometry"]["x"]
        name = portinfo["features"][0]["attributes"]["PORT_NAME"]
        cur2.execute(SQL_ADD_PORTS, (newport, lat, lon, name))
    else:
        print("No match found")

cur2.close()
con.commit()
con.close()
