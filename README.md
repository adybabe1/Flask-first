# Flask-first
name: Tests
on: push

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.6

      - name: Install tools
        run: |
          python -m pip install --upgrade pip pytest
          pip3 install flask
          pip3 install flask-wtf
          pip3 install flask-sqlalchemy
          pip3 install email-validator

      - name: Test webpages
        run: python3 tests/test_basic.py