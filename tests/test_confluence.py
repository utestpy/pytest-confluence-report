from atlassian import Confluence
from report.confluence import _client_from_settings
from report.settings import Settings


def test_client_from_settings(fake_settings: Settings) -> None:
    assert isinstance(_client_from_settings(fake_settings), Confluence)
