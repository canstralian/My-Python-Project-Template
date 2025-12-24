"""Tests for file utility functions."""

import logging
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from my_project.file_utils import read_file_content


class TestReadFileContent:
    """Test suite for read_file_content function."""

    def test_read_file_success(self, tmp_path):
        """Test successful file reading."""
        test_file = tmp_path / "test.txt"
        test_content = "Hello, World!"
        test_file.write_text(test_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == test_content

    def test_read_file_with_unicode(self, tmp_path):
        """Test reading file with unicode characters."""
        test_file = tmp_path / "unicode.txt"
        test_content = "Hello, 世界! 🌍"
        test_file.write_text(test_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == test_content

    def test_read_file_multiline(self, tmp_path):
        """Test reading multiline file."""
        test_file = tmp_path / "multiline.txt"
        test_content = "Line 1\nLine 2\nLine 3"
        test_file.write_text(test_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == test_content

    def test_read_empty_file(self, tmp_path):
        """Test reading an empty file."""
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == ""

    def test_file_not_found(self):
        """Test FileNotFoundError is raised for non-existent file."""
        with pytest.raises(FileNotFoundError):
            read_file_content("/nonexistent/path/to/file.txt")

    @pytest.mark.skipif(
        os.getuid() == 0, reason="Skipping permission test when running as root"
    )
    def test_permission_error(self, tmp_path):
        """Test PermissionError is raised for files without read permissions."""
        test_file = tmp_path / "no_permission.txt"
        test_file.write_text("test content", encoding="utf-8")

        # Remove read permissions
        os.chmod(test_file, 0o000)

        try:
            with pytest.raises(PermissionError):
                read_file_content(str(test_file))
        finally:
            # Restore permissions for cleanup
            os.chmod(test_file, 0o644)

    def test_is_directory_error(self, tmp_path):
        """Test IsADirectoryError is raised when filepath is a directory."""
        test_dir = tmp_path / "test_directory"
        test_dir.mkdir()

        with pytest.raises(IsADirectoryError):
            read_file_content(str(test_dir))

    def test_unicode_decode_error(self, tmp_path):
        """Test UnicodeDecodeError is raised for non-UTF-8 files."""
        test_file = tmp_path / "binary.txt"
        # Write binary content that's not valid UTF-8
        test_file.write_bytes(b"\x80\x81\x82\x83")

        with pytest.raises(UnicodeDecodeError):
            read_file_content(str(test_file))

    def test_logging_on_success(self, tmp_path, caplog):
        """Test that success is logged appropriately."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content", encoding="utf-8")

        with caplog.at_level(logging.INFO):
            read_file_content(str(test_file))

        assert "Attempting to read file" in caplog.text
        assert "Successfully read file" in caplog.text

    def test_logging_on_file_not_found(self, caplog):
        """Test that FileNotFoundError is logged."""
        with caplog.at_level(logging.ERROR):
            with pytest.raises(FileNotFoundError):
                read_file_content("/nonexistent/file.txt")

        assert "File not found" in caplog.text

    @pytest.mark.skipif(
        os.getuid() == 0, reason="Skipping permission test when running as root"
    )
    def test_logging_on_permission_error(self, tmp_path, caplog):
        """Test that PermissionError is logged."""
        test_file = tmp_path / "no_permission.txt"
        test_file.write_text("test", encoding="utf-8")
        os.chmod(test_file, 0o000)

        try:
            with caplog.at_level(logging.ERROR):
                with pytest.raises(PermissionError):
                    read_file_content(str(test_file))

            assert "Permission denied" in caplog.text
        finally:
            os.chmod(test_file, 0o644)

    def test_logging_on_directory_error(self, tmp_path, caplog):
        """Test that IsADirectoryError is logged."""
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()

        with caplog.at_level(logging.ERROR):
            with pytest.raises(IsADirectoryError):
                read_file_content(str(test_dir))

        assert "Expected a file but found a directory" in caplog.text

    def test_unexpected_error_returns_none(self, tmp_path, monkeypatch):
        """Test that unexpected errors are handled gracefully."""

        def mock_open(*args, **kwargs):
            raise RuntimeError("Unexpected error")

        with patch("builtins.open", side_effect=mock_open):
            result = read_file_content("any_file.txt")
            assert result is None

    def test_large_file(self, tmp_path):
        """Test reading a large file."""
        test_file = tmp_path / "large.txt"
        # Create a file with ~1MB of content
        large_content = "x" * 1_000_000
        test_file.write_text(large_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == large_content
        assert len(result) == 1_000_000

    def test_special_characters(self, tmp_path):
        """Test reading file with special characters."""
        test_file = tmp_path / "special.txt"
        test_content = "Test with special chars: !@#$%^&*()_+-=[]{}|;:,.<>?"
        test_file.write_text(test_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == test_content

    def test_whitespace_content(self, tmp_path):
        """Test reading file with only whitespace."""
        test_file = tmp_path / "whitespace.txt"
        test_content = "   \n\t\t\n   "
        test_file.write_text(test_content, encoding="utf-8")

        result = read_file_content(str(test_file))
        assert result == test_content
