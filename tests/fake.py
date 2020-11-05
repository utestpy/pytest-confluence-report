from uyaml import Yaml
from uyaml.loader import YamlType
from report.workflow.settings import Settings, _Credentials, _Page

SECTION = {
    'url': '',
    'page': {'parent': 'Home', 'target': 'Salary'},
    'credentials': {'username': 'Foo', 'api-key': 'Bar'},
}
CONFLUENCE_PART = {'confluence': SECTION}


class FakeYaml(Yaml):
    def content(self) -> YamlType:
        return {}

    def section(self, name: str) -> YamlType:
        return CONFLUENCE_PART[name]


class FakeSettings(Settings):
    @property
    def url(self) -> str:
        return ''

    @property
    def page(self) -> _Page:
        return _Page.from_dict(SECTION['page'])

    @property
    def credentials(self) -> _Credentials:
        return _Credentials.from_dict(SECTION['credentials'])
