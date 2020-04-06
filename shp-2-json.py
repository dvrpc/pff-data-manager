import numpy as np
import pandas as pd
import geopandas as gpd
import json

df = gpd.read_file('G:\My Drive\PFF\Maritime Revamp\MSA\Shapefiles\tl_2019_us_cbsa.shp')
data = df.to_json()

print(data)
