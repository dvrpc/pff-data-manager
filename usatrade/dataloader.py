import requests
import psycopg2 as psql
import json

from utils.settings import conn_string

SQL_INSERT_USATRADE = """
        INSERT INTO usa_trade(year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value) 
        VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s
        )
    """
con = psql.connect(conn_string)
cur = con.cursor()

def get_trade(year):
    directions = ['imports', 'exports']

    for imex in directions:
        
        comm = 'E' if imex == 'exports' else 'I' 
        url = 'https://api.census.gov/data/timeseries/intltrade/%s/porths?get=PORT,PORT_NAME,%s_COMMODITY,VES_WGT_YR,VES_VAL_YR,CNT_VAL_YR,CNT_WGT_YR&PORT=1107&PORT=1102&PORT=1113&PORT=1105&PORT=1101&COMM_LVL=HS2&time=%s-12'
        data=requests.get(url % (imex, comm, year))

        for item in data.json()[1:]:
            type = imex
            portid = item[0]
            hs_group = int(item[2])
            vessel_kg = int(item[3])
            vessel_value = int(item[4])
            cont_kg = int(item[5])
            cont_value = int(item[6])

            # cur.execute(SQL_INSERT_USATRADE, (year, type, portid, hs_group,vessel_kg,vessel_value,cont_kg,cont_value))
        print("USA Trade %s for %s imported to database" % (imex,year))
    con.commit()

def check_year(year):
    """Check that data isn't already in the database"""
    sql = "SELECT EXISTS(SELECT 1 FROM usa_trade WHERE year = %s)"

    cur.execute(sql, (year,))
    val = cur.fetchone()
    if val[0] == True:
        return 'exists'
    else:
        return 'new'

def get_top(year, type, unit, port, num):
    """Return the top commodities"""
    sql = """
    SELECT h.hs_name, t.v FROM (SELECT sum(%s) as v, hs_group
    FROM usa_trade 
    WHERE type = %s AND year = %s %s
    GROUP BY hs_group) as t
    INNER JOIN hs_comm_code as h
    ON h.hs_group = t.hs_group
    ORDER BY t.v DESC
    LIMIT %s;
    """

if __name__ == "__main__":
    get_trade()
    check_year()