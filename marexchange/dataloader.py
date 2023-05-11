import requests
import psycopg2 as psql
import os
import csv

from utils.settings import FREIGHTDB_CONN

con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()

# Loop through the files in the directory and insert them into the table
directory = 'G:/Shared drives/Freight Planning/Technical Studies/_FreightData/maritime_exchange'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    cur.execute(f'INSERT INTO marex_delriver_shipcalls (filename, content) VALUES ({row["arrival"].strip()},{row["vessel"].strip()},{row["rig"].strip()},{row["flag"].strip()},{row["commonname"].strip()},{row["location_id"].strip()},{row["state"].strip()},{row["cargo_typ"].strip()},{row["cargo"].strip()},{row["dir"].strip()}')
                except:
                    cur.rollback()
con.commit()