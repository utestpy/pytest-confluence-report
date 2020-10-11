from atlassian import Confluence
from report.confluence import _client_from_settings
from tests.fake import FakeSettings


def test_client_from_settings() -> None:
    assert isinstance(_client_from_settings(FakeSettings()), Confluence)
