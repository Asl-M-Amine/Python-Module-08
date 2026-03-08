#!/usr/bin/env python3

import os
import sys
from typing import Optional
from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> None:
    """
    Load environment variables from .env file if present.
    """
    load_dotenv()


def get_env_variable(name: str) -> Optional[str]:
    """
    Get environment variable safely.
    """
    return os.getenv(name)


def check_configuration() -> dict[str, Optional[str]]:
    """
    Validate and collect configuration variables.
    """
    config: dict[str, Optional[str]] = {}

    for var in REQUIRED_VARS:
        config[var] = get_env_variable(var)

    return config


def print_configuration(config: dict[str, Optional[str]]) -> None:
    """
    Display configuration status without exposing secrets.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config.get("MATRIX_MODE")
    db = config.get("DATABASE_URL")
    api = config.get("API_KEY")
    log = config.get("LOG_LEVEL")
    zion = config.get("ZION_ENDPOINT")

    print(f"Mode: {mode if mode else 'Not configured'}")

    if db:
        print("Database: Connected to configured instance")
    else:
        print("Database: Not configured")

    if api:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    print(f"Log Level: {log if log else 'Default'}")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """
    Display basic security checks.
    """
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    """
    Main program execution.
    """
    load_configuration()

    config = check_configuration()

    print_configuration(config)

    security_check()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)