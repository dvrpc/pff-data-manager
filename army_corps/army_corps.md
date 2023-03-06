### army_corps

## Data Source Notes
- Sanitize port_names by replacing apostrophies(') with blank strings (""). Some ports (mostly in Hawai'i) have apostrophies in their name.

## CLI Commands:
- load_principal_ports - retrieves the port_codes and port_names for all principal ports from a Bureau of Transportation Statistics REST service and inserts them into the army_corps.principal_ports table
- load_port_tonnage [folder] - loops through .xlsx files in the specified directory and inserts the contents into the army_corps.port_tonnage table
- load_dvrpc_port_names [file] - takes a .csv file and inserts its conents into the army_corps.dvrpc_port_names table

## To-Do
- Establish procedure for updates/overwriting data and removing duplicates. Change command flags acoordingly
