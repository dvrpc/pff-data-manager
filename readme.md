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

## 3. Commands

...document commands has toolset is developed.
