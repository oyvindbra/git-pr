# git-pr

## Prerequisites

* Azure CLI
* Github CLI

## Using the application

### First run

  # Check if all dependencies are installed
  python git-pr.py bootstrap

  # Get more help
  python git-pr.py --help

## Contributing

### Bootstrapping development environment

  python3 -m venv env
  # Enter virtualenv
  source env/bin/activate
  # Install prerequisites
  pip install -r requirements.txt

### Running tests

  # Run unit tests for python
  python3 -m unittest git-pr.py -v

### Code coverage report

*note: Also runs the tests automatically*

  # Run coverage scan
  coverage run -m unittest git-pr.py -v

  # Show report with missing lines
  coverage report -m

### Coding conventions

  # Check code conventions
  pycodestyle git-pr.py
