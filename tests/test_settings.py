import pytest
from uyaml import Yaml
from uyaml.loader import YamlType
from report.settings import (
    ConfluenceSettings,
    Settings,
    _Credentials,
    _Page,
    _UnifiedSettings,
)

_SECTION = {
    'url': '',
    'page': {'parent': 'Home', 'target': 'Salary'},
    'credentials': {'username': 'Foo', 'api-key': 'Bar'},
}
_CONFLUENCE_PART = {'confluence': _SECTION}


class FakeYaml(Yaml):
    def content(self) -> YamlType:
        return {}

    def section(self, name: str) -> YamlType:
        return _CONFLUENCE_PART[name]


@pytest.fixture()
def credentials() -> _Credentials:
    return _Credentials('foo', 'bar')


@pytest.fixture()
def page() -> _Page:
    return _Page('Home', 'Salary')


@pytest.fixture()
def unified_settings() -> Settings:
    return _UnifiedSettings(_SECTION)


@pytest.fixture()
def settings() -> Settings:
    return ConfluenceSettings(FakeYaml())


def test_credentials_username(credentials: _Credentials) -> None:
    assert credentials.username == 'foo'


def test_credentials_api_key(credentials: _Credentials) -> None:
    assert credentials.api_key == 'bar'


def test_credentials_from_dict() -> None:
    assert isinstance(
        _Credentials.from_dict({'username': 'foo', 'api-key': 'bar'}),
        _Credentials,
    )


def test_credentials_as_str(credentials: _Credentials) -> None:
    assert str(credentials) == '[_Credentials: user = foo]'


def test_page_parent(page: _Page) -> None:
    assert page.parent == 'Home'


def test_page_target(page: _Page) -> None:
    assert page.target == 'Salary'


def test_page_from_dict() -> None:
    assert _Page.from_dict({'parent': 'Home', 'target': 'Salary'})


def test_unified_settings_url(unified_settings: _UnifiedSettings) -> None:
    assert unified_settings.url == ''


def test_unified_settings_page(unified_settings: _UnifiedSettings) -> None:
    assert isinstance(unified_settings.page, _Page)


def test_unified_settings_credentials(
    unified_settings: _UnifiedSettings,
) -> None:
    assert isinstance(unified_settings.credentials, _Credentials)


def test_unified_settings_content(unified_settings: _UnifiedSettings) -> None:
    assert unified_settings._UnifiedSettings__content('page') == {
        'parent': 'Home',
        'target': 'Salary',
    }


def test_settings_url(settings: ConfluenceSettings) -> None:
    assert settings.url == ''


def test_settings_page(settings: ConfluenceSettings) -> None:
    assert isinstance(settings.page, _Page)


def test_settings_credentials(settings: ConfluenceSettings) -> None:
    assert isinstance(settings.credentials, _Credentials)
