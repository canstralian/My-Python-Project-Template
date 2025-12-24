"""Main application entry point with improved error handling."""

import argparse
import logging
import sys
from typing import NoReturn

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def sample_function(name: str) -> str:
    """
    Sample function to demonstrate modularity.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.

    Raises:
        ValueError: If the name is empty or contains only whitespace.
        TypeError: If the name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected string for name, got {type(name).__name__}")

    if not name or name.isspace():
        raise ValueError("Name cannot be empty or contain only whitespace")

    return f"Hello, {name}! Welcome to the template repository."


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing the name parameter.
    """
    parser = argparse.ArgumentParser(description="Template Python Application")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    return parser.parse_args()


def main() -> NoReturn:
    """
    Main function to run the script.

    Raises:
        SystemExit: Always exits with status 0 on success or 1 on error.
    """
    try:
        args = parse_args()
        message = sample_function(args.name)
        logger.info(message)
        sys.exit(0)

    except ValueError as e:
        logger.error("Invalid input value: %s", str(e))
        sys.exit(1)

    except TypeError as e:
        logger.error("Type error: %s", str(e))
        sys.exit(1)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        sys.exit(0)

    except Exception as e:
        logger.exception("An unexpected error occurred: %s", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
