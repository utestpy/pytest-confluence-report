"""Module contains API to operate Confluence REST."""
import logging
from types import TracebackType
from typing import Dict, Optional, Type
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


class Client:
    """The class represents interface to work with Confluence REST."""

    def __init__(self, settings: ConfluenceSettings) -> None:
        self._settings: ConfluenceSettings = settings
        self._client: Confluence = _client_from_settings(settings)

    def __enter__(self) -> "Client":
        """Returns Confluence Client."""
        return self

    def _page_link(self, from_response: Dict[str, Dict[str, str]]) -> str:
        """Returns page link.

        Args:
            from_response: <dict> a response

        Returns: a link
        """
        return f'{self._settings.url}wiki{from_response["_links"]["webui"]}'

    def build_page(self, body: str) -> None:
        """Create page with given body.

        Args:
            body: <str> a body
        """
        _logger.info('Creating "%s" page', self._settings.page.target)
        response = self._client.create_page(
            self._settings.page.parent, self._settings.page.target, body
        )
        _logger.info(
            '"%s" page is created. Please follow "%s" link.',
            self._settings.page.target,
            self._page_link(response),
        )

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],  # noqa: U100
        exception_value: Optional[BaseException],  # noqa: U100
        traceback: Optional[TracebackType],  # noqa: U100
    ) -> None:
        """Clears Client."""
        del self._client
        del self._settings
