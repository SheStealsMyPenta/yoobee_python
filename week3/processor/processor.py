import pandas as pd
import os
from data_fileFormat_processor import DataFileFormat_Processor
class Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ext = os.path.splitext(file_path)[1].lower()

    def read(self):
        if self.ext == '.csv':
            return pd.read_csv(self.file_path)
        elif self.ext == '.txt':
            return self.read_txt()
        elif self.ext == '.parquet':
            return pd.read_parquet(self.file_path)
        else:
            raise ValueError(f"Unsupported file type: {self.ext}")

    def read_txt(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return pd.DataFrame(lines, columns=["line"])

    def print_first_and_last(self):
        df = self.read()
        print("NUmber of Line")
        print(df.shape[0])
        print("First row:")
        print(df.head(1))
        print("Last row:")
        print(df.tail(1))


def main():
    # file_path = "../sample_text.txt" 
    # processor = Processor(file_path)
    # processor.print_first_and_last()
    file_path = "../Sample_data_2.parquet" 
    processor = Processor(file_path)
    processor.read()
    file_path = '../sample_junk_mail.csv' 
    dfFormat_processor = DataFileFormat_Processor(file_path)
    dfFormat_processor.load_data()
    dfFormat_processor.initial_processing()



if __name__ == '__main__':
    main()