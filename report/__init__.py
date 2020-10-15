"""Package stands for pytest plugin to upload results into Confluence page."""
import logging

__author__: str = 'Volodymyr Yahello'
__email__: str = 'vyahello@gmail.com'
__license__: str = 'MIT'
__copyright__: str = f'Copyright 2020, {__author__}'
__version__: str = '0.0.0'
__package_name: str = 'pytest-confluence-report'

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
)
SETTINGS_PATH: str = 'settings.yml'
XML_PATH: str = 'pytest.xml'
