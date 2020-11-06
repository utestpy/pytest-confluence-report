"""Module provides a set of API for HTML page(s)."""
import logging
from datetime import date
from types import TracebackType
from typing import Optional, Type

from report import TestXml

_logger: logging.Logger = logging.getLogger(__name__)


def _date(format_string: str = '%B %d, %Y') -> str:
    """Returns current date."""
    return date.today().strftime(format_string)


class _HtmlPage:
    """The class represent html page."""

    STRONG_ELEMENT = '<strong>{}</strong>'
    TABLE_START_TAG = "<table border='1'>"
    TABLE_END_TAG = '</table>'
    HEADER_ROW_STYLE = "align='center' style='font-weight:bold'"
    HEADER_COLUMN_STYLE = 'data-highlight-colour="#eae6ff" class="confluenceTd"'

    def __init__(self, xml: TestXml) -> None:
        self._xml: TestXml = xml

    def build_date(self) -> str:
        """Returns date."""
        return f'<p>{self.STRONG_ELEMENT.format("Date")}: {_date()}</p>'

    def build_status_table(self) -> str:
        """Returns test status HTML table."""
        header: str = ''.join(
            map(
                lambda status: f'<td {self.HEADER_COLUMN_STYLE}>'
                f'<b>{status}</b></td>',
                self._xml.outcome.as_dict().keys(),
            )
        )
        amount: str = ''.join(
            map(
                lambda count: f'<td><b>{count}</b></td>',
                self._xml.outcome.as_dict().values(),
            )
        )
        return (
            f'<h3>{self.STRONG_ELEMENT.format("Test status:")}</h3>'
            f'{self.TABLE_START_TAG}'
            f"<tr {self.HEADER_ROW_STYLE}>{header}</tr>"
            f'<tr>{amount}</tr>{self.TABLE_END_TAG}'
        )

    def build_opened_bugs_table(self) -> str:
        """Returns opened bugs table."""
        return (
            f'<h3>{self.STRONG_ELEMENT.format("Opened bugs:")}</h3>'
            f'{self.STRONG_ELEMENT.format("Total: N")}'
            f'{self.TABLE_START_TAG}'
            f'<tr {self.HEADER_ROW_STYLE}>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Frequency</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Type (Known/New)</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Jira</b></td></tr>'
            f'<tr><td></td><td></td><td></td></tr>{self.TABLE_END_TAG}'
        )

    def build_failures_table(self) -> str:
        """Returns failures table."""
        return (
            f'<h3>{self.STRONG_ELEMENT.format("Failures:")}</h3>'
            f'{self.STRONG_ELEMENT.format("Total: N")}'
            f'{self.TABLE_START_TAG}'
            f'<tr {self.HEADER_ROW_STYLE}>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Frequency</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Assertion</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Test name(s)</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Reason</b></td>'
            f'<td {self.HEADER_COLUMN_STYLE}><b>Resolution</b></td></tr>'
            f'<tr>'
            f'<td></td><td></td><td></td><td></td><td></td>'
            f'</tr>{self.TABLE_END_TAG}'
        )


class ReportPage:
    """Represent test report page."""

    def __init__(self, xml: TestXml) -> None:
        self._xml: TestXml = xml
        self._page: _HtmlPage = _HtmlPage(xml)
        self._content: str = ''

    def __enter__(self) -> 'ReportPage':
        """Returns report page instance."""
        if not self._content:
            _logger.info('Collecting statistics from "%s" file', self._xml.name)
            self._content += self._page.build_date()
            self._content += self._page.build_status_table()
            self._content += self._page.build_opened_bugs_table()
            self._content += self._page.build_failures_table()
        return self

    @property
    def content(self) -> str:
        """Returns report page content."""
        return self._content

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Clears report page content."""
        self._content = ''
