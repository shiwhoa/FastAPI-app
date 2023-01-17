from dotenv import load_dotenv
load_dotenv()
import os

# gets from .env file

my_host = os.getenv('my_host')
my_database=os.getenv('my_database')
my_user=os.getenv('my_user')
my_pass=os.getenv('my_pass')