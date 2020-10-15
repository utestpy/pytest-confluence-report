"""Module provides a set of API for XML files."""
import logging
from abc import ABC, abstractmethod
from typing import Dict
from junitparser import JUnitXml

_logger: logging.Logger = logging.getLogger(__name__)


class Xml(ABC):
    """XML file abstraction."""

    @property
    @abstractmethod
    def statistics(self) -> str:
        """Returns xml statistics."""
        pass


class _Outcome:
    """An outcome of report."""

    def __init__(self, report: JUnitXml) -> None:
        self._report: JUnitXml = report

    @property
    def total(self) -> int:
        """Returns total tests count."""
        return self._report.tests

    @property
    def skipped(self) -> int:
        """Returns skipped tests count."""
        return self._report.skipped

    @property
    def failed(self) -> int:
        """Returns failed tests count."""
        return self._report.failures

    @property
    def errored(self) -> int:
        """Returns errored tests count."""
        return self._report.errors

    @property
    def passed(self) -> int:
        """Returns passed tests count."""
        return self.total - self.skipped - self.failed - self.errored

    def as_dict(self) -> Dict[str, int]:
        """Returns tests as dict."""
        return {
            'total': self.total,
            'skipped': self.skipped,
            'failed': self.failed,
            'errored': self.errored,
            'passed': self.passed,
        }


class PytestXml(Xml):
    """Pytest XML file."""

    def __init__(self, path: str) -> None:
        self._path: str = path
        self._outcome: _Outcome = _Outcome(JUnitXml.fromfile(filepath=path))

    @property
    def statistics(self) -> str:
        """Returns pytest xml file stats."""
        _logger.info('Collecting statistics from "%s" file', self._path)
        return (
            '<h1>Test report</h1>\n'
            f'Total: {self._outcome.total}\n'
            f'Passed: {self._outcome.passed}\n'
            f'Failed: {self._outcome.failed}\n'
            f'Skipped: {self._outcome.skipped}\n'
            f'Errored: {self._outcome.errored}\n'
        )
