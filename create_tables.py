import configparser
import psycopg2
from sql_queries import drop_staging_queries, create_staging_queries, drop_table_queries, create_table_queries


def drop_staging_tables(conn, cur):
    cur.execute("SET search_path TO staging")
    for query in drop_staging_queries:
        cur.execute(query)
        conn.commit()

def create_staging_tables(conn, cur):
    cur.execute("SET search_path TO staging")
    for query in create_staging_queries:
        cur.execute(query)
        conn.commit()
        
def drop_tables(conn, cur):
    cur.execute("SET search_path TO dwh")
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
def create_tables(conn, cur):
    cur.execute("SET search_path TO dwh")
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')                
    
    ENDPOINT = config.get("CLUSTER","ENDPOINT")
    DB_NAME = config.get("CLUSTER","DB_NAME")
    DB_USER = config.get("CLUSTER","DB_USER")
    DB_USER = config.get("CLUSTER","DB_USER")
    DB_PASSWORD = config.get("CLUSTER","DB_PASSWORD")
    
    conn = psycopg2.connect(f"host='{ENDPOINT}' port='5439' user={DB_USER} password={DB_PASSWORD} dbname='{DB_NAME}'")
    cur = conn.cursor()
    
    cur.execute("CREATE SCHEMA IF NOT EXISTS staging;");
    cur.execute("CREATE SCHEMA IF NOT EXISTS dwh;");
    
    print("Function drop_staging_tables started.")
    drop_staging_tables(conn, cur)
    print("Function drop_staging_tables completed.")
    
    print("Function create_staging_tables started.")
    create_staging_tables(conn, cur)
    print("Function create_staging_tables completed.")
    
    print("Function drop_tables started.")
    drop_tables(conn, cur)
    print("Function drop_tables completed.")
    
    print("Function create_tables started.")
    create_tables(conn, cur)
    print("Function create_tables completed.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
