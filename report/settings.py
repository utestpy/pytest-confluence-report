"""Module provides a set of API to manipulate user topology settings."""
from typing import Any, Dict, Sequence
from uyaml import Yaml
from punish import AbstractStyle, abstractstyle


class _Credentials(AbstractStyle):
    """The class represents credentials as an object."""

    __slots__: Sequence[str] = ('_username', '_api_key')

    def __init__(self, username: str, api_key: str) -> None:
        self._username = username
        self._api_key = api_key

    @property
    def username(self) -> str:
        """Return a username.

        :return: <str> username
        """
        return self._username

    @property
    def api_key(self) -> str:
        """Return a API Key.

        :return: <str> api key
        """
        return self._api_key

    @classmethod
    def from_dict(cls, settings: Dict[str, str]) -> "_Credentials":
        """Instantiate fresh credentials object from given settings.

        Example:
        >>> credentials = _Credentials.from_dict(
        ...     {'username': 'foo', 'api-key': 'bar'}
        ... )
        >>> credentials.username
        'foo'
        >>> credentials.api_key
        'bar'

        :param settings: <dict> given settings
        :return: credentials object
        """
        return cls(settings['username'], settings['api-key'])

    def __str__(self) -> str:
        """Return credentials as string representative.

        :return: <str> a string
        """
        return f'[{self.__class__.__name__}: user = {self._username}]'


class _Page(AbstractStyle):
    """Represents an abstract interface for confluence page settings."""

    __slots__: Sequence[str] = ('_parent', '_target')

    def __init__(self, parent: str, target: str) -> None:
        self._parent = parent
        self._target = target

    @property
    def parent(self) -> str:
        """Returns parent confluence page."""
        return self._parent

    @property
    def target(self) -> str:
        """Returns parent confluence page."""
        return self._target

    @classmethod
    def from_dict(cls, settings: Dict[str, str]) -> "_Page":
        """Instantiate fresh page object from given settings.

        Example:
        >>> page = _Page.from_dict(
        ...     {'parent': 'Home', 'target': 'Personal web site tests'}
        ... )
        >>> page.parent
        'Home'
        >>> page.target
        'Personal web site tests'

        :param settings: <dict> given settings
        :return: credentials object
        """
        return cls(settings['parent'], settings['target'])

    def __str__(self) -> str:
        """Return credentials as string representative.

        :return: <str> a string
        """
        return (
            f'[{self.__class__.__name__}: '
            f'parent = {self._parent}, target = {self._target}]'
        )


class Settings(AbstractStyle):
    """Represents an abstract interface for settings topology."""

    @property  # type: ignore
    @abstractstyle
    def url(self) -> str:
        """Return an URL.

        :return: <str> URL
        """
        pass

    @property  # type: ignore
    @abstractstyle
    def page(self) -> _Page:
        """Return an URL.

        :return: <str> URL
        """
        pass

    @property  # type: ignore
    @abstractstyle
    def credentials(self) -> _Credentials:
        """Return credentials.

        :return: <Credentials> user credentials
        """
        pass


class _UnifiedSettings(Settings):
    """Represents common settings topology."""

    __slots__: Sequence[str] = ('_yaml',)

    def __init__(self, section: Dict[str, Any]) -> None:
        self._yaml = section

    @property
    def url(self) -> str:
        """Return an URL.

        :return: <str> URL
        """
        return self.__content(name='url')

    @property
    def page(self) -> _Page:
        """Return an URL.

        :return: <Page> a page
        """
        return _Page.from_dict(self.__content(name='page'))

    @property
    def credentials(self) -> _Credentials:
        """Return credentials.

        :return: <Credentials> user credentials
        """
        return _Credentials.from_dict(settings=self.__content('credentials'))

    def __content(self, name: str) -> Any:
        """Return content from yaml file.

        :param name: <str> item from yaml file
        :return: <int>, <str>, or <dict> from yaml file
        """
        return self._yaml[name]


class ConfluenceSettings(Settings):
    """Represents testrail settings topology."""

    __slots__: Sequence[str] = ('_confluence',)

    def __init__(self, settings: Yaml) -> None:
        self._confluence: Settings = _UnifiedSettings(
            settings.section(name='confluence')
        )

    @property
    def url(self) -> str:
        """Return Confluence source URL.

        :return: <str> TestRail URL
        """
        return self._confluence.url

    @property
    def page(self) -> _Page:
        """Return an URL.

        :return: <Page> a page
        """
        return self._confluence.page

    @property
    def credentials(self) -> _Credentials:
        """Return Confluence credentials.

        :return: <Credentials> TestRail credentials
        """
        return self._confluence.credentials
