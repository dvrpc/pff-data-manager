# DVRPC Freight Postgres Database

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






***
# Template for a new data table
[Markdown resources](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)


### __[table name]__ - Human-readable Name
Data description. Yes, Yes, without the oops! Do you have any idea how long it takes those cups to decompose. Yeah, but your scientists were so preoccupied with whether or not they could, they didn't stop to think if they should. You really think you can fly that thing?

Source: [Name of source](https://www.url.of.source)

| Field Name    | Data Type     | Description                       |
| :-------------| :-----------  | :------------                     |
| oid           | serial        | Unique id for data table          |
| year          | smallint      | Year of reported data             |
| portid        | varchar(6)    | Foreign key to [pports_dict] portid |
