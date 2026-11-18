from pathlib import Path
import pandas as pd
from .schema import ALL_COLUMNS

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def load_raw_data():
    """Load original NSL-KDD training and testing datasets."""

    train_path = RAW_DIR / "KDDTrain+.txt"
    test_path = RAW_DIR / "KDDTest+.txt"

    if not train_path.exists():
        raise FileNotFoundError(
            f"Training file not found: {train_path}"
        )

    if not test_path.exists():
        raise FileNotFoundError(
            f"Testing file not found: {test_path}"
        )

    train_df = pd.read_csv(
        train_path,
        header=None,
        names=ALL_COLUMNS
    )

    test_df = pd.read_csv(
        test_path,
        header=None,
        names=ALL_COLUMNS
    )

    return train_df, test_df


def load_processed_data():
    """Load labeled training and testing datasets."""

    train_path = PROCESSED_DIR / "train_labeled.csv"
    test_path = PROCESSED_DIR / "test_labeled.csv"

    if not train_path.exists():
        raise FileNotFoundError(f"Processed training file not found: {train_path}")

    if not test_path.exists():
        raise FileNotFoundError(f"Processed testing file not found: {test_path}")

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    return train_df, test_df