import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# connection settings
FREIGHTDB_CONN = os.getenv("FREIGHTDB_CONN")
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

from usatrade import dataloader as usatrade
#print(usatrade.check_table_exists("annual_trade"),"\n\n")
#usatrade.create_usatrade_schema()
#usatrade.create_annual_trade()
#print(usatrade.check_table_exists("annual_trade"))
usatrade.insert_annual_trade(usatrade.get_annual_trade(2019))