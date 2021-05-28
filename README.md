# git-pr

##

## Testing 

  # Run unit tests for python
  python3 -m unittest git-pr.py -v

## Code coverage

*note: Also runs the tests automatically*

  # Run coverage scan
  coverage run -m unittest git-pr.py -v

  # Show report with missing lines
  coverage report -m
