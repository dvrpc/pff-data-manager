#!/usr/bin/python

##################################
#
#   USA Trade Port Imports and Exports Data Cleaning
#   Author: Kristen Scudder, DVRPC
#   Date: April 2, 2020
#     
#
#################################

import os
import sys
import psycopg2 as psql
import csv
from settings import conn_string
from itertools import islice
import pandas as pd
import requests
from pandas import DataFrame
import numpy as np

""" #import csv files from download
importPath1 = 'G:\Shared drives\Freight Planning\Technical Studies\_Ongoing Studies\Data Management\USAtrade\Port-level Imports (2003-2009).csv'
importPath2 = 'G:\Shared drives\Freight Planning\Technical Studies\_Ongoing Studies\Data Management\USAtrade\Port-level Imports (2010-2019).csv'
exportPath = 'G:\Shared drives\Freight Planning\Technical Studies\_Ongoing Studies\Data Management\USAtrade\Port-level Exports (2003-2019).csv'

import1 = pd.read_csv(importPath1)
import2 = pd.read_csv(importPath2)
export = pd.read_csv(exportPath)

#import1_df = pd.DataFrame(import1)
#import2_df = pd.DataFrame(import2)

imports = import1.append(import2)

#df_usa_trade = pd.concat([imports, export], ignore_index=True, join='outer')
df_usa_trade = pd.merge(imports, export,  how='outer', on=['Commodity','Port','Time']) """

#add usa trade data
df_usa_trade_PATH = 'C:\Users\kscudder\Documents\GitHub\data-management\csv\USATrade\usa-trade-commodities-raw.csv'
df_usa_trade = pd.read_csv(df_usa_trade_PATH)
#remove (Port) from all port names
df_usa_trade['Port'] = df_usa_trade['Port'].str.replace(r'\([^)]*\)', '').str.rstrip()
print(df_usa_trade.head())

#add port IDs
portIDPath = 'C:\Users\kscudder\Documents\GitHub\data-management\csv\usace-usaTrade-port-id-lookup.csv'
portID = pd.read_csv(portIDPath)
#print(portID.head())

#convert port names to string
#df_usa_trade['Port'] = df_usa_trade['Port'].astype(str)
#portID['PortName'] = portID['PortName'].astype(str)

#merge portID with USA Trade Data
usa_trade = pd.merge(df_usa_trade, portID,  how='outer', left_on='Port', right_on='USATradePortName')

#convert commodity code to number
usa_trade['Commodity'] = usa_trade['Commodity'].str.split(' ').str[0]
usa_trade= usa_trade[usa_trade['Commodity'] != 'Total']
#usa_trade.drop(usa_trade[ usa_trade['Commodity'] == 'Total' ].index)
#usa_trade = usa_trade[~usa_trade['Commodity'].astype(str).str.contains('Total')]
usa_trade.dropna(subset=['Commodity'], inplace=True)
print(usa_trade.head())
usa_trade['Commodity'] = usa_trade['Commodity'].astype(int)

#remove Port Totals
usa_trade= usa_trade[usa_trade['Port'] != 'Total']
print(len(usa_trade))

#convert to proper data types
usa_trade['PortID'] = usa_trade['PortID'].fillna(0)
usa_trade['PortID'] = usa_trade['PortID'].astype(int)

usa_trade['Time'] = usa_trade['Time'].astype(int)

usa_trade['Vessel Customs Value (Gen) ($US)'] = usa_trade['Vessel Customs Value (Gen) ($US)'].str.replace(',', '')
usa_trade['Vessel Customs Value (Gen) ($US)'] = usa_trade['Vessel Customs Value (Gen) ($US)'].fillna(0)
usa_trade['Vessel Customs Value (Gen) ($US)'] = usa_trade['Vessel Customs Value (Gen) ($US)'].astype(float)

usa_trade['Vessel SWT (Gen) (kg)'] = usa_trade['Vessel SWT (Gen) (kg)'].str.replace(',', '')
usa_trade['Vessel SWT (Gen) (kg)'] = usa_trade['Vessel SWT (Gen) (kg)'].fillna(0)
usa_trade['Vessel SWT (Gen) (kg)'] = usa_trade['Vessel SWT (Gen) (kg)'].astype(float)

usa_trade['Vessel Total Exports SWT (kg)'] = usa_trade['Vessel Total Exports SWT (kg)'].str.replace(',', '')
usa_trade['Vessel Total Exports SWT (kg)'] = usa_trade['Vessel Total Exports SWT (kg)'].fillna(0)
usa_trade['Vessel Total Exports SWT (kg)'] = usa_trade['Vessel Total Exports SWT (kg)'].astype(float)

usa_trade['Vessel Total Exports Value ($US)'] = usa_trade['Vessel Total Exports Value ($US)'].str.replace(',', '')
usa_trade['Vessel Total Exports Value ($US)'] = usa_trade['Vessel Total Exports Value ($US)'].fillna(0)
usa_trade['Vessel Total Exports Value ($US)'] = usa_trade['Vessel Total Exports Value ($US)'].astype(float)


#write to csv
PATH = 'G:\Shared drives\Freight Planning\Technical Studies\_Ongoing Studies\Data Management\USAtrade\usa-trade-commodities-cleaned.csv'
usa_trade.to_csv(PATH, index = None)

