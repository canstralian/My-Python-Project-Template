"""Tests for main application module."""

import logging
import sys
from unittest.mock import patch

import pytest

from my_project.main import main, parse_args, sample_function


class TestSampleFunction:
    """Test suite for sample_function."""

    def test_sample_function_basic(self):
        """Test basic greeting functionality."""
        result = sample_function("Alice")
        assert result == "Hello, Alice! Welcome to the template repository."

    def test_sample_function_world(self):
        """Test default greeting with 'World'."""
        result = sample_function("World")
        assert result == "Hello, World! Welcome to the template repository."

    def test_sample_function_unicode(self):
        """Test with unicode characters."""
        result = sample_function("世界")
        assert "世界" in result
        assert "Hello, 世界!" in result

    def test_sample_function_special_characters(self):
        """Test with special characters."""
        result = sample_function("@User!")
        assert "Hello, @User!" in result

    def test_sample_function_long_name(self):
        """Test with extremely long name."""
        long_name = "x" * 1000
        result = sample_function(long_name)
        assert long_name in result

    def test_sample_function_empty_string_raises_error(self):
        """Test that empty string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            sample_function("")

    def test_sample_function_whitespace_raises_error(self):
        """Test that whitespace-only string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            sample_function("   ")

    def test_sample_function_tabs_raises_error(self):
        """Test that tab-only string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            sample_function("\t\t")

    def test_sample_function_newlines_raises_error(self):
        """Test that newline-only string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            sample_function("\n\n")

    def test_sample_function_wrong_type_raises_error(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Expected string"):
            sample_function(123)

    def test_sample_function_none_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Expected string"):
            sample_function(None)

    def test_sample_function_list_raises_error(self):
        """Test that list input raises TypeError."""
        with pytest.raises(TypeError, match="Expected string"):
            sample_function(["Alice"])


class TestParseArgs:
    """Test suite for parse_args function."""

    def test_parse_args_default(self):
        """Test default argument value."""
        with patch("sys.argv", ["main.py"]):
            args = parse_args()
            assert args.name == "World"

    def test_parse_args_custom_name(self):
        """Test custom name argument."""
        with patch("sys.argv", ["main.py", "--name", "TestUser"]):
            args = parse_args()
            assert args.name == "TestUser"

    def test_parse_args_custom_name_with_spaces(self):
        """Test custom name with spaces."""
        with patch("sys.argv", ["main.py", "--name", "John Doe"]):
            args = parse_args()
            assert args.name == "John Doe"

    def test_parse_args_help_exits(self):
        """Test that --help causes SystemExit."""
        with patch("sys.argv", ["main.py", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                parse_args()
            assert exc_info.value.code == 0

    def test_parse_args_unicode_name(self):
        """Test unicode name argument."""
        with patch("sys.argv", ["main.py", "--name", "世界"]):
            args = parse_args()
            assert args.name == "世界"

    def test_parse_args_special_characters(self):
        """Test name with special characters."""
        with patch("sys.argv", ["main.py", "--name", "@User#123!"]):
            args = parse_args()
            assert args.name == "@User#123!"


class TestMain:
    """Test suite for main function."""

    def test_main_success_default(self, caplog):
        """Test successful main execution with default arguments."""
        with patch("sys.argv", ["main.py"]):
            with caplog.at_level(logging.INFO):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0
                assert "Hello, World!" in caplog.text

    def test_main_success_custom_name(self, caplog):
        """Test successful main execution with custom name."""
        with patch("sys.argv", ["main.py", "--name", "Alice"]):
            with caplog.at_level(logging.INFO):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0
                assert "Hello, Alice!" in caplog.text

    def test_main_empty_name_error(self, caplog):
        """Test main with empty name triggers ValueError handling."""
        with patch("sys.argv", ["main.py", "--name", ""]):
            with caplog.at_level(logging.ERROR):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 1
                assert "Invalid input value" in caplog.text

    def test_main_whitespace_name_error(self, caplog):
        """Test main with whitespace-only name triggers ValueError handling."""
        with patch("sys.argv", ["main.py", "--name", "   "]):
            with caplog.at_level(logging.ERROR):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 1
                assert "Invalid input value" in caplog.text

    def test_main_keyboard_interrupt(self, caplog):
        """Test main handles KeyboardInterrupt gracefully."""
        with patch("sys.argv", ["main.py"]):
            with patch(
                "my_project.main.sample_function", side_effect=KeyboardInterrupt
            ):
                with caplog.at_level(logging.INFO):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 0
                    assert "cancelled by user" in caplog.text

    def test_main_unexpected_error(self, caplog):
        """Test main handles unexpected errors."""
        with patch("sys.argv", ["main.py"]):
            with patch(
                "my_project.main.sample_function",
                side_effect=RuntimeError("Unexpected error"),
            ):
                with caplog.at_level(logging.ERROR):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 1
                    assert "unexpected error occurred" in caplog.text

    def test_main_unicode_input(self, caplog):
        """Test main with unicode input."""
        with patch("sys.argv", ["main.py", "--name", "世界"]):
            with caplog.at_level(logging.INFO):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0
                assert "世界" in caplog.text

    def test_main_long_input(self, caplog):
        """Test main with very long input."""
        long_name = "x" * 1000
        with patch("sys.argv", ["main.py", "--name", long_name]):
            with caplog.at_level(logging.INFO):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0

    def test_main_special_characters(self, caplog):
        """Test main with special characters in input."""
        with patch("sys.argv", ["main.py", "--name", "@User#123!"]):
            with caplog.at_level(logging.INFO):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 0
                assert "@User#123!" in caplog.text
