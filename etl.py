import configparser
import psycopg2
from sql_queries import load_staging_queries, insert_table_queries


def load_staging_tables(conn, cur):
    cur.execute("SET search_path TO staging")
    i=0
    for query in load_staging_queries:
        print(f"query load_staging_queries[{i}] started")
        cur.execute(query)
        conn.commit()
        print(f"query load_staging_queries[{i}] completed")
        i = i + 1
        

def insert_tables(conn, cur):
    cur.execute("SET search_path TO dwh")
    for query in insert_table_queries:
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
    
    print("Function load_staging_tables started.")
    load_staging_tables(conn, cur)
    print("Function load_staging_tables completed.")
    #insert_tables(conn, cur)

    conn.close()


if __name__ == "__main__":
    main()
