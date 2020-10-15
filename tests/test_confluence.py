import pytest
from atlassian import Confluence
from report.confluence import Page, _EmptyPage, _client_from_settings
from report.settings import Settings


@pytest.fixture(scope='module')
def empty_page() -> Page:
    return _EmptyPage()


def test_client_from_settings(fake_settings: Settings) -> None:
    assert isinstance(_client_from_settings(fake_settings), Confluence)


def test_empty_link(empty_page: Page) -> None:
    assert not empty_page.link


def test_empty_build(empty_page: Page) -> None:
    assert not empty_page.build('')
