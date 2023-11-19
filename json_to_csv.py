# import pandas as pd

# # Load JSON data into DataFrame
# df = pd.read_json("log.json")

# # Convert JSON to CSV
# df.to_csv("output.csv", index=False)

import pandas as pd
import json

#Converting uploaded .json file to .csv file
def json_to_csv(file):
    
    #Opening file in read mode
    with open(file, "r") as file:
        data = json.load(file)
    
    #this help in metadata column of required json format
    df = pd.json_normalize(data)

    # since, commit is keyword and column name dont accept any symbols
    # we need to rename to columns name as follows   
    df.rename(columns = {'commit':'commitby','metadata.parentResourceId':'parentResourceId'}, inplace = True)

    #saving file to train our embedchain bot
    df.to_csv("converted_json.csv", index=False)