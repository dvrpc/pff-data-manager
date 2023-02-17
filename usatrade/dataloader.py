import requests
import psycopg2 as psql
import json

from utils.settings import FREIGHTDB_CONN, CENSUS_API_KEY

SQL_INSERT_USATRADE = """
        INSERT INTO ustrade.annual_trade(year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value) 
        VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s
        )
    """
con = psql.connect(FREIGHTDB_CONN)
cur = con.cursor()
def get_annual_trade(year):
    directions = ["imports", "exports"]
    dvrpc_ports = [1107, 1102, 1113, 1105, 1101]

    port_str = "".join(["&PORT=" + str(port) for port in dvrpc_ports])

    data = []
    for imex in directions:

        comm = "E" if imex == "exports" else "I"
        response = requests.get(
            f"https://api.census.gov/data/timeseries/intltrade/{imex}/porths?key={CENSUS_API_KEY}&get=PORT,PORT_NAME,{comm}_COMMODITY,VES_WGT_YR,VES_VAL_YR,CNT_VAL_YR,CNT_WGT_YR{port_str}&COMM_LVL=HS2&time={year}-12"
        )

        for item in response.json()[1:]:
            type = imex
            portid = item[0]
            portname = item[1]
            hs_group = int(item[2])
            vessel_kg = int(item[3])
            vessel_value = int(item[4])
            cont_kg = int(item[5])
            cont_value = int(item[6])

            data.append([year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value, portname])

    return data
def insert_annual_trade(data):
    for item in data:
            year = item[0]
            type = item[1]
            portid = item[2]
            hs_group = item[3]
            vessel_kg = item[4]
            vessel_value = item[5]
            cont_kg = item[6]
            cont_value = item[7]
            portname = item[8]

            cur.execute(
                f"""
                    INSERT INTO usatrade.annual_trade(year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value, portname) 
                    VALUES (
                        {year},'{type}',{portid},{hs_group},{vessel_kg},{vessel_value}, {cont_kg}, {cont_value}, '{portname}'
                    )
                """
            )
    con.commit()

def get_and_insert_annual_trade(year):
    directions = ["imports", "exports"]
    dvrpc_ports = [1107, 1102, 1113, 1105, 1101]

    port_str = "".join(["&PORT=" + str(port) for port in dvrpc_ports])

    for imex in directions:

        comm = "E" if imex == "exports" else "I"
        data = requests.get(
            f"https://api.census.gov/data/timeseries/intltrade/{imex}/porths?key={CENSUS_API_KEY}&get=PORT,PORT_NAME,{comm}_COMMODITY,VES_WGT_YR,VES_VAL_YR,CNT_VAL_YR,CNT_WGT_YR{port_str}&COMM_LVL=HS2&time={year}-12"
        )

        for item in data.json()[1:]:
            type = imex
            portid = item[0]
            portname = item[1]
            hs_group = int(item[2])
            vessel_kg = int(item[3])
            vessel_value = int(item[4])
            cont_kg = int(item[5])
            cont_value = int(item[6])

            cur.execute(
                f"""
                    INSERT INTO usatrade.annual_trade(year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value, portname) 
                    VALUES (
                        {year},'{type}',{portid},{hs_group},{vessel_kg},{vessel_value}, {cont_kg}, {cont_value}, '{portname}'
                    )
                """
            )
        print("USA Trade %s for %s loaded to database" % (imex, year))
    con.commit()

def check_year(year):
    """Check that data isn't already in the database"""
    sql = "SELECT EXISTS(SELECT 1 FROM ustrade.annual_trade WHERE year = %s)"

    cur.execute(sql, (year,))
    val = cur.fetchone()
    if val[0] == True:
        return "exists"
    else:
        return "new"

def check_table_exists(table_name, schema_name="usatrade"):
    """Check if table is already in the database"""
    sql= "SELECT EXISTS (SELECT 1 from information_schema.tables WHERE table_name=%s AND table_schema=%s)"

    cur.execute(sql, (table_name,schema_name))
    val = cur.fetchone()
    if val[0] == True:
        return True
    else:
        return False

def check_schema_exists(schema_name):
    """Check if schema is already in the database"""
    sql= "SELECT EXISTS (SELECT 1 from information_schema.schemata WHERE schema_name=%s)"

    cur.execute(sql, (schema_name,))
    val = cur.fetchone()
    if val[0] == True:
        return True
    else:
        return False

def get_top(year, type, unit, port, num):
    """Return the top commodities"""
    sql = """
    SELECT h.hs_name, t.v FROM (SELECT sum(%s) as v, hs_group
    FROM ustrade.annual_trade 
    WHERE type = %s AND year = %s %s
    GROUP BY hs_group) as t
    INNER JOIN hs_comm_code as h
    ON h.hs_group = t.hs_group
    ORDER BY t.v DESC
    LIMIT %s;
    """

def create_annual_trade(overwrite=False):
    exists = check_table_exists("annual_trade")
    if overwrite or not exists:
        sql = """CREATE TABLE usatrade.annual_trade
            (
            uid SERIAL,
            portid character varying(4),
            portname text,
            year smallint,
            hs_group smallint,
            type text,
            vessel_kg double precision,
            vessel_value double precision,
            cont_kg double precision,
            cont_value double precision
            )
        """
        cur.execute(sql)
        con.commit()
    else:
        print("Table annual_trade already exists. Set overwrite to True to create it anyway.")

def create_usatrade_schema(overwrite=False):
    exists = check_schema_exists("usatrade")
    if overwrite or not exists:
        sql = """CREATE SCHEMA usatrade"""
        cur.execute(sql)
        con.commit()
    else:
        print("Schema usatrade already exists. Set overwrite to True to create it anyway.")

if __name__ == "__main__":
    #insert_annual_trade()
    #check_year()
    pass
