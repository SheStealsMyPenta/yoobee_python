import os
from typing import Tuple, List, Union

import pandas as pd
import tensorflow as tf


class Processor:
    """Unified reader for CSV/TXT/Parquet files with an optional CIFAR‑10 helper."""

    _SUPPORTED_TABLE_EXT: Tuple[str, ...] = (".csv", ".txt", ".parquet")

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ext: str = os.path.splitext(file_path)[1].lower()
        if self.ext not in self._SUPPORTED_TABLE_EXT:
            raise ValueError(f"Unsupported file format: {self.ext}")

    # ------------------------------------------------------------------
    # Tabular data loading
    # ------------------------------------------------------------------
    def read(self) -> pd.DataFrame:
        """Dispatch the correct loader based on the file extension and return a ``pandas.DataFrame``."""
        if self.ext == ".csv":
            return pd.read_csv(self.file_path)
        if self.ext == ".txt":
            return self._read_txt(self.file_path)
        if self.ext == ".parquet":
            return pd.read_parquet(self.file_path)
        # This line should never be reached because of the check in ``__init__``.
        raise ValueError(f"Unsupported file type: {self.ext}")

    @staticmethod
    def _read_txt(path: str) -> pd.DataFrame:
        """Read a plain‑text file line by line and return a DataFrame with a single ``line`` column."""
        with open(path, "r", encoding="utf-8") as f:
            lines: List[str] = [line.rstrip("\n") for line in f]
        return pd.DataFrame(lines, columns=["line"])

    # ------------------------------------------------------------------
    # Image data loading
    # ------------------------------------------------------------------
    @staticmethod
    def read_image() -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor, List[str]]:
        """Load the CIFAR‑10 dataset and return train/test splits along with class names."""
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
        class_names: List[str] = [
            "airplane", "automobile", "bird", "cat", "deer",
            "dog", "frog", "horse", "ship", "truck",
        ]
        return x_train, y_train, x_test, y_test, class_names

    # ------------------------------------------------------------------
    # Convenience helpers
    # ------------------------------------------------------------------
    def summary(self) -> None:
        """Print the total number of records, the first row, and the last row of the file."""
        df: pd.DataFrame = self.read()
        print(f"Row count: {len(df)}")
        print("First row:\n", df.head(1))
        print("Last row:\n", df.tail(1))


# ----------------------------------------------------------------------
# Example entry point
# ----------------------------------------------------------------------

def main() -> None:
    """Demonstrate the basic usage of the ``Processor`` class."""

    # 1) Read a Parquet file
    parquet_processor: Processor = Processor("../Sample_data_2.parquet")
    parquet_processor.summary()

    # 2) Read a CSV file
    csv_processor: Processor = Processor("../sample_junk_mail.csv")
    csv_processor.summary()

    # 3) Read a TXT file
    txt_processor: Processor = Processor("../sample_text.txt")
    txt_processor.summary()

    # 4) Load CIFAR‑10 image data
    x_train, y_train, x_test, y_test, classes = Processor.read_image()
    print(f"Training set shape: {x_train.shape}; Test set shape: {x_test.shape}")
    print(f"Class labels: {classes}")


if __name__ == "__main__":
    main()
