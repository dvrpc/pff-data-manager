# U.S. Army Corps of Engineers WaterBorne Commerce Statistics Metadata

## Maritime Trade Data
### __[pports_act]__ - Principal Port Activity 
The U.S. Army Corps of Engineers maintains several data sets through the Waterborne Commerce Statistics Center (WCSC). This data provides information such as total volume, value, and Twenty-Foot Equivalent Units (TEUs) for at least the top 150 Principal Ports in the United States. This table provides the WCSC data for all Principal Ports for each of the available years. This is summary data and may exclude smaller activity ports nationwide.

Source: [US Army Corps of Engineers, Principal Ports of the United States](https://usace.contentdm.oclc.org/digital/collection/p16021coll2/id/2094/)

| Field Name    | Data Type     | Description                       |
| :-------------| :-----------  | :------------                     |
| oid           | serial        | Unique id for data table          |
| year          | smallint      | Year of reported data             |
| portid        | varchar(6)    | Foreign key to [pports_dict] portid |
| domestic      | integer       | Volume of domestic trade (ktons)  |
| import        | integer       | Volume of foreign imports (ktons) |
| export        | integer       | Volume of foreign exports (ktons) |


### __[pports_cargo]__ - Principal Port Cargo
This table provides the WCSC data for all Principal Ports in the DVRPC region for each of the available years. This data includes receipt and shipment volume by commodity ID for foreign and domestic trade as well as intraport volume for domestic ports.

Source: [US Army Corps Principal Port Cargo Reports](http://cwbi-ndc-nav.s3-website-us-east-1.amazonaws.com/files/wcsc/webpub/#/report-landing/year/2017/region/1/location/552)

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| oid           | serial        | Unique id for data table              |
| year          | smallint      | Year of reported data                 |
| portid        | varchar(6)    | Foreign key to [pports_dict] portid   |
| pub_group     | smallint      | WCSC Published Commodity Code         |
| dom_intraport | integer       | Volume of domestic intraport movement (ktons)|
| dom_receipt   | integer       | Volume of domestic receipts (ktons)   |
| dom_shipment  | integer       | Volume of domestic shipments (ktons)  |
| for_receipt   | integer       | Volume of foreign imports (ktons)     |
| for_shipment  | integer       | Volume of foreign exports (ktons)     |


### __[pports_trips]__ - Principal Port Trips
This table provides the WCSC data for all Principal Ports in the DVRPC region for each of the available years. This data includes receipt and shipment trip counts by traffic type for each port.

Source: [US Army Corps Principal Port Trip Reports](http://cwbi-ndc-nav.s3-website-us-east-1.amazonaws.com/files/wcsc/webpub/#/report-landing/year/2017/region/1/location/552)

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| oid           | serial        | Unique id for data table              |
| year          | smallint      | Year of reported data                 |
| portid        | varchar(6)    | Foreign key to [pports_dict] portid   |
| receipt_trip  | integer       | Count of receipt trips                |
| shipment_trip | integer       | Count of shipment trips               |
| traffic_type  | smallint      | Traffic type code                     |


### __[pub_comm_code]__ - WSCS Published Commodity Codes
This table provides the WCSC 4-digit published commodity code. 

Source: [US Army Corps Commodity Codes (WCUS) Cross Reference](https://usace.contentdm.oclc.org/digital/collection/p16021coll2/id/2107)

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| pub_group     | smallint      | Unique commodity code                 |
| pub_name      | text          | Commodity Code Name                   |


### __[pports_traf_type]__ - Principal Ports Traffic Type
This table provides a 2-digit marine activity traffic type code for principal port trip activity.

Source: 

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| traf_code     | smallint      | Unique 2-digit traffic type code      |
| traf_name     | varchar(50)   | Traffic Type Description              |



<!-- ***
# Template for a new data table
[Markdown resources](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)


### __[table name]__ - Human-readable Name
Data description. Yes, Yes, without the oops! Do you have any idea how long it takes those cups to decompose. Yeah, but your scientists were so preoccupied with whether or not they could, they didn't stop to think if they should. You really think you can fly that thing?

Source: [Name of source](https://www.url.of.source)

| Field Name    | Data Type     | Description                       |
| :-------------| :-----------  | :------------                     |
| oid           | serial        | Unique id for data table          |
| year          | smallint      | Year of reported data             |
| portid        | varchar(6)    | Foreign key to [pports_dict] portid | -->
