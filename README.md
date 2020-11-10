![Screenshot](media/logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/pytest-confluence-report.svg?branch=master)](https://travis-ci.org/vyahello/pytest-confluence-report)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/pytest-confluence-report/badge.svg?branch=master)](https://coveralls.io/github/vyahello/pytest-confluence-report?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with interrogate](https://img.shields.io/badge/interrogate-checked-yellowgreen)](https://interrogate.readthedocs.io/en/latest/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Docs](https://img.shields.io/badge/docs-github-orange)](https://vyahello.github.io/pytest-confluence-report/)

# Pytest confluence report

> Pytest plugin to convert test results into confluence page report to proceed with tests analysis.
> 
> ⚠️  **Note:** the project is under construction.

## Tools

### Production

- python 3.6, 3.7, 3.8
- [typer](https://typer.tiangolo.com/)
- [loguru](https://loguru.readthedocs.io/en/stable/index.html)
- [pytest](https://pypi.org/project/pytest/)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)
- [interrogate](https://interrogate.readthedocs.io/en/latest/)
- [bats](https://github.com/sstephenson/bats)

## Usage

![Usage](media/usage.gif)

### Installation

```bash
pip install pytest-confluence-report
✨ 🍰 ✨
```

### Quick start

> Please make sure your [settings.yml](settings.yml) file is properly configured before execution.

```bash
pytest --junit-xml=pytest.xml --confluence-upload
```

### Source code

```bash
git clone git@github.com:vyahello/pytest-confluence-report.git
pip install -e .
```

Or using direct release:
```bash
pip install git+https://github.com/vyahello/pytest-confluence-report@0.0.2
```

### Local debug

```bash
git clone git@github.com:vyahello/pytest-confluence-report.git
python -m report --settings settings.yml --xml-path pytest.xml
```

**[⬆ back to top](#pytest-confluence-report)**

## Development notes

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

In addition, package unit tests are implemented with [bats](https://github.com/sstephenson/bats) framework:
> `PACKAGE_NAME` and `PACKAGE_VERSION` environment variables should be set to run tests.

```bash
bats --pretty test-package.bats
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle` and `interrogate`) and unittests (`pytest`, `bats`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/pytest-confluence-report/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pytest-confluence-report)**
