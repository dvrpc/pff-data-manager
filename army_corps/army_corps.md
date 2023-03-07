# army_corps 

## Data Source Notes
- Sanitize port_names by replacing apostrophies(') with blank strings (""). Some ports (mostly in Hawai'i) have apostrophies in their name.
- To maintain a list of regional ports while port names change, the dvrpc_port_names table lists current or former port names and whether or not they are in the DVRPC region. This allows records from all years to be joined on port_name then filtered to only those where the dvrpc='y'. This table will have to be updated if a port in the DVRPC region changes names using the load-dvrpc-port-names command and csv file. The panj_port_names view on the SQL server lists all the unqiue port_names from the port_tonnage table that end with 'PA' or 'NJ'. To update a user can copy the view to a CSV, add and populate the dvrpc column, then use the load-dvrpc-port-names to push the updated list to the server

## CLI Commands (note the use of dashes rather than underscores):
- load-principal-ports - retrieves the port_codes and port_names for all principal ports from a Bureau of Transportation Statistics REST service and inserts them into the army_corps.principal_ports table
- load-port-tonnage [folder] - loops through .xlsx files in the specified directory and inserts the contents into the army_corps.port_tonnage table
- load-dvrpc-port-names [file] - takes a .csv file and inserts its conents into the army_corps.dvrpc_port_names table

## To-Do
- Establish procedure for updates/overwriting data and removing duplicates. Change command flags acoordingly
