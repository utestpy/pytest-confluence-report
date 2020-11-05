"""Package stands for pytest plugin to upload results into Confluence page."""
import logging
from typing import Tuple

from report.workflow.settings import ConfluenceSettings, Settings
from report.workflow.xml import PytestXml, TestXml
from report.workflow.html import ReportPage
from report.workflow.confluence import (
    ConfluenceContent,
    ConfluencePage,
    client_from_settings,
)
from report.workflow.build import easy_build

SETTINGS_PATH: str = 'settings.yml'
XML_PATH: str = 'pytest.xml'

__author__: str = 'Volodymyr Yahello'
__email__: str = 'vyahello@gmail.com'
__license__: str = 'MIT'
__copyright__: str = f'Copyright 2020, {__author__}'
__version__: str = '0.0.2'
__package_name__: str = 'pytest-confluence-report'
__all__: Tuple[str, ...] = (
    'ConfluenceContent',
    'ConfluencePage',
    'ConfluenceSettings',
    'Settings',
    'PytestXml',
    'ReportPage',
    'TestXml',
    'easy_build',
    'client_from_settings',
)

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
)
