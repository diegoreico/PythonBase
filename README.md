# Python Base Project

## Index

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Tests](#tests)
6. [Run](#run)

## <a name="overview">Overview</a>



## <a name="requirements">Requirements</a>

This project has been developed using [Setuptools](https://setuptools.readthedocs.io/en/latest/). 
So, `Python 3.6.9` and `pip3` are required.

## <a name="installation">Installation</a>

All the other required python packages may be installed using the command:

```bash
pip3 install .

# or may be required

pip3 install . --user
```

A new requirement must be added to the `install_requires` property within the `setup.py` file.

## <a name="configuration">Configuration</a> 

All the configuration variables are included on **.env** files. For 
further information read the [related documentation](https://pypi.org/project/python-dotenv/). An example **.env** file is provided `.env.example` you can use it as a base **.env** file if you rename it to `.env`

## <a name="tests">Tests</a>

```bash
# All tests
pytest

# All tests verbose mode (not encouraged use logging module instead)
pytest -s

# Unit tests
pytest etl/tests/unit

# Integration tests
pytest etl/tests/integration

# Validation tests
pytest etl/tests/validation
```

## <a name="run">Run</a>

The package has a command-line entry point configured. This entry point is built using the library 
[Click](https://palletsprojects.com/p/click/). To get all the possible commands, use `package-name --help`.


