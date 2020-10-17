"""Module contains confluence reporter plugin AP."""
import logging
import sys
from _pytest.config import Config
from _pytest.config.argparsing import OptionGroup, Parser
from report import SETTINGS_PATH, XML_PATH, easy_build

_logger: logging.Logger = logging.getLogger(__name__)


def pytest_addoption(parser: Parser) -> None:
    """Defines custom pytest options.

    Args:
        parser: Parser for command line arguments and ini-file values
    """
    group: OptionGroup = parser.getgroup(name='Confluence report_from')
    group.addoption(
        '--confluence-upload',
        '--cu',
        action='store_true',
        help='Convert pytest results into Confluence page',
    )
    group.addoption(
        '--confluence-settings',
        '--cs',
        type=str,
        default=SETTINGS_PATH,
        help=f'Path to Confluence settings file e.g `{SETTINGS_PATH}`.',
    )
    group.addoption(
        '--pytest-xml-path',
        '--px',
        type=str,
        default=XML_PATH,
        help=f'Path to pytest XML file e.g `{XML_PATH}`.',
    )


def pytest_report_header() -> str:
    """Adds header to pytest runner."""
    return (
        f'Running on {sys.platform} platform'
        f": {'{}.{}.{}'.format(*sys.version_info[:3])} python versions"
    )


def pytest_unconfigure(config: Config) -> None:
    """Pytest hook that launches at the end of test run."""
    if config.getoption('confluence_upload'):
        _logger.info('Uploading testing results to confluence ...')
        easy_build(
            settings_path=config.getoption(name='confluence_settings'),
            xml_path=config.getoption(name='pytest_xml_path'),
        )
