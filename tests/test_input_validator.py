import pytest

from src.data.loader import load_raw_data
from src.data.schema import FEATURE_COLUMNS
from src.data.preprocessing import prepare_dataset
from src.data.validator import (
    validate_dataset,
    validate_train_test
)
from src.data.input_validator import validate_input


def test_valid_input():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    result = validate_input(X.head(5))

    assert result.shape == (5, 41)


def test_missing_feature():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    X = X.drop(columns=[FEATURE_COLUMNS[0]])

    with pytest.raises(ValueError):
        validate_input(X)


def test_extra_feature():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    X["unexpected"] = 1

    with pytest.raises(ValueError):
        validate_input(X)


def test_invalid_input_type():
    with pytest.raises(TypeError):
        validate_input("invalid")


def test_valid_dictionary_input():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    record = X.iloc[0].to_dict()

    result = validate_input(record)

    assert result.shape == (1, 41)


def test_missing_values_input():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    X.loc[X.index[0], FEATURE_COLUMNS[0]] = None

    with pytest.raises(ValueError):
        validate_input(X.head(5))