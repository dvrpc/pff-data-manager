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


def get_trade(year):
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
            hs_group = int(item[2])
            vessel_kg = int(item[3])
            vessel_value = int(item[4])
            cont_kg = int(item[5])
            cont_value = int(item[6])

            cur.execute(
                f"""
                    INSERT INTO ustrade.annual_trade(year, type, portid, hs_group, vessel_kg, vessel_value, cont_kg, cont_value) 
                    VALUES (
                        {year},'{type}',{portid},{hs_group},{vessel_kg},{vessel_value}, {cont_kg}, {cont_value}
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


if __name__ == "__main__":
    get_trade()
    check_year()
