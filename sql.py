import sqlite3, pandas 

# this function will upload the file data to log.db
def upload_to_db(file):

    # default database  as log.db
    con = sqlite3.connect("log.db")
    cur = con.cursor()

    # default table as LOG
    cur.execute("CREATE TABLE IF NOT EXISTS LOG (level VARCHAR(50), message VARCHAR(50), resourceId VARCHAR(50), timestamp VARCHAR(50), traceId VARCHAR(50), spanId VARCHAR(50),commitby VARCHAR(50), parentResourceId VARCHAR(50));")

    #converting csv file to dataframe for editing
    df = pandas.read_csv(file)

    # since, commit is keyword and column name dont accept any symbols
    # we need to rename to columns name as follows
    df.rename(columns = {'commit':'commitby','metadata/parentResourceId':'parentResourceId'}, inplace = True)
    
    #uploading data to log table
    df.to_sql("LOG", con, if_exists='append', index=False)
    
    #commiting any change to table
    con.commit()

    #closing connection
    con.close()

    



