"""File utility functions with robust error handling."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


def read_file_content(filepath: str) -> Optional[str]:
    """
    Reads the content of a file as a string.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        Optional[str]: The content of the file as a string, or None if an unexpected error occurs.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user does not have permissions to read the file.
        IsADirectoryError: If the filepath points to a directory instead of a file.
        UnicodeDecodeError: If the file is not UTF-8 encoded or contains invalid characters.
    """
    try:
        logger.info("Attempting to read file: %s", filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info("Successfully read file: %s", filepath)
        return content

    except FileNotFoundError:
        logger.error("File not found: %s", filepath)
        raise  # Re-raise the FileNotFoundError to allow the caller to handle it appropriately.

    except PermissionError:
        logger.error("Permission denied for file: %s", filepath)
        raise  # Re-raise the PermissionError for the caller to handle.

    except IsADirectoryError:
        logger.error("Expected a file but found a directory: %s", filepath)
        raise  # Re-raise the error to indicate incorrect usage.

    except UnicodeDecodeError:
        logger.error(
            "File at %s is not UTF-8 encoded or contains invalid characters.", filepath
        )
        # Re-raise or handle according to your application's needs.
        raise

    except Exception as e:
        logger.exception(
            "An unexpected error occurred while reading the file at %s: %s",
            filepath,
            str(e),
        )
        return None  # Return None as a fallback.
