"""Pytest configuration and fixtures for test suite."""

import sys
from pathlib import Path

import pytest

# Add src directory to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture(autouse=True)
def reset_logging():
    """Reset logging configuration for each test."""
    import logging

    # Clear all handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Reset to default configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )

    yield

    # Cleanup after test
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
