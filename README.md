# MD Table Creator

Python 3.8.3

Takes in a mysql create table syntax as an input and output markdown table which you can then paste into confluence.

3.8.2 is used for the walrus operator

# Contributing

## Setup

Create a virtualenv, example with `pyenv` and `pyenv-virtualenv` plugin:

    pyenv install 3.8.2
    pyenv virtualenv 3.8.2 md-table-creator
    pyenv local md-table-creator # Automatically activates md-table-creator whenever you are in this folder
    pip install -r requirements.txt
    pre-commit install

## Running Tests

    pytest .
    pytest -vv . # verbose mode

Or if you want tests to re-run when any file is changed:

    ptw .
    ptw . -- -vv # verbose mode

## Running formatter

    black .

# Building

Installed pyinstaller and ran:

    pyinstaller --onefile --console md_table_creator.py

Then copied the executable from the dist folder to the runnable folder:

    cp dist/md_table_creator runnable/md_table_creator

# Uploading as a library to pypy

Followed these instructions:

https://dzone.com/articles/executable-package-pip-install

    rm -rf build dist # clear as folders conflict with pyinstaler
    python setup.py bdist_wheel # compile
    python -m twine upload dist/* # upload to pypy

# Versioning

Using semantic versioning
