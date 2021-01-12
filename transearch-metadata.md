# TRANSEARCH 2011 IHS Global Insights Metadata


### __[Destination_regions]__ - Destination Regions 
This table provides the details on the destination regions 

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| region        | smallint      | Unique id for destination regions     |
| region_name   | text          | Destination region name               |
| state         | varchar(3)    | Destination region state name         |
| BEA           | smallint      | Business economic area code           |
| BEA_name      | text          | Business economic area name           |
| Country       | varchar(3)    | Destination region country            |


### __[Origin_regions]__ - Origin Regions
This table provides the details on the origin regions 

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| region        | smallint      | Unique id for origin regions          |
| region_name   | text          | Origin region name                    |
| state         | varchar(3)    | Origin region state name              |
| BEA           | smallint      | Business economic area code           |
| BEA_name      | text          | Business economic area name           |
| Country       | varchar(3)    | Origin region country                 |

### __[stcc_commodity]__ - Standard Transportation Commodity Code (STCC)
This table provides the 4 digit STCC Commodity code and description

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| ID            | smallint      | Unique id for STCC Commodity Code     |
| STCC4         | integer       | STCC 4-digit code                     |
| name          | text          | STCC name uppercase                   |
| proper        | text          | STCC name lowercase                   |
| STCC          | varchar(5)    | STCC 2 or 4-digit code                |

### __[modes]__ - Modes
This table provides a 2 digit code for mode

| Field Name    | Data Type     | Description                           |
| :-------------| :-----------  | :------------                         |
| number        | smallint      | Unique id for modes                   |
| code          | varchar(5)    | Mode abbreviation code                |
| text          | text          | Mode description                      |
| mode_group    | text          | Mode group description                |
| mode_group_id | smallint      | Mode group code                       |

### __[PA2011]__ - DVRPC IHS Commodity Data
This table provides the details on the origin regions 

| Field Name            | Data Type     | Description                           |
| :-------------        | :-----------  | :------------                         |
| oid                   | serial        | Unique id for data table              |
| year                  | smallint      | Year of reported data                 |
| origin_region         | smallint      | Origin region code                    |
| destination_region    | smallint      | Destination region code               |
| STCC                  | smallint      | STCC 4-digit code                     |
| mode                  | smallin       | Mode group code                       |
| tons                  | integer       | Volume of commodities (ktons)         |
| value                 | integer       | Value of commodities ($M)             |
| units                 | integer       | ???                                   |
| STCC4                 | varchar(6)    | STCC 2 or 4-digit code                |

