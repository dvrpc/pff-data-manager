import os
import psycopg2 as psql
import pandas as pd
import requests
from shapely.geometry import shape
from datetime import datetime
from utils.settings import FREIGHTDB_CONN, CENSUS_API_KEY

con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()

def load_msas():
    try:
        #gets the number of records in the MSA layer
        url = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/21/query?where=1%3D1&returnCountOnly=true&f=json"
        total_records = requests.get(url).json()["count"]
        result_offset = 0
        max_results = 10
        
        #gets and iterates through the features from the REST service
        while(result_offset < total_records):
            url = f"https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/21/query?where=1%3D1&outFields=BASENAME,NAME,GEOID&resultOffset={str(result_offset)}&resultRecordCount={str(max_results)}&returnGeometry=true&returnIdsOnly=false&outSR=4326&f=geojson"
            features = requests.get(url).json()["features"]
            for f in features:
                try:
                    row = f["properties"]
                    basename = row['BASENAME'].replace("'","")
                    name = row["NAME"].replace("'","")
                    wkt = shape(f["geometry"]).wkt
                    cur.execute(f"INSERT INTO census.msas(basename, name, geoid, geom) VALUES ('{basename}', '{name}', '{row['GEOID']}', '{wkt}')")
                    print("inserted", name)
                except Exception as e:
                    print("Failed to insert row")
                    print(e)
            result_offset = result_offset + max_results
        con.commit()
    except Exception as e:
        print("Failed to load MSAs")
        print(e)