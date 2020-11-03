"""Package stands for pytest plugin to upload results into Confluence page."""
import logging
from typing import Tuple
from uyaml import ContextYamlFromPath, Yaml
from report.xml import PytestXml
from report.html import ReportPage
from report.confluence import (
    ConfluenceContent,
    ConfluencePage,
    client_from_settings,
)
from report.settings import ConfluenceSettings, Settings

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
    'client_from_settings',
)

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
)


def easy_build(settings_path: str, xml_path: str) -> None:
    """Builds Confluence report page based on settings path and test XML file.

    Args:
        settings_path: <str> a settings path.
        xml_path: <str> an XML path.
    """
    with ContextYamlFromPath(path=settings_path) as yaml:  # type: Yaml
        confluence_settings: Settings = ConfluenceSettings(settings=yaml)
        with ConfluenceContent(
            ConfluencePage(
                settings=confluence_settings,
                client=client_from_settings(confluence_settings),
            ),
            settings=confluence_settings,
        ) as page:
            with ReportPage(PytestXml(path=xml_path)) as report:
                page.build(content=report.content)
