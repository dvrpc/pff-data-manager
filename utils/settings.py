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
FREIGHTDB_CONN = os.getenv("FREIGHTDB_CONN")
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")