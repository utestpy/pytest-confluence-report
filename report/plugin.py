"""Module contains confluence reporter plugin AP."""
import logging
import sys
from _pytest.config import Config
from _pytest.config.argparsing import OptionGroup, Parser

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.DEBUG,
)
_logger: logging.Logger = logging.getLogger(__name__)


def pytest_addoption(parser: Parser) -> None:
    """Defines custom pytest options.

    Args:
        parser: Parser for command line arguments and ini-file values
    """
    group: OptionGroup = parser.getgroup('Confluence report')
    group.addoption(
        '--confluence',
        '--cf',
        action='store_true',
        help='Convert pytest results into Confluence page',
    )


def pytest_report_header() -> str:
    """Adds header to pytest runner."""
    return (
        f'Running on {sys.platform} platform'
        f": {'{}.{}.{}'.format(*sys.version_info[:3])} python versions"
    )


def pytest_unconfigure(config: Config) -> None:
    """Pytest hook that launches at the end of test run."""
    if config.getoption('confluence'):
        _logger.info('Uploading testing results to confluence ...')
        # TODO  # pylint: disable=fixme
        # confluence = Confluence(load_confluence_config())
        # confluence.upload()
