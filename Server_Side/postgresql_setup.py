import psycopg2, sys, csv, os

hostname = os.getenv("PGHOST", '')
database = os.getenv("PGDATABASE", '')
username = os.getenv("PGUSER", '')
pwd = os.getenv("PGPASSWORD", '')
port_id = os.getenv("PGPORT", 0)

def query(sql):
    result = None
    try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
            )
            
        cur = conn.cursor()

        cur.execute(sql)        

        conn.commit()
        try:
            result = cur.fetchall()
        except:
            pass

        cur.close()
        
        conn.close()

    except Exception as e:
        print(e)
    finally:
        cur.close()
        
        conn.close()

    return result

def setup():

    #NOTE: This is where you update what tables you want in the database.
    tables = [{'name':'example',
               'vars': {'var1' : 'text',
                        'var2' : 'NUMERIC'},
               'constraints':["key_constraint PRIMARY KEY (var1))",
                              ]}]

    for table in tables:
        #Create the table

        #Iterate over the current columns
        db_names, db_dtypes = query("""SELECT column_name, data_type
                                       FROM information_schema.columns
                                       WHERE table_name = 'table_name';
                                    """)
        #Iterate over existing column/tag pairs
        for name, dtype in zip(db_names, db_dtypes):
            if name in table['vars']:
                print(dtype)
                #if dtype != table['vars'][name]:try to change type, if that does not work,
                #delete and recreate.
            else:
                query(f"""ALTER TABLE {table['name']}
                          DROP COLUMN {name} {dtype};
                     """)
        
        #Iterate over the column/tag pairs we want
        for name, dtype in table['vars'].items():
            if not name in db_names:
                query(f"""ALTER TABLE {table['name']}
                          ADD COLUMN {name} {dtype};
                     """)
        
        for constraint in table['constraints']:
            query(f"""ALTER TABLE {table['name']} DROP CONSTRAINT IF EXISTS {constraint};
                      ALTER TABLE {table['name']} ADD CONSTRAINT {constraint};
                     """)

if __name__ == "__main__":
    setup()
