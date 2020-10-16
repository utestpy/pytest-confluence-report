"""Represents executable entrypoint for `report_from` application."""
import textwrap
from typer import Option, run
from uyaml import YamlFromPath
from report.xml import PytestXml, report_from_xml
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
        client.build_page(content=report_from_xml(PytestXml(path=xml_path)))


if __name__ == "__main__":
    run(__main)
