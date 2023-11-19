import pandas as pd
import sqlite3
from tabulate import tabulate

# To view log table in commandline.
def print_db():

    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect('log.db')
    df = pd.read_sql_query("SELECT * from log", con)

    # Verify that result of SQL query is stored in the dataframe
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    con.close()

print_db()
