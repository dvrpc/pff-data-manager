# PhillyFreightFinder Data Manager

An internal python toolset for managing datasets behind DVRPC's PhillyFreightFinder regional data program. This toolset is built with a Command Line Interface (CLI) for various ETL functions of data utilized by the DVRPC Freight Planning program.

## 1. Setup Environment

This toolset is configured to run in a conda virtual enviroment. To install necessary dependencies and begin using the toolset, create and activate the virtual environment:

```
# create environment (named pff-data-manager)
conda env create -f environment.yml

# activate your conda env
conda activate pff-data-manager
```

## 2. Configure settings

This toolset uses environment variables for managing database and datasource connections/locations. Create a `.env` file in the local directory with thhe following variables:

```
FREIGHTDB_CONN = "postgresql://username:password@host:port/dbname"
CENSUS_API_KEY = "CENSUS API KEY"
```

## 3. File Structure

Most of the files in this toolset are grouped in directories by the external datasource they interact with. This is intended to parallel the structure of the SQL server where schemas group together tables from the same datasource, and to allow for data sources with different release schedules to be updated independently. As detailed below,the dataloader.py file contains most of the functions required to: retrieve and clean external data, create tables and a schema for that data in a SQL database, and populate those tables with the cleaned data. The cli.py file defines terminal commands using the click library. Commands begin with the name of the datasource, which should be the same as the name of the subdirectory for that datasource, followed by another command. Insert commands retreive external data and insert it into a SQL table. Get commands retrive and print external data, but do not write to the SQL database. This makes it convient to check the data before committing it to the database. Finally some commands may have parameters. The parameters for the get and insert commands should be the same. The readme.md file contains documentation for the datasource-specific implementations of the functions  and commands listed below.
### Example Datasource Subdirectory Structure
- Folder Name: Example
- dataloader.py (functions listed)
    - check_schema_exists
    - check_table_exists
    - create_example_schema
    - create_example_data_table
    - get_example_data_table
    - insert_example_data
- cli.py (commands listed)
    - example check_schema
    - example check_table table
    - example create_schema
    - example create_table
    - example load data
- readme.md

## To-Do:
- In cli.py, consolidate get and insert commands into load
- Move schema functions to database folder 