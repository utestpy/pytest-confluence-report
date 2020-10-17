"""Module contains API to operate Confluence REST."""
import logging
from abc import ABC, abstractmethod
from types import TracebackType
from typing import Optional, Type
from atlassian import Confluence
from report.settings import ConfluenceSettings, Settings

_logger: logging.Logger = logging.getLogger(__name__)


def _client_from_settings(settings: Settings) -> Confluence:
    """Returns Confluence client from settings.

    Args:
        settings: a Confluence settings/

    Returns: Confluence client.
    """
    return Confluence(
        settings.url,
        settings.credentials.username,
        settings.credentials.api_key,
    )


class Page(ABC):
    """The class represents abstract interface for page."""

    @property
    @abstractmethod
    def link(self) -> str:
        """Returns page link."""
        pass

    @abstractmethod
    def build(self, content: str) -> None:
        """Creates a page."""
        pass


class _EmptyPage(Page):
    """The class represents an empty page."""

    @property
    def link(self) -> str:
        """Returns am empty link."""
        return ''

    def build(self, content: str) -> None:
        """Creates an empty page."""
        content = ''  # noqa: F841


class _ConfluencePage(Page):
    """The class represents interface for Confluence page."""

    def __init__(
        self, settings: ConfluenceSettings, client: Confluence
    ) -> None:
        self._settings: ConfluenceSettings = settings
        self._client: Confluence = client

    @property
    def link(self) -> str:
        """Returns page link.

        Returns: a link
        """
        link: str = self._client.get_page_by_title(
            space=self._settings.page.parent, title=self._settings.page.target
        )['_links']['webui']
        return f'{self._settings.url}wiki{link}'

    def build(self, content: str) -> None:
        """Creates confluence page."""
        self._client.create_page(
            space=self._settings.page.parent,
            title=self._settings.page.target,
            body=content,
        )


class RestClient:
    """The class represents interface to work with Confluence REST."""

    def __init__(self, settings: ConfluenceSettings) -> None:
        self._settings: ConfluenceSettings = settings
        self._client: Optional[Confluence] = None
        self._page: Page = _EmptyPage()

    def __enter__(self) -> "RestClient":
        """Returns Confluence Client."""
        if not self._client:
            self._client = _client_from_settings(self._settings)
            if isinstance(self._page, _EmptyPage):
                self._page = _ConfluencePage(self._settings, self._client)
        return self

    def build_page(self, content: str) -> None:
        """Create page with given body.

        Args:
            content: <str> a body
        """
        _logger.info('Creating "%s" page', self._settings.page.target)
        self._page.build(content)
        _logger.info(
            '"%s" page is created. Please follow "%s" link.',
            self._settings.page.target,
            self._page.link,
        )

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Clears Client."""
        self._client = None
        self._page = _EmptyPage()
