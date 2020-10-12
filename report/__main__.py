"""Represents executable entrypoint for `report` application."""
import textwrap
from typer import Option, run
from uyaml import YamlFromPath
from report import SETTINGS_PATH, confluence
from report.settings import ConfluenceSettings


def __main(
    settings_path: str = Option(
        default=SETTINGS_PATH,
        help=textwrap.dedent(
            f'Confluence settings file (e.g ``{SETTINGS_PATH}``)'
        ),
    ),
    xml_path: str = Option(
        default='',
        help=textwrap.dedent('Pytest XML artifact file e.g ``pytest.xml``.'),
    ),
) -> None:
    """Tool allows to convert pytest results into Confluence page."""

    with confluence.Client(
        settings=ConfluenceSettings(YamlFromPath(settings_path))
    ) as client:
        # TODO  # pylint: disable=fixme
        # xml_from_pytest = XmlFile(xml_path)
        # failures = xml_from_pytest.load_failures(html=True)
        client.build_page(xml_path)


if __name__ == "__main__":
    run(__main)
