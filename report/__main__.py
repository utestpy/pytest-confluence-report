"""Represents executable entrypoint for `report` application."""
import textwrap
from typer import Option, run
from uyaml import YamlFromPath
from report.xml import PytestXml, Xml
from report import SETTINGS_PATH, XML_PATH, confluence
from report.settings import ConfluenceSettings


def __main(
    settings_path: str = Option(
        default=SETTINGS_PATH,
        help=textwrap.dedent(
            f'Confluence settings path (e.g ``{SETTINGS_PATH}``)'
        ),
    ),
    xml_path: str = Option(
        default=XML_PATH,
        help=textwrap.dedent(f'Pytest XML artifact path e.g ``{XML_PATH}``.'),
    ),
) -> None:
    """Tool allows to convert pytest results into Confluence page."""

    with confluence.Client(
        settings=ConfluenceSettings(YamlFromPath(settings_path))
    ) as client:
        pytestxml: Xml = PytestXml(path=xml_path)
        client.build_page(content=pytestxml.statistics)


if __name__ == "__main__":
    run(__main)
