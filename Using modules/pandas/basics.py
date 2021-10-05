import os
import pandas

if os.path.exists("files/temps-today.csv"):
    data = pandas.read_csv("files/temps-today.csv")
    print(data.mean())
else:
    print("File does not exist.")
