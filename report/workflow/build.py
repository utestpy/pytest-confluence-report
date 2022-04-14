"""Module provides a set of API to build report."""
from uyaml import ContextYamlFromPath, Yaml

from report import (
    ConfluenceContent,
    ConfluencePage,
    ConfluenceSettings,
    PytestXml,
    ReportPage,
    Settings,
    client_from_settings,
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
        ) as page:  # type: ConfluenceContent
            with ReportPage(
                PytestXml(path=xml_path)
            ) as report:  # type: ReportPage
                page.build(content=report.content)
