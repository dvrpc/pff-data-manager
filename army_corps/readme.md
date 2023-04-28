# army_corps 

## Data Source Notes
- Sanitize port_names by replacing apostrophies(') with blank strings (""). Some ports (mostly in Hawai'i) have apostrophies in their name.
- The port_name is used for joining principal port tables since port_codes have been inconsistent
- The army_corps.princtipal_ports table has been generated manually because all external sources of principal ports definitions have proved problematic. See Principal Ports Procedure below for more information.
- GEOIDs are stored as character strings even if they only contain digits
- The DVRPC region is NOT coterminus with the Philadelphia-Camden-Wilmington MSA (GEOID: 37980)

## Principal Ports Procedure
- The principal_ports table contains five columns:
    - port_name: text, serves as the key, should not be NULL
    - msa_geoid: 5 character string, indicates the geoid of the Metroplitan Statisical Area in which the port is located, NULL if the port is not in an MSA
    - dvrpc, text, equals 'y' if in the dvrpc region, otherwise NULL
    - long, double precision, longitude of port 
    - lat, double precision, latitude of port 
- Its purpose is to be a static table (not a dynamic view) that contains all the unique port_names from the port_tonnage table and links each of them to a Metropolitan Statistical Area and whether or not it is included in the dvrpc region. Since the spatial join is performed outside SQL, the lat and long columns are currenly unused but may be useful for visualizations in the future. 
- The geospatial analysis can be done in ArcPro (or postGIS, etc). The results of the analyis performed in April 2023 are saved on the Freight Planning Google Drive here: Freight Planning\Technical Studies\_FreightData\port_msa_4apr23_final.xlsx
    - The results are saved as an excel file because editing the raw CSV file in Excel can lead to an undetermined issue (probably a character encoding thing).
    - To avoid the issues exporting the results of analysis done in Arc, export the attribute table from ArcPro (you can use your table format of choice, as long as Excel can open it), open the exported table in Excel, immediately save the table as an new xlsx file, then make any nessary manual edits to the xlsx file.
- To get a single point geometry per port_name, first collect all the geospatial data available, then find the centorid of all the points with the same name. Data sources used in the April 2023 analysis include:
    - The archived pports*.zip files from various years avaiable from the U.S. Army Corps of Engineers Digital Library here: https://usace.contentdm.oclc.org/digital/collection/p16021coll2/id/1450/rec/1
    - The principal ports REST service using the query shown here: https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/ndc/FeatureServer/1/query?where=1%3D1&outFields=PORT_NAME,PORT,TYPE&returnGeometry=true&outSR=4326&f=geojson
- Once each port_name has a single point, join them to the MSA layer available here: https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer. Then, add an x and y column and export the resulting table.
- Open the exportred table in Excel, add the dvrpc column and fill it out mannually.
    -  TIP: since all the dvrpc ports will be in either Pennsylvania or New Jersey, you can narrow the list down by only looking at ports that contain the strings 'PA' or 'NJ'
- On the SQL server pull all the distinct port_names in the port_tonange table and add any missing names to the Excel table and populate the appropriate columns.
- Export the Excel file as a csv and use the insert_csv command to insert the rows into the army_corps.principal_ports table.

## CLI Commands (note the use of dashes rather than underscores):
- insert_principal_ports [path] - inserts a csv file into the army_corps.principal_ports table. Assumes table and all CSV columns already exist on the server, have mathcing names, and are of the proper type.
- load-port-tonnage [folder] - loops through .xlsx files in the specified directory and inserts the contents into the army_corps.port_tonnage table


