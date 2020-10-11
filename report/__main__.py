"""Represents executable entrypoint for `report` application."""
import textwrap
import click
from uyaml import YamlFromPath
from report import confluence
from report.settings import ConfluenceSettings

DEFAULT_PATH: str = 'settings.yml'


@click.command(
    help=textwrap.dedent(
        '''
    Tool allows to convert pytest results into Confluence page.
    '''
    ),
    short_help='Upload pytest results into Confluence.',
)
@click.option(
    '--settings-path',
    '-p',
    type=str,
    default=DEFAULT_PATH,
    help=textwrap.dedent(
        '''
    Confluence settings file (e.g ``settings.yml``)
    '''
    ),
    required=True,
)
@click.option(
    '--body',
    '-b',
    type=str,
    default='',
    help=textwrap.dedent(
        '''
    Confluence page body to fill.
    '''
    ),
    required=True,
)
def main(settings_path: str, body: str) -> None:
    """Launch command to upload test results into Confluence."""

    with confluence.Client(
        settings=ConfluenceSettings(YamlFromPath(settings_path))
    ) as client:
        client.build_page(body)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
