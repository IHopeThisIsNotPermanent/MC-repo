#! /bin/bash

### Set Env Vars
set PGUSER=postgres
set /P PGPASSWORD=< .\PostgreSQL.pass
set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=postgres
set PGREQUIREAUTH=true

### Run the command

python ./postgresql_setup.py