import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# connection settings
FREIGHTDB_CONN = os.getenv("FREIGHTDB_CONN")
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

from army_corps import dataloader as ac
#ac.load_tonnage(r"C:\Users\mbrahms\Documents\GitHub\pff-data-manager\army_corps\army_corps_xlsx")
ac.load_dvrpc_port_names(r"C:\Users\mbrahms\Documents\GitHub\pff-data-manager\army_corps\dvrpc_ports.csv")
