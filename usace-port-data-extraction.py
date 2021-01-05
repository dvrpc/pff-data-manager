#!/usr/bin/python

##################################
#
#   USACE principal ports data extration
#   Author: Kristen Scudder, DVRPC
#   Date: March 26, 2019
#      Arguments
#      [1] = windows file path for list of ports
#      
#       Usage: usace-port-data-extraction.py <port file>
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

#imports for scrapeUSACEdata
from bs4 import BeautifulSoup
import select
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Users\kscudder\Documents\GitHub\data-management\chrome_driver\chromedriver.exe')
from pandas import DataFrame
import numpy as np

# check for necessary arguments before running
if (len(sys.argv) < 2 or  len(sys.argv) > 2):
    print """\
        ERROR: This script requires one argument:

        1 - file path for csv list of ports

        Usage: usace-port-data-extraction.py <year directory> <port directory>
        """
    sys.exit(1)

#accept arguments from command line
#years = pd.read_csv(sys.argv[1])
#ports = pd.read_csv(sys.argv[2])
#f = open(sys.argv[2])
#ports = csv.reader(f)

# Scrape the data from USACE website
def scrapeUSACEdata(arg1, arg2, arg3):
    #define the url
    driver.get(arg3)

    #Pass the page source to Beautiful Soup
    soup = BeautifulSoup(driver.page_source,'lxml')
    #print(soup)

    #select the report table elements
    elements = soup.select('tbody tr td')
    print(len(elements))
    elements_cleaned = [c.text.strip().lower() for c in elements]

    #convert array to DataFrame
    df = DataFrame(elements_cleaned)

    #reshape dataframe 
    #(Even though ports only have 13 columns, waterways have 16 columns. 
    # These extra columns are hidden, but still create 16 columns for dataframe)
    df_reshape = np.array(df).reshape(-1, 16)
    table = DataFrame(df_reshape)
    #print(table)

    table.columns = ['pub_group','AllTraffic','Intraport','Receipts','Shipments','Intrawaterway',
                    'DomAllTraffic','dom_intraport','dom_receipts','dom_shipments','DomIntrawaterway',
                    'ForAllTraffic','ForIntraport','for_receipts','for_shipments','ForIntrawaterway']
    #print(table)

    table = table[['pub_group','dom_intraport','dom_receipts','dom_shipments','for_receipts','for_shipments']]
    #print(table)

    #clean commodity codes IF the table is not empty
    if not table.empty:
        table['pub_group'] = table['pub_group'].str.split(' ').str[0]
        table['pub_group'] = table['pub_group'].astype(int)
        table['pub_group'] = table[table['pub_group'] > 1000]
        table = table.dropna()
    print(table)

    #print to csv
    port = arg1
    year = arg2
    PATH = 'C:\Users\kscudder\Documents\GitHub\data-management\port-cargo\cargo.' + str(year) + '.' + str(port) + '.csv'
    table.to_csv(PATH, index = None)
    return

#extract tables by year and portID (available years include 2000 - 2018)
for i in range(2010, 2019):
    year = i
    print i
    f = open(sys.argv[1])
    ports = csv.reader(f)
    for row in ports:
        #print row[0]
        urlbase = 'http://cwbi-ndc-nav.s3-website-us-east-1.amazonaws.com/files/wcsc/webpub/#/report-landing/year/'
        urlbase2 = '/region/4/location/'
        port = row[0]
        url = urlbase + str(year) + urlbase2 + port
        print url
        scrapeUSACEdata(port, year, url)