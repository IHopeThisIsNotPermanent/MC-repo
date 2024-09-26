#! /bin/bash

### Set Env Vars

#Set the username and password
set PGUSER=postgres
set /P PGPASSWORD=< .\PostgreSQL.pass

#set the data folder
set PGDATA=\PostgreSQL\data

#set the general config
set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=postgres
set PGREQUIREAUTH=true

### Run the command

postgres 