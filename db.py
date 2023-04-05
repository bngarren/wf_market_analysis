import psycopg2
import sqlalchemy
import pandas as pd

host="96.255.166.164"
port="6500"
db="wf_market"
user="postgres"
pwd="bng2113!"

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