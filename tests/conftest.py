import pytest
import sys
from uyaml import Yaml
from report.settings import Settings
from tests.fake import FakeSettings, FakeYaml


def pytest_report_header() -> str:
    """Adds header to pytest runner."""
    return (
        f'Running on {sys.platform} platform'
        f": {'{}.{}.{}'.format(*sys.version_info[:3])} python versions"
    )


@pytest.fixture(scope='module')
def fake_yaml() -> Yaml:
    return FakeYaml()


@pytest.fixture(scope='module')
def fake_settings() -> Settings:
    return FakeSettings()
