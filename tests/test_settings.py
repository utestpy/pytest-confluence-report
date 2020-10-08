import pytest
from report.settings import _Credentials


@pytest.fixture()
def credentials() -> _Credentials:
    return _Credentials('foo', 'bar')


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
