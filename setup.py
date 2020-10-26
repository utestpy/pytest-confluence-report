"""Package setup entrypoint."""
import re
import sys
from pathlib import Path
from typing import IO, Sequence
from setuptools import (
    find_packages as __find_packages,
    setup as __compose_package,
)


class __Package:
    """Represents a single package."""

    def __init__(self, path: Path) -> None:
        self._path = path

    @property
    def version(self) -> str:
        """Returns a package version e.g `0.0.1`."""
        return self._read(pattern=r"(?<=__version__: str = ')[\d\.\d\.\d]+")

    @property
    def name(self) -> str:
        """Returns a package name e.g `some-package`."""
        return self._read(
            pattern=r"(?<=__package_name__: str = ')[\w-]+",
        )

    @property
    def author(self) -> str:
        """Returns a package author e.g `some-author`."""
        return self._read(
            pattern=r"(?<=__author__: str = ')[\w-]+",
        )

    @property
    def license_(self) -> str:
        """Returns a package license e.g `MIT`."""
        return self._read(
            pattern=r"(?<=__license__: str = ')[\w-]+",
        )

    @property
    def email(self) -> str:
        """Returns a package email e.g `some-email@com`."""
        return self._read(
            pattern=r"(?<=__email__: str = ')[\w-]+",
        )

    @property
    def goal(self) -> str:
        """Returns a package goal e.g `reporting results`."""
        return self._read(
            pattern=r'(?<=""")[\w\s\.]+',
        )

    def _read(self, pattern: str) -> str:
        """Reads package content.

        :param pattern: <str> a package regular expression pattern.
        """
        return re.findall(
            pattern=pattern, string=(self._path / '__init__.py').open().read()
        )[0]


def __readme() -> str:
    """Returns project description."""
    with open("README.md") as readme:  # type: IO[str]
        return readme.read()


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt") as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


def main(package: __Package) -> None:
    """Setup package entrypoint."""
    __compose_package(
        name=package.name,
        version=package.version,
        author=package.author,
        author_email=package.email,
        description=package.goal,
        long_description=__readme(),
        long_description_content_type="text/markdown",
        url=f"https://github.com/vyahello/{package.name}",
        packages=__find_packages(
            exclude=("*.tests", "*.tests.*", "tests.*", "tests")
        ),
        include_package_data=True,
        install_requires=__requirements(),
        classifiers=(
            "Framework :: Pytest",
            "Topic :: Software Development :: Testing",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            f"License :: OSI Approved :: {package.license_} License",
            "Operating System :: OS Independent",
        ),
        python_requires=">=3.6",
        entry_points={"pytest11": ("creport = report.plugin",)},
    )


if __name__ == "__main__":
    sys.exit(main(package=__Package(path=Path('report'))))
