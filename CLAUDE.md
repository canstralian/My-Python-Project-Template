# CLAUDE.md - AI Assistant Guide for My-Python-Project-Template

**Last Updated**: 2025-12-24
**Repository**: canstralian/My-Python-Project-Template
**Purpose**: Batteries-included Python project template with clean src/ layout, Poetry dependency management, and GitHub Actions CI

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Development Environment](#development-environment)
4. [Code Conventions](#code-conventions)
5. [Testing Strategy](#testing-strategy)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Key Workflows](#key-workflows)
8. [Dependencies](#dependencies)
9. [Git Conventions](#git-conventions)
10. [AI Assistant Guidelines](#ai-assistant-guidelines)

---

## Project Overview

### What is This Repository?

This is a **production-ready Python project template** designed to eliminate setup friction and provide a clean, standardized foundation for Python projects. It's NOT just a skeleton—it's a complete development environment with:

- Pre-configured tooling (formatting, testing, CI)
- Poetry workflow for dependency management
- CI-ready GitHub Actions setup
- Clean src/ layout following Python best practices

### Key Value Proposition

**"Green CI on the first push"** - From empty repo → authenticated, tested, documented Python project with no setup drift.

### Project Goals

1. **Immediate productivity**: Start building features, not configuring tooling
2. **Standardization**: Consistent project structure across Python projects
3. **CI/CD ready**: GitHub Actions wired up out of the box
4. **Best practices**: Type hints, logging, argparse, clean architecture

### Target Use Cases

- Internal tools and APIs requiring fast setup
- Educational projects and templates
- Microservices and CLI applications
- Data science projects (includes transformers, datasets, huggingface_hub)

---

## Repository Structure

### Current Directory Layout

```
My-Python-Project-Template/
├── .github/
│   ├── workflows/          # GitHub Actions CI/CD pipelines
│   │   ├── ci.yml          # Main CI pipeline (Black, pytest)
│   │   ├── python-app.yml  # Alternative CI with flake8
│   │   ├── code-review.yml # AI-powered code review (Llama-2)
│   │   ├── huggingface-sync.yml  # Sync to Hugging Face Spaces
│   │   ├── greetings.yml   # First-time contributor greetings
│   │   ├── stale.yml       # Stale issue management
│   │   ├── label-sponsors.yml  # Sponsor labeling
│   │   └── setup-python.yml    # Python setup configuration
│   ├── ISSUE_TEMPLATE/     # GitHub issue templates
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── dependabot.yml      # Dependabot configuration (weekly pip updates)
│   ├── labeler.yml         # Auto-labeling configuration
│   └── FUNDING.yml         # GitHub Sponsors configuration
├── main.py                 # Entry point with CLI argument parsing
├── pyproject.toml          # Poetry configuration and project metadata
├── requirements.txt        # Pip dependencies (transformers, datasets, black, huggingface_hub)
├── tox.ini                 # Tox configuration for multi-environment testing
├── .gitignore              # Python-specific gitignore (comprehensive)
├── LICENSE                 # MIT License
├── README.md               # User-facing documentation
├── TEST_COVERAGE_ANALYSIS.md  # Detailed test coverage analysis
└── CLAUDE.md               # This file (AI assistant guide)
```

### Notable Absence: src/ Directory

**IMPORTANT**: Despite being advertised as having a "src/ layout", the repository currently has:
- **NO src/ directory**
- **NO test/ directory**
- Only `main.py` in the root directory

This is a **template contradiction** that should be addressed when using this template:

1. **Option A (Recommended)**: Create `src/my_project/` structure and move `main.py` into it
2. **Option B**: Update documentation to reflect flat layout
3. **Option C**: Treat this as a minimal starting point and evolve structure as needed

---

## Development Environment

### Prerequisites

- **Python**: 3.9+ (3.10 recommended for CI compatibility)
- **Poetry**: Latest version (for dependency management)
- **Git**: For version control

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/canstralian/My-Python-Project-Template.git
cd My-Python-Project-Template

# Install dependencies with Poetry
poetry install

# Run the application
poetry run python main.py

# Run tests (when they exist)
poetry run pytest
```

### Virtual Environment Management

Poetry automatically manages virtual environments:

```bash
# Activate Poetry shell
poetry shell

# Run Python scripts in the environment
python main.py

# Exit the shell
exit
```

### Tools and Technologies

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Poetry** | Dependency management | `pyproject.toml` |
| **Black** | Code formatting | `pyproject.toml` (line-length: 88) |
| **Pytest** | Testing framework | `pyproject.toml` (recommended) |
| **Tox** | Multi-environment testing | `tox.ini` (py38, py39, lint) |
| **Flake8** | Linting (alternative) | Used in `python-app.yml` |
| **Pylint** | Linting | `tox.ini` (tox -e lint) |

---

## Code Conventions

### Python Style Guide

- **Formatter**: Black (line length: 88)
- **Target**: Python 3.10+
- **Type Hints**: Encouraged (see `main.py` examples)
- **Docstrings**: Google-style (see `sample_function` in `main.py`)

### Code Quality Standards

1. **Type Annotations**: Use type hints for function signatures
   ```python
   def sample_function(name: str) -> str:
       """Sample function with type hints."""
       return f"Hello, {name}!"
   ```

2. **Logging**: Use Python's `logging` module (configured in `main.py`)
   ```python
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(levelname)s - %(message)s'
   )
   ```

3. **CLI Arguments**: Use `argparse` for command-line interfaces
   ```python
   parser = argparse.ArgumentParser(description="Template Python Application")
   parser.add_argument('--name', type=str, default='World', help='Name to greet')
   ```

4. **Error Handling**: Proper exception handling with logging
   ```python
   try:
       # ... code ...
   except Exception as e:
       logging.error(f"An error occurred: {e}")
       sys.exit(1)
   ```

### Naming Conventions

- **Functions**: `snake_case` (e.g., `sample_function`, `parse_args`)
- **Classes**: `PascalCase` (when needed)
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: Prefix with underscore `_private_function`

### File Organization

**Current Pattern** (single file):
```python
# Imports
import argparse
import logging
import sys

# Configuration
logging.basicConfig(...)

# Functions
def sample_function(...):
    pass

def parse_args():
    pass

def main():
    pass

# Entry point
if __name__ == '__main__':
    main()
```

**Recommended Pattern** (as project grows):
```
src/my_project/
├── __init__.py
├── main.py           # Entry point
├── cli.py            # CLI argument parsing
├── core.py           # Core business logic
└── utils.py          # Utility functions

tests/
├── __init__.py
├── test_main.py
├── test_cli.py
└── test_core.py
```

---

## Testing Strategy

### Current State: 0% Coverage

**Critical Issue**: The repository has **NO test files**, resulting in zero test coverage.

See `TEST_COVERAGE_ANALYSIS.md` for detailed analysis, but key points:

- **Total Python Files**: 1 (`main.py`)
- **Total Functions**: 3 (all untested)
- **Test Files**: 0
- **Coverage**: 0%

### Recommended Test Structure

```
tests/
├── __init__.py
├── conftest.py           # Pytest fixtures
├── test_main.py          # Tests for main() function
├── test_sample_function.py  # Tests for sample_function()
└── test_parse_args.py    # Tests for parse_args()
```

### Essential Tests to Implement

1. **sample_function** (`main.py:11-21`)
   - Basic functionality (greeting generation)
   - Input validation (empty strings, special characters)
   - Unicode handling
   - Edge cases (None, extremely long strings)

2. **parse_args** (`main.py:23-32`)
   - Default argument behavior
   - Custom argument parsing
   - Invalid argument handling
   - Help message generation

3. **main** (`main.py:34-46`)
   - Successful execution path
   - Logging output verification
   - Exception handling
   - sys.exit(1) behavior on errors
   - Integration with parse_args and sample_function

### Testing Commands

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=. --cov-report=term-missing

# Run specific test file
poetry run pytest tests/test_main.py

# Run with verbose output
poetry run pytest -v

# Run tests in parallel
poetry run pytest -n auto  # requires pytest-xdist
```

### Coverage Goals

- **Line Coverage**: 90%+
- **Branch Coverage**: 85%+
- **Function Coverage**: 100%

---

## CI/CD Pipeline

### GitHub Actions Workflows

The repository includes **9 GitHub Actions workflows**:

#### 1. **ci.yml** - Main CI Pipeline ✅
- **Trigger**: Push/PR to `main`
- **Steps**:
  1. Checkout code
  2. Setup Python 3.10
  3. Cache pip dependencies
  4. Install dependencies from `requirements.txt`
  5. Lint with Black (`black --check .`)
  6. Run tests with pytest

#### 2. **python-app.yml** - Alternative CI (Flake8)
- **Trigger**: Push/PR to `main`
- **Steps**: Similar to `ci.yml` but uses `flake8` instead of Black

#### 3. **code-review.yml** - AI Code Review
- **Trigger**: Pull requests (excludes `*.md`, `LICENSE`)
- **Features**:
  - Hugging Face login
  - Diff extraction
  - LLM-based code review using Llama-2-7b-chat-hf
  - PR comment generation
- **Secrets Required**: `HF_USERNAME`, `HF_PASSWORD`, `API_KEY`

#### 4. **huggingface-sync.yml** - Hugging Face Sync
- **Trigger**: Push to `main`
- **Purpose**: Sync repo to Hugging Face Space (Gradio)
- **Configuration**:
  - GitHub repo: `canstralian/My-Python-Project-Template`
  - HF repo: `canstralian/my-huggingface-repo`
  - Repo type: `space` (Gradio)
- **Secrets Required**: `HF_TOKEN`

#### 5. **greetings.yml** - First-time Contributor Welcome
- **Trigger**: Issues/PRs
- **Purpose**: Welcome first-time contributors

#### 6. **stale.yml** - Stale Issue Management
- **Trigger**: Scheduled
- **Purpose**: Mark and close stale issues/PRs

#### 7. **label-sponsors.yml** - Sponsor Labeling
- **Trigger**: Issues/PRs
- **Purpose**: Label contributions from sponsors

#### 8. **setup-python.yml** - Python Setup Configuration
- **Purpose**: Reusable Python setup configuration
- **Configuration**:
  - Python version: 3.10
  - Architecture: x64
  - Cache: pip
  - Cache dependency path: `requirements.txt`

#### 9. **pyright-check.yml** (if exists)
- **Purpose**: Type checking with Pyright (not verified)

### CI/CD Best Practices

1. **Caching**: Workflows use `actions/cache@v3` for pip dependencies
2. **Version Pinning**: Python 3.10 specified across all workflows
3. **Parallel Jobs**: Consider splitting lint and test into separate jobs
4. **Security**: Secrets management for Hugging Face and API tokens

### CI/CD Improvements Needed

1. **Coverage Reporting**: Add coverage thresholds and badges
2. **Workflow Consolidation**: `ci.yml` and `python-app.yml` are redundant
3. **Poetry Support**: Workflows use pip, but project uses Poetry
4. **Test Enforcement**: CI passes even with 0% coverage (no tests)

---

## Key Workflows

### Adding Dependencies

```bash
# Add production dependency
poetry add <package>

# Add development dependency
poetry add --group dev <package>

# Update all dependencies
poetry update

# Show installed packages
poetry show
```

### Code Formatting

```bash
# Format all Python files
poetry run black .

# Check formatting without changes
poetry run black --check .

# Format specific file
poetry run black main.py
```

### Running the Application

```bash
# Default behavior (greets "World")
poetry run python main.py

# With custom name argument
poetry run python main.py --name Alice

# View help
poetry run python main.py --help
```

### Tox Multi-Environment Testing

```bash
# Run all tox environments
tox

# Run specific environment
tox -e py39

# Run linting only
tox -e lint

# Recreate environments
tox -r
```

### Git Workflows

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes, format code
poetry run black .

# Run tests (when they exist)
poetry run pytest

# Commit with descriptive message
git commit -m "Add feature: description"

# Push to remote
git push origin feature/your-feature-name

# Open Pull Request on GitHub
```

---

## Dependencies

### Production Dependencies (requirements.txt)

```
transformers>=4.48.0    # Hugging Face Transformers library
datasets==4.4.2         # Hugging Face Datasets library
black==25.11.0          # Code formatter
huggingface_hub==1.2.3  # Hugging Face Hub API
```

**Note**: Versions recently updated by Dependabot (see git history)

### Development Dependencies (Poetry)

Defined in `pyproject.toml`:

```toml
[tool.poetry.dev-dependencies]
pytest = "^6.2"
```

**Recommended Additional Dev Dependencies**:
```bash
poetry add --group dev pytest-cov pytest-mock pytest-xdist
poetry add --group dev mypy pylint flake8
```

### Poetry vs. Requirements.txt

**Inconsistency Alert**: The repository uses BOTH:
- `pyproject.toml` (Poetry) - Lists `requests ^2.26`, `pytest ^6.2`
- `requirements.txt` (pip) - Lists `transformers`, `datasets`, `black`, `huggingface_hub`

**These are NOT synchronized!**

**Recommendation for AI Assistants**:
1. **Use Poetry as source of truth**: `pyproject.toml`
2. **Generate requirements.txt** from Poetry: `poetry export -f requirements.txt --output requirements.txt`
3. **Update both** when adding dependencies

### Dependency Management Commands

```bash
# Install from pyproject.toml
poetry install

# Export to requirements.txt
poetry export -f requirements.txt --output requirements.txt --without-hashes

# Export with dev dependencies
poetry export -f requirements.txt --output requirements-dev.txt --with dev --without-hashes

# Update lock file
poetry lock

# Show outdated packages
poetry show --outdated
```

---

## Git Conventions

### Branch Naming

- **Feature branches**: `feature/<description>`
- **Bug fixes**: `fix/<description>`
- **Claude AI branches**: `claude/<task>-<session-id>`
- **Main branch**: `main` (NOT `master`)

### Commit Message Style

Based on git history analysis:

```
Update README.md
Bump <package> from <old-version> to <new-version>
Revert merge commit <hash>
Add <feature>: <description>
Fix <bug>: <description>
```

**Recommended Format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

Examples:
```
feat(cli): add support for JSON output format
fix(main): handle None input in sample_function
docs(readme): update installation instructions
test(main): add unit tests for parse_args
ci(github): add coverage reporting to workflow
```

### Pull Request Workflow

1. **Create branch** from `main`
2. **Make changes** and commit
3. **Ensure CI passes** (Black, pytest)
4. **Open PR** against `main`
5. **AI code review** runs automatically (`code-review.yml`)
6. **Address feedback** and merge

### Protected Branches

- **main**: Should require PR reviews and passing CI

---

## AI Assistant Guidelines

### When Working with This Repository

#### 1. Understand the Template Contradiction

**Critical Awareness**: This template advertises a "src/ layout" but currently has a **flat structure** with only `main.py` in the root. When assisting users:

- **Ask for clarification**: "Would you like to maintain the flat structure or migrate to src/ layout?"
- **Respect user choice**: Don't force src/ layout if they prefer flat
- **Be consistent**: Once a choice is made, follow it throughout

#### 2. Testing is Priority Zero

The repository has **0% test coverage**. When making ANY code changes:

1. **Create tests FIRST** (TDD approach)
2. **Never ship untested code**
3. **Use TEST_COVERAGE_ANALYSIS.md** as a guide
4. **Aim for 90%+ coverage**

Example workflow:
```bash
# 1. Create test file
touch tests/test_new_feature.py

# 2. Write failing test
# (write test code)

# 3. Run test (should fail)
poetry run pytest tests/test_new_feature.py

# 4. Implement feature
# (write implementation)

# 5. Run test (should pass)
poetry run pytest tests/test_new_feature.py

# 6. Check coverage
poetry run pytest --cov=. --cov-report=term-missing
```

#### 3. Dependency Management Protocol

**Always use Poetry as primary tool**:

# Add dependency and ensure lock file is updated
poetry add <package>

# Update requirements.txt for CI compatibility
poetry export -f requirements.txt --output requirements.txt --without-hashes

# Commit all relevant files to ensure consistency
git add pyproject.toml poetry.lock requirements.txt
git commit -m "chore(deps): add <package>"

#### 4. Code Style Enforcement

**Before ANY commit**:

```bash
# Format code
poetry run black .

# Verify formatting
poetry run black --check .

# Run tests
poetry run pytest

# Verify all checks pass
git commit -m "..."
```

#### 5. Documentation Updates

When changing functionality, update:

1. **CLAUDE.md** (this file) - For architectural changes
2. **README.md** - For user-facing changes
3. **Docstrings** - For function/class changes
4. **Type hints** - Always include type annotations

#### 6. CI/CD Awareness

**Know that CI will run**:
- Black formatting check
- Pytest (will pass even with no tests - **this is a bug**)
- AI code review on PRs
- Hugging Face sync on main branch

**Ensure your changes**:
- Pass Black formatting
- Include tests
- Don't break existing functionality

#### 7. File Modification Guidelines

**Read before writing**:
```python
# ALWAYS read existing files first
with open('main.py', 'r') as f:
    existing_code = f.read()

# Understand context, then modify
# Use Edit tool, not Write tool, for existing files
```

**Preserve structure**:
- Don't reformat entire files
- Maintain existing patterns
- Keep imports organized
- Preserve logging configuration

#### 8. Error Handling Standards

All functions should follow this pattern:

```python
def your_function(arg: str) -> ReturnType:
    """
    Function description.

    Args:
        arg: Description

    Returns:
        Description

    Raises:
        ValueError: When...
    """
    try:
        # Implementation
        result = process(arg)
        logging.info(f"Successfully processed: {arg}")
        return result
    except SpecificException as e:
        logging.error(f"Error in your_function: {e}")
        raise
```

#### 9. Git Workflow for AI Assistants

**Current branch**: `claude/add-claude-documentation-b1pCU`

**Standard workflow**:
```bash
# 1. Ensure you're on the correct branch
git branch --show-current

# 2. Make changes
# (edit files)

# 3. Format code
poetry run black .

# 4. Run tests
poetry run pytest  # (when tests exist)

# 5. Stage changes
git add <files>

# 6. Commit with descriptive message
git commit -m "type(scope): description"

# 7. Push to remote
git push -u origin claude/add-claude-documentation-b1pCU
```

#### 10. Common Pitfalls to Avoid

**DON'T**:
- ❌ Skip reading existing files before editing
- ❌ Create new files when editing existing ones would suffice
- ❌ Add dependencies without updating both Poetry AND requirements.txt
- ❌ Commit code without running Black
- ❌ Ship features without tests
- ❌ Assume src/ structure exists (it doesn't!)
- ❌ Use pip install (use Poetry instead)
- ❌ Modify .github/workflows without understanding the full CI pipeline

**DO**:
- ✅ Read files before editing
- ✅ Use Edit tool for existing files
- ✅ Run Black before committing
- ✅ Write tests for all new code
- ✅ Update documentation when changing functionality
- ✅ Use Poetry for dependency management
- ✅ Ask for clarification when structure is unclear
- ✅ Check CI/CD workflows before making infrastructure changes

#### 11. Hugging Face Integration Awareness

This repository syncs to Hugging Face Spaces:
- **Trigger**: Push to `main`
- **Target**: `canstralian/my-huggingface-repo` (Gradio Space)
- **Implication**: Changes to `main` are automatically deployed

**Be cautious** when:
- Merging to `main`
- Modifying `huggingface-sync.yml`
- Adding dependencies (must work in HF Spaces environment)

#### 12. Question Checklist for AI Assistants

Before starting work, ask:

1. ✅ Have I read all relevant existing files?
2. ✅ Do I understand the current structure (flat vs. src/)?
3. ✅ Am I creating tests for my changes?
4. ✅ Will my changes pass Black formatting?
5. ✅ Am I updating both Poetry and requirements.txt?
6. ✅ Am I on the correct git branch?
7. ✅ Have I updated relevant documentation?
8. ✅ Do I understand the CI/CD implications?

---

## Appendices

### A. Quick Reference Commands

```bash
# Setup
poetry install
poetry shell

# Development
poetry run python main.py --name Alice
poetry run black .
poetry run pytest

# Dependencies
poetry add <package>
poetry update
poetry export -f requirements.txt --output requirements.txt --without-hashes

# Testing
poetry run pytest -v
poetry run pytest --cov=. --cov-report=term-missing

# Multi-environment
tox
tox -e py39
tox -e lint

# Git
git checkout -b feature/my-feature
git add .
git commit -m "feat: add new feature"
git push origin feature/my-feature
```

### B. File Path Reference

| Purpose | Path |
|---------|------|
| Main application | `main.py` |
| Poetry config | `pyproject.toml` |
| Pip dependencies | `requirements.txt` |
| Tox config | `tox.ini` |
| Main CI | `.github/workflows/ci.yml` |
| Code review | `.github/workflows/code-review.yml` |
| HF sync | `.github/workflows/huggingface-sync.yml` |
| Dependabot | `.github/dependabot.yml` |
| Test analysis | `TEST_COVERAGE_ANALYSIS.md` |
| User docs | `README.md` |
| AI guide | `CLAUDE.md` (this file) |

### C. Key Contacts and Resources

- **GitHub Repository**: https://github.com/canstralian/My-Python-Project-Template
- **Hugging Face Space**: canstralian/my-huggingface-repo (Gradio)
- **License**: MIT
- **Python Version**: 3.9+ (3.10 recommended)
- **Main Branch**: `main`

### D. Recent Changes (from Git History)

- `760c8fe` - Update README.md
- `f2dd886` - Update README.md
- `ae2e9d8` - Revert merge commit
- `086b5d4` - Bump huggingface-hub from 0.33.2 to 1.2.3
- `304edd2` - Bump datasets from 2.12.0 to 4.4.2

### E. Known Issues and TODOs

1. **No tests**: 0% coverage (see `TEST_COVERAGE_ANALYSIS.md`)
2. **Structure mismatch**: No src/ directory despite documentation claiming it exists
3. **Dependency mismatch**: `pyproject.toml` and `requirements.txt` are out of sync
4. **Redundant workflows**: `ci.yml` and `python-app.yml` do similar things
5. **Poetry/pip inconsistency**: CI uses pip, but project uses Poetry
6. **No poetry.lock**: Missing lock file for reproducible builds

---

## Conclusion

This template provides a **solid foundation** for Python projects with:
- ✅ Pre-configured CI/CD
- ✅ Code formatting (Black)
- ✅ Dependency management (Poetry)
- ✅ Hugging Face integration
- ✅ AI code review

**Critical gaps** to address:
- ❌ Zero test coverage
- ❌ No src/ structure (despite docs)
- ❌ Dependency management inconsistencies

**For AI Assistants**: Prioritize **testing**, **code quality**, and **consistency** when working with this repository. Always verify the actual structure before making assumptions based on documentation.

---

**Document Version**: 1.0.0
**Created by**: Claude (AI Assistant)
**Date**: 2025-12-24
**Maintained by**: Repository maintainers and AI assistants
