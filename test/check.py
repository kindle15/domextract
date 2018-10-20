import pandas as pd
import domextract
from os.path import join, dirname


if __name__ == "__main__":


    path = join(dirname(domextract.__file__), "columns.txt")
    
    with open(path, "r") as f:
        columns = [line.strip() for line in f]

    df1 = pd.read_csv("testdata.csv")
    df2 = pd.read_csv("testdata2.csv")

    for c in columns:
        t = df1[c] != df2[c]
        if sum(t) > 0:
            print(c)
            print(df1[c].iloc[:5])
            print(df2[c].iloc[:5])
            print()
