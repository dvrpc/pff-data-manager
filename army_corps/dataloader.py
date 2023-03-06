import os
import psycopg2 as psql
import openpyxl
import pandas as pd
import requests
from datetime import datetime
from utils.settings import FREIGHTDB_CONN, CENSUS_API_KEY

con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()

def load_tonnage(dir, overwrite=False):
    try:
        files = os.listdir(dir)
    except FileNotFoundError:
        print("directory", dir, "was not found")
    else:
        for file in files:
            if file.endswith(".xlsx"):
                try:
                    sheetName = getPortSheetName(os.path.join(dir, file))
                    year = getYear(os.path.join(dir, file), sheetName)
                except:
                    print("Could not determine year for", file, "in", dir)
                else:
                    if not yearExists(year) or overwrite:
                        print("Loading Tonnage for", year)
                        try:
                            ports = pd.read_excel(os.path.join(dir, file), sheet_name=sheetName, header=4)
                            for row in ports.itertuples(name=None):
                                cur.execute("""
                                INSERT INTO army_corps.port_tonnage(port_name, year, total_tons, domestic_tons, foreign_tons, import_tons, export_tons)
                                VALUES ('{port_name}', {year}, {total}, {domestic}, {foreign}, {import_tonnage}, {export})
                                """.format(port_name=row[2].replace("'",""), year=year, total=row[3], domestic=row[4], foreign=row[5], import_tonnage=row[6], export=row[7]))
                        except:
                            print("Failed to load data for", year, "from", os.path.join(dir, file))
                    else:
                        print("Tonnage for", year, "already exists")
            else:
                continue
        con.commit()

def load_principal_ports():
    try:
        layerUrl = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/ndc/FeatureServer/1?f=json"
        lastEditDate = requests.get(layerUrl).json()["editingInfo"]["lastEditDate"]
        year = datetime.fromtimestamp(float(lastEditDate)/1000).year
        print("Loading principal ports")
        url = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/ndc/FeatureServer/1/query?where=1%3D1&outFields=PORT_NAME,PORT,TYPE&returnGeometry=false&outSR=4326&f=json"
        features = requests.get(url).json()["features"]
        for f in features:
            try:
                row = f["attributes"]
                cur.execute("INSERT INTO army_corps.principal_ports(port_code, port_name, port_type, year) VALUES ('{port_code}', '{port_name}', '{port_type}', {year})".format(port_code=str(row["PORT"]).zfill(4), port_name=row["PORT_NAME"].replace("'",""), port_type=row["TYPE"], year=year))
            except Exception as e:
                print("Failed to insert", row)
                print(e)
        con.commit()
    except:
        print("Failed to load principal ports")

def load_dvrpc_port_names(path):
    ports = pd.read_csv(path)
    print("Loading dvrpc port names")
    for row in ports.itertuples(name=None):
        cur.execute("""
        INSERT INTO army_corps.dvrpc_port_names(port_name, dvrpc)
        VALUES ('{port_name}', '{dvrpc}')
        """.format(port_name=row[1], dvrpc=row[2]))
    con.commit()

def load_port_dict(path):
    ports = pd.read_csv(path)
    for row in ports.itertuples(name=None):
        cur.execute("""
        INSERT INTO army_corps.port_dict(port_code, port_name, lat, lon, dvrpc, geoid)
        VALUES ('{port_code}', '{port_name}', {lon}, {lat}, '{dvrpc}', {geoid})
        """.format(port_code=row[2], port_name=row[5], lon=row[3], lat=row[4], dvrpc=row[6], geoid=row[7]))

def getPortSheetName(path):
    possibleNames = ["Ports_by_Name", "Port_Name"]
    xlsx = openpyxl.load_workbook(path)
    sheets = xlsx.sheetnames
    for name in possibleNames:
        if name in sheets:
            return name
    raise Exception("getPortSheetName was unable to determine the proper sheet name for the workbook {wb}".format(wb=path))

def getYear(path, sheetName):
    try:
        sheet = openpyxl.load_workbook(path)[sheetName]
        year = sheet["B2"].value
        year = year[year.index("in") + 3:]
        return year
    except:
        raise Exception("Error in getYear()")

def yearExists(year):
    cur.execute("SELECT EXISTS(SELECT 1 FROM army_corps.port_tonnage WHERE year = %s)", (year,))
    val = cur.fetchone()
    if val[0] == True:
        return True
    else:
        return False