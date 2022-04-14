"""Module contains confluence reporter plugin AP."""
import sys

from _pytest.config import Config
from _pytest.config.argparsing import OptionGroup, Parser
from loguru import logger as _logger

from report import SETTINGS_PATH, easy_build


def pytest_addoption(parser: Parser) -> None:
    """Defines custom pytest options.

    Args:
        parser: Parser for command line arguments and ini-file values
    """
    group: OptionGroup = parser.getgroup(name='Confluence test report')
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
            xml_path=config.option.xmlpath,
        )
