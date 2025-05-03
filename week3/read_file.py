import pandas as pd

def print_first_and_last_line_with_pandas(file_path):
    df = pd.read_csv(file_path, header=None)
    print("First line:", df.iloc[0, 0])
    print("Last line:", df.iloc[-1, 0])
print_first_and_last_line_with_pandas("./sample_text.txt")



import pandas as pd

def print_first_and_last_line_with_pandas(file_path):
    df = pd.read_parquet(file_path)
    print("number of row")
    print(df.shape[0])
    print("First row:")
   
    print(df.head(1))
    print("Last row:")
    print(df.tail(1))

print_first_and_last_line_with_pandas("Sample_data_2.parquet")
