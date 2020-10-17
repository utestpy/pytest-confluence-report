"""Represents executable entrypoint for `report_from` application."""
import textwrap
from typer import Option, run
from report import SETTINGS_PATH, XML_PATH, easy_build


def main(
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
    easy_build(settings_path, xml_path)


if __name__ == "__main__":
    run(main)
