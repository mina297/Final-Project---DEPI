import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype

from .schema import (
    FEATURE_COLUMNS,
    ALL_COLUMNS,
    TARGET_COLUMN,
    DIFFICULTY_COLUMN
)

from .preprocessing import validate_attack_labels


CATEGORICAL_COLUMNS = [
    "protocol_type",
    "service",
    "flag",
    TARGET_COLUMN
]

NUMERICAL_COLUMNS = [
    col for col in FEATURE_COLUMNS
    if col not in CATEGORICAL_COLUMNS
] + [DIFFICULTY_COLUMN]


def validate_columns(df):
    """Validate dataset columns."""

    if list(df.columns) != ALL_COLUMNS:
        raise ValueError("Dataset columns do not match official schema.")

    return True


def validate_missing_values(df):
    """Check missing values."""

    missing = df.isnull().sum()

    if missing.sum() > 0:
        raise ValueError(
            f"Missing values found:\n{missing[missing > 0]}"
        )

    return True


def validate_duplicates(df):
    """Check duplicates within dataset."""

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Dataset contains {duplicates} duplicate rows."
        )

    return True


def validate_data_types(df):
    """Validate categorical and numerical columns."""

    for column in CATEGORICAL_COLUMNS:
        if not is_string_dtype(df[column]):
            raise TypeError(
                f"Invalid categorical type: {column}"
            )

    for column in NUMERICAL_COLUMNS:
        if not is_numeric_dtype(df[column]):
            raise TypeError(
                f"Invalid numerical type: {column}"
            )

    return True


def validate_dataset(df, check_labels=False):
    """Run all dataset validation checks."""

    validate_columns(df)
    validate_missing_values(df)
    validate_duplicates(df)
    validate_data_types(df)

    if check_labels:
        validate_attack_labels(df)

    return True


def validate_train_test(train_df, test_df):
    """Validate training and testing datasets."""

    validate_dataset(train_df)
    validate_dataset(test_df)

    if list(train_df.columns) != list(test_df.columns):
        raise ValueError("Train/Test columns mismatch.")

    return True