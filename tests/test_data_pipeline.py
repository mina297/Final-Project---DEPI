from src.data.loader import load_raw_data
from src.data.preprocessing import (
    map_attack_labels,
    prepare_dataset,
    validate_attack_labels
)
from src.data.validator import (
    validate_dataset,
    validate_train_test
)


def test_load_raw_data():
    train, test = load_raw_data()
    assert not train.empty
    assert not test.empty


def test_validate_dataset():
    train, test = load_raw_data()
    assert validate_dataset(train)
    assert validate_dataset(test)


def test_validate_train_test():
    train, test = load_raw_data()
    assert validate_train_test(train, test)


def test_attack_mapping():
    train, _ = load_raw_data()
    mapped = map_attack_labels(train)
    assert validate_attack_labels(mapped)


def test_prepare_dataset():
    train, _ = load_raw_data()
    X, y = prepare_dataset(train)

    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 41


def test_no_data_leakage():
    train, _ = load_raw_data()
    X, _ = prepare_dataset(train)

    assert "label" not in X.columns
    assert "difficulty" not in X.columns


def test_expected_attack_classes():
    train, _ = load_raw_data()
    _, y = prepare_dataset(train)

    expected = {"Normal", "DoS", "Probe", "R2L", "U2R"}

    assert set(y.unique()) == expected