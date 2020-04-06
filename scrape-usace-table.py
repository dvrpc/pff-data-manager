import pandas as pd
import requests
#import beautifulsoup4
from bs4 import BeautifulSoup
import select
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Users\kscudder\Documents\GitHub\data-management\chrome_driver\chromedriver.exe')
from pandas import DataFrame
import numpy as np

#define the url
url = 'http://cwbi-ndc-nav.s3-website-us-east-1.amazonaws.com/files/wcsc/webpub/#/report-landing/year/2017/region/1/location/552'
driver.get(url)

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

#clean commodity codes
table['pub_group'] = table['pub_group'].str.split(' ').str[0]
table['pub_group'] = table['pub_group'].astype(int)
table['pub_group'] = table[table['pub_group'] > 1000]
table = table.dropna()
print(table)

#print to csv
port = '552'
year = '2017'
PATH = 'C:\Users\kscudder\Documents\GitHub\data-management\port-cargo\cargo.' + str(year) + '.' + str(port) + '.csv'
table.to_csv(PATH, index = None)

#create empty dataframe to fill
#dfPorts = pd.DataFrame(columns=['port', 'year', 'pub_group', 'dom_intraport', 'dom_receipt', 'dom_shipment', 'for_receipt', 'for_shipment'])

#define attributes
#for row in table.rows:
""" for index, row in table.iterrows():
    port = 552
    year = 2017
    pub_group = row[0]
    dom_intraport = row[7]
    dom_receipt = row[8]
    dom_shipment = row[9]
    for_receipt = row[13]
    for_shipment = row[14] 
    
    dfPorts = dfPorts.append({  [0]: port, 
                                [1]: year, 
                                [2]: pub_group, 
                                [3]: dom_intraport, 
                                [4]: dom_receipt, 
                                [5]: dom_shipment, 
                                [6]: for_receipt, 
                                [7]: for_shipment})
    dfTemp = pd.DataFrame([ port, 
                            year, 
                            pub_group, 
                            dom_intraport, 
                            dom_receipt, 
                            dom_shipment, 
                            for_receipt, 
                            for_shipment])
    print(dfTemp)
    dfPorts.append(dfTemp)  """

#print(dfPorts)
#print(dfTemp)

