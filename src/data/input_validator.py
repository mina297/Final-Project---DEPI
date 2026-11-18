import pandas as pd

from .schema import FEATURE_COLUMNS


def validate_input(data):
    """
    Validate input data before model prediction.
    Supports both dictionary and DataFrame inputs.
    """

    # Convert dictionary to DataFrame
    if isinstance(data, dict):
        data = pd.DataFrame([data])

    # Check input type
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Input must be a DataFrame or dictionary."
        )

    # Check missing and unexpected features
    missing = set(FEATURE_COLUMNS) - set(data.columns)
    extra = set(data.columns) - set(FEATURE_COLUMNS)

    if missing:
        raise ValueError(
            f"Missing features: {sorted(missing)}"
        )

    if extra:
        raise ValueError(
            f"Unexpected features: {sorted(extra)}"
        )

    # Check missing values
    if data.isnull().any().any():
        raise ValueError(
            "Input contains missing values."
        )

    # Return features in the correct order
    return data[FEATURE_COLUMNS].copy()