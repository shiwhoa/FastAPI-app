import psycopg2
from psycopg2.extras import RealDictCursor
from .env import my_host, my_database, my_user, my_pass
import time

def start_psycopg2_postgres_connection():
    while True: # repeatedly try to connect and break out if connected
        try:
            pydantic_psycopg_conn = psycopg2.connect(host=my_host, database=my_database, user=my_user, password=my_pass, cursor_factory=RealDictCursor)
            pydantic_psycopg_cursor = pydantic_psycopg_conn.cursor() # cursor is the variable which allows to manipulate and type sql commands
            print('db connection was successful')
            break
        except Exception as my_error:
            print('db connection has failed')
            print('Error was', my_error)
            time.sleep(2)

    return pydantic_psycopg_conn, pydantic_psycopg_cursor