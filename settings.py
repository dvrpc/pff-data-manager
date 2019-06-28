##################################
#
#   Standard connection settings for dvrpc-freight scripts
#   Author: Michael Ruane, DVRPC
#   Date: June 28, 2019
#
#################################

import os
from dotenv import load_dotenv
load_dotenv()

# connection settings
host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (host, dbname, user, password)