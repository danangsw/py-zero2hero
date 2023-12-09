import pandas as pd

data_tsv = pd.read_csv("../data/chipotle.tsv", sep = "\t")

def data_transformation(data):
    
    data["item_price"] = data["item_price"].str.replace("$","").astype(float)
    
    return data

data_transformed = data_transformation(data_tsv)