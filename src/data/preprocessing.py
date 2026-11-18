import pandas as pd

from .schema import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    DIFFICULTY_COLUMN
)


ATTACK_MAPPING = {
    # DoS
    "back": "DoS",
    "land": "DoS",
    "neptune": "DoS",
    "pod": "DoS",
    "smurf": "DoS",
    "teardrop": "DoS",
    "mailbomb": "DoS",
    "apache2": "DoS",
    "processtable": "DoS",
    "udpstorm": "DoS",

    # Probe
    "ipsweep": "Probe",
    "nmap": "Probe",
    "portsweep": "Probe",
    "satan": "Probe",
    "mscan": "Probe",
    "saint": "Probe",

    # R2L
    "ftp_write": "R2L",
    "guess_passwd": "R2L",
    "imap": "R2L",
    "multihop": "R2L",
    "phf": "R2L",
    "spy": "R2L",
    "warezclient": "R2L",
    "warezmaster": "R2L",
    "snmpgetattack": "R2L",
    "snmpguess": "R2L",
    "xlock": "R2L",
    "xsnoop": "R2L",
    "httptunnel": "R2L",
    "sendmail": "R2L",
    "named": "R2L",
    "worm": "R2L",

    # U2R
    "buffer_overflow": "U2R",
    "loadmodule": "U2R",
    "perl": "U2R",
    "rootkit": "U2R",
    "ps": "U2R",
    "sqlattack": "U2R",
    "xterm": "U2R"
}


def map_attack_labels(df):
    """Map original attack labels into five categories."""

    df = df.copy()

    df[TARGET_COLUMN] = (
        df[TARGET_COLUMN]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df[TARGET_COLUMN] = df[TARGET_COLUMN].replace(
        {"normal": "Normal", **ATTACK_MAPPING}
    )

    return df


def validate_attack_labels(df):
    """Check whether all attack labels are recognized."""

    unknown = set(df[TARGET_COLUMN].unique()) - {
        "Normal", "DoS", "Probe", "R2L", "U2R"
    }

    if unknown:
        raise ValueError(f"Unknown attack labels: {unknown}")

    return True


def prepare_features_target(df):
    """Separate features and target."""

    X = df[FEATURE_COLUMNS].copy()
    y = df[TARGET_COLUMN].copy()

    return X, y


def prepare_dataset(df):
    """Prepare dataset for the next pipeline stage."""

    df = map_attack_labels(df)

    validate_attack_labels(df)

    X, y = prepare_features_target(df)

    return X, y
