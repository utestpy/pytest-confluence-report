import shutil
from pathlib import Path
from typing import IO
import pytest
from setup import _Package

_INIT_CONTENT = '''
"""Package stands for pytest plugin."""

__author__: str = 'Volodymyr Yahello'
__email__: str = 'vyahello@gmail.com'
__license__: str = 'MIT'
__version__: str = '0.0.0'
__package_name__: str = 'pytest-confluence-report'
'''


@pytest.fixture()
def package() -> _Package:
    """Returns a test package."""
    report: Path = Path('test-report')
    if not report.exists():
        report.mkdir()
    with (report / '__init__.py').open(mode='w') as init:  # type: IO[str]
        init.write(_INIT_CONTENT)
    yield _Package(path=report)
    shutil.rmtree(path=report)


def test_package_version(package: _Package) -> None:
    assert package.version == '0.0.0', 'Package version is wrong'


def test_package_name(package: _Package) -> None:
    assert package.name == 'pytest-confluence-report', 'Package name is wrong'


def test_package_author(package: _Package) -> None:
    assert package.author == 'Volodymyr Yahello', 'Package author is wrong'


def test_package_email(package: _Package) -> None:
    assert package.email == 'vyahello@gmail.com', 'Package email is wrong'


def test_package_license(package: _Package) -> None:
    assert package.license_ == 'MIT', 'Package license is wrong'


def test_package_goal(package: _Package) -> None:
    assert (
        package.goal == 'Package stands for pytest plugin.'
    ), 'Package goal is wrong'


def test_package_read_property(package: _Package) -> None:
    assert (
        package._read(pattern=r"(?<=__license__: str = ')[\w-]+") == 'MIT'
    ), 'Package property is wrong'
