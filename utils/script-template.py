import os
import psycopg2 as psql
import csv
from settings import conn_string

con = psql.connect(conn_string)
cur = con.cursor()

cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cur.fetchall():
    print(table)