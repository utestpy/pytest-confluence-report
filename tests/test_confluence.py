import pytest
from atlassian import Confluence
from report.confluence import Page, _EmptyPage, client_from_settings
from report.settings import Settings


@pytest.fixture(scope='module')
def empty_page() -> Page:
    return _EmptyPage()


def test_client_from_settings(fake_settings: Settings) -> None:
    assert isinstance(client_from_settings(fake_settings), Confluence)


def test_empty_link(empty_page: Page) -> None:
    assert not empty_page.link


def test_empty_page_build(empty_page: Page) -> None:
    assert not empty_page.build('')


def test_empty_page_update(empty_page: Page) -> None:
    assert not empty_page.update('')


def test_empty_id(empty_page: Page) -> None:
    assert not empty_page.id_


def test_empty_page_exists(empty_page: Page) -> None:
    assert not empty_page.exists()
