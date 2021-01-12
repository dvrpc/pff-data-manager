# Delaware River Ship Calls Metadata

### __[marex.shipcalls]__ - Delaware River Ship Calls
Ship call records of commercial vessels on the Delaware River as compiled by the Maritime Exchange of the Delaware River and Bay.
| Field Name    | Data Type     | Description                       |
| :-------------| :-----------  | :------------                     |
| oid           | serial        | Unique id for data table          |
| date          | datetime      | Date of arrival                   |
| vessel        | text          | Vessel name                       |
| rig           | text          | Type of vessel                    |
| flag          | text          | Country flag of vessel            |
| name          | text          | Common name of port terminal      |
| locid         | text          | MarEx id for port terminal        |
| state         | varchar(2)    | State code of terminal            |
| cargo_typ     | text          | Cargo classification (type)       |
| cargo         | text          | Cargo description                 |
| dir           | varchar(1)    | Load (L)/Discharge (D)            |