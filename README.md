My-Python-Project-Template

A batteries-included Python project template with a clean src/ layout, Poetry dependency management, and GitHub Actions CI—so you can start building immediately.

What you get
	•	Pre-configured tooling: formatting, testing, and CI defaults.
	•	Poetry workflow: dependency management + virtual environments.
	•	CI-ready: GitHub Actions workflow wired up out of the box.

Table of Contents
	•	Quickstart￼
	•	Customize this template￼
	•	Usage￼
	•	Developer commands￼
	•	Contributing￼
	•	License￼
	•	Contact￼

Quickstart

1) Clone

git clone https://github.com/canstralian/My-Python-Project-Template.git
cd My-Python-Project-Template

2) Install dependencies (Poetry)

Install Poetry if you don’t have it yet (see Poetry docs), then:

poetry install

3) Run tests

poetry run pytest

4) Run the app

poetry run python src/my_project/main.py

Customize this template

This repo ships with placeholder names. You’ll want to rename them once, early.

Rename the package/module

Find and replace these placeholders:
	•	Import/package name: my_project
	•	Example module: my_module
	•	Example function: my_function
	•	PyPI package name (badge + publish name): my-python-package

Typical rename steps:
	1.	Rename the source package directory:
	•	src/my_project/ → src/<your_package_name>/
	2.	Update imports in code/tests:
	•	from my_project ... → from <your_package_name> ...
	3.	Update command examples in this README:
	•	python src/my_project/main.py → python src/<your_package_name>/main.py
	4.	Update badges/links:
	•	badge.fury.io/py/my-python-package.svg
	•	pypi.org/project/my-python-package/

Update project metadata

In pyproject.toml, update at least:
	•	name (PyPI name)
	•	version
	•	description
	•	authors
	•	license
	•	readme
	•	repository/homepage URLs (if present)

(Optional) Make it a CLI

If you want poetry run <command> style execution, add a console script entry in pyproject.toml (under [tool.poetry.scripts]) pointing to your main function.

Usage

Running the application

poetry run python src/my_project/main.py

Using the library

from my_project import my_module

result = my_module.my_function(some_argument)
print(result)

Running tests

poetry run pytest

Developer commands

Common commands you’ll use while developing:

Install / update deps

poetry install
poetry update

Add dependencies

poetry add <package>
poetry add --group dev <package>

Run formatting (Black)

poetry run black .

Run tests (Pytest)

poetry run pytest

Run a single test file

poetry run pytest tests/test_example.py

Run the project in an activated shell (optional)

poetry shell
python src/my_project/main.py

Contributing
	1.	Fork the repo
	2.	Create a branch:

git checkout -b feature/your-feature-name


	3.	Make changes and ensure checks pass:

poetry run black .
poetry run pytest


	4.	Commit and push:

git commit -m "Describe your change"
git push origin feature/your-feature-name


	5.	Open a Pull Request

License

MIT License. See LICENSE￼.

Contact

Add a contact method here (e.g., GitHub Issues, email, or a handle).
