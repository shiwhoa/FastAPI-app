from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .env import my_host, my_database, my_user, my_pass
from .config import local_env_var


### Connect to Postgres DB using SQLalchemy (python to generate sql)
# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# don't need port number

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:785612@127.0.0.1/fastAPI_DB'



# option1: from env.py (depends on .env)
SQLALCHEMY_DATABASE_URL = f'postgresql://{my_user}:{my_pass}@{my_host}/{my_database}'



# option2: from config.py (depends on .env)
SQLALCHEMY_DATABASE_URL = f'postgresql://{local_env_var.db_username}:{local_env_var.db_password}@{local_env_var.db_hostname}/{local_env_var.db_name}'
###


### Create SQL query engine session for the DB
sql_alchemy_database_engine = create_engine(SQLALCHEMY_DATABASE_URL)
sql_alchemy_database_session = sessionmaker(autocommit=False, autoflush=False, bind=sql_alchemy_database_engine)
###


### Call SQL query engine session using function
def get_sql_alchemy_db_session():
    sql_alchemy_db = sql_alchemy_database_session()
    try:
        yield sql_alchemy_db
    finally:
        sql_alchemy_db.close()
###