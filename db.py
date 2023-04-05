import psycopg2
import sqlalchemy
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("DB_HOST")
port=os.getenv("DB_PORT")
db=os.getenv("DB_NAME")
user=os.getenv("DB_USER")
pwd=os.getenv("DB_PASSWORD")

def getData(query):
    
    conn = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}")

    # A function that takes in a PostgreSQL query and outputs a pandas database 
    def create_pandas_table(sql_query, database = conn):
        table = pd.read_sql_query(sql_query, database)
        return table
      
    # Utilize the create_pandas_table function to create a Pandas data frame
    # Store the data as a variable

    return create_pandas_table(query)

    # Close the connection
    conn.close()