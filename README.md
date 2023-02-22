# My Module

Intro

## <a name="overview">Overview</a>
Description


## <a name="requirements">Requirements</a>

This project has been developed using Python 3.10 and Poetry. 
So, `Python 3` and `pip3` are required.

Dependencies are managed through the tool poetry that you can install as follows

*Note: you need at least this versions to be able to use depencies groups inside pyproject.toml*

```
pip install "poetry"
```

When you use poetry, you can use all the commans listed in this files following the pattern
```
poetry run [tool/programa/aplication]
```
If you run the commands using poetry, it will create a virtualenvironment that poetry will manage trasnparently. But the commands in this file are written taking into account that you are already using virtualenv or conda environments, so poetry doesn't need to create a managed virtualenvironment when it's run inside one of this. Then you can run the commands inside this file without the need to write `poetry run`




## <a name="hooks">Pre-commit hooks</a>

This project uses pre-commit hooks to check code quality and format before it s finally committed to the repository. To configure the pre-commit hooks to evaluate your code, follow this steps:

1. Install pre-commit utility: `pip install pre-commit`
2. Run inside the root directory the following command: `pre-commit install`
3. Done

After this setup, black and flake should run before each commit command

```
git commit -m "example commit"
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
black....................................................................Passed
flake8...................................................................Passed
[master 12a838b] example commit
```

If you don't follow the style guide, this tools will show warning and they will abort your commit

```
git commit -m "example commit"
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted example_package/common/infraestructure/timescale_engine.py

All done! ✨ 🍰 ✨
1 file reformatted, 3 files left unchanged.

flake8...................................................................Failed
- hook id: flake8
- exit code: 1

example_package/cli.py:12:80: E501 line too long (88 > 79 characters)
example_package/common/infraestructure/timescale_engine.py:10:80: E501 line too long (88 > 79 characters)

```

## <a name="installation">Installation</a>

The Python version used is Python 3.10.

All the other required python packages may be installed using the command:

```bash
poetry install
```

A new requirement must be added using the command `poetry add dependency` or editing de file `pyproject.toml` file.

## <a name="configuration">Configuration</a> 

All the configuration variables are included on **.env** files. For 
further information read the [related documentation](https://pypi.org/project/python-dotenv/). An example **.env** file is provided `.env.example` you can use it as a base **.env** file if you rename it to `.env`



## <a name="tests">Tests</a>

```bash
# All tests
PYTHONPATH=. pytest ./src/tests

# All tests verbose mode (not encouraged use logging module instead)
PYTHONPATH=. pytest -s --log-cli-level=INFO

# Unit tests
PYTHONPATH=. pytest -s --log-cli-level=INFO src/tests/unit

# Integration tests
PYTHONPATH=. pytest -s --log-cli-level=INFO src/tests/integration

# Validation tests
PYTHONPATH=. pytest -s --log-cli-level=INFO src/tests/validation
```

## <a name="run">Run</a>

To run the command line without installing it, use the following command: `python3 -m src.cli --help`

## Scaffolding

- **src**: contiene el desarrollo realizado
- **.github/workflows**: contiene los tareas de CI/CD definidas por Gradiant durante la realización del proyecto
- **tools**: herramienta y utilidades de cara a ejecutar el servicio
