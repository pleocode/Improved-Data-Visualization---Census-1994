import pandas as pd

def read_file():
    file = pd.read_csv("Census 1994.csv", delimiter=";")
    return file