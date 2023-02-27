import os
import psycopg2 as psql
import openpyxl
import pandas as pd
from utils.settings import FREIGHTDB_CONN, CENSUS_API_KEY

con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()

def load_tonnage(dir):
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".xlsx"):
            sheetName = getPortSheetName(os.path.join(dir, file))
            year = getYear(os.path.join(dir, file), sheetName)
            ports = pd.read_excel(os.path.join(dir, file), sheet_name=sheetName, header=4)
            for row in ports.itertuples(name=None):
                cur.execute("""
                INSERT INTO army_corps.port_tonnage(port_name, year, total_tons, domestic_tons, foreign_tons, import_tons, export_tons)
                VALUES ('{port_name}', {year}, {total}, {domestic}, {foreign}, {import_tonnage}, {export})
                """.format(port_name=row[2].replace("'",""), year=year, total=row[3], domestic=row[4], foreign=row[5], import_tonnage=row[6], export=row[7]))
        else:
            continue
    con.commit()

def getPortSheetName(path):
    possibleNames = ["Ports_by_Name", "Port_Name"]
    xlsx = openpyxl.load_workbook(path)
    sheets = xlsx.sheetnames
    for name in possibleNames:
        if name in sheets:
            return name
    raise Exception("getPortSheetName was unable to determine the proper sheet name for the workbook {wb}".format(wb=path))

def getYear(path, sheetName):
    sheet = openpyxl.load_workbook(path)[sheetName]
    year = sheet["B2"].value
    year = year[year.index("in") + 3:]
    return year