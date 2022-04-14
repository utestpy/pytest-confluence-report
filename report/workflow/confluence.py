"""Module contains API to operate Confluence page(s)."""
from abc import ABC, abstractmethod
from types import TracebackType
from typing import Optional, Type
from urllib.parse import urljoin

from atlassian import Confluence
from loguru import logger as _logger

from report import Settings


def client_from_settings(settings: Settings) -> Confluence:
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
    """The class represents abstract interface for Confluence Client."""

    @property
    @abstractmethod
    def link(self) -> str:
        """Returns page link."""
        pass

    @property
    @abstractmethod
    def id_(self) -> int:
        """Returns page id."""
        pass

    @abstractmethod
    def build(self, content: str) -> None:
        """Creates a page."""
        pass

    @abstractmethod
    def update(self, content: str) -> None:
        """Updates confluence client page."""
        pass

    @abstractmethod
    def exists(self) -> bool:
        """Check if page exists page."""
        pass


class _EmptyPage(Page):
    """The class represents an empty page."""

    @property
    def link(self) -> str:
        """Returns am empty link."""
        return ''

    @property
    def id_(self) -> int:
        """Returns am empty id."""
        return 0

    def build(self, content: str) -> None:
        """Creates an empty page."""
        content = ''  # noqa: F841

    def update(self, content: str) -> None:
        """Updates an empty page."""
        content = ''  # noqa: F841

    def exists(self) -> bool:
        """Returns not existing page."""
        return False


class ConfluencePage(Page):
    """The class represents interface for Confluence page."""

    def __init__(self, settings: Settings, client: Confluence) -> None:
        self._settings: Settings = settings
        self._client: Confluence = client

    @property
    def link(self) -> str:
        """Returns confluence client page.

        Returns: a link
        """
        link: str = self._client.get_page_by_title(
            space=self._settings.page.space, title=self._settings.page.target
        )['_links']['webui']
        return urljoin(self._settings.url, f'wiki{link}')

    @property
    def id_(self) -> int:
        """Returns confluence page id."""
        return self._client.get_page_id(
            space=self._settings.page.space, title=self._settings.page.target
        )

    def build(self, content: str) -> None:
        """Creates confluence client page."""
        self._client.create_page(
            space=self._settings.page.space,
            title=self._settings.page.target,
            body=content,
        )

    def update(self, content: str) -> None:
        """Updates confluence client page."""
        self._client.update_page(self.id_, self._settings.page.target, content)

    def exists(self) -> bool:
        """Check if page exists page."""
        return self._client.page_exists(
            self._settings.page.space, self._settings.page.target
        )


class ConfluenceContent:
    """The class represents interface to work with Confluence page."""

    def __init__(self, page: Page, settings: Settings) -> None:
        self._page: Page = page
        self._settings: Settings = settings

    def __enter__(self) -> 'ConfluenceContent':
        """Returns Confluence content."""
        if isinstance(self._page, _EmptyPage):
            self._page = ConfluencePage(
                self._settings, client_from_settings(self._settings)
            )
        return self

    def build(self, content: str) -> None:
        """Create page with given body.

        Args:
            content: <str> a body
        """
        if self._page.exists():
            self._page.update(content)
            self._inform_page_action(action='updated')
        else:
            self._page.build(content)
            self._inform_page_action(action='created')

    def _inform_page_action(self, action: str) -> None:
        """Inform Confluence page action.

        Args:
            action: <str> an action
        """
        _logger.info(
            '"{}" page is {}. Please follow "{}" link.',
            self._settings.page.target,
            action,
            self._page.link,
        )

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Clears Client."""
        self._page = _EmptyPage()
