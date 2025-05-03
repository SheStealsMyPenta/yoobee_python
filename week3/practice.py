import os
import pandas as pd

def print_csv():
    for file in os.listdir('.'):
        if file.endswith('.csv'):
            df = pd.read_csv(file)
            print(df.head(2))
            break
print_csv()