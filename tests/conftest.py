import sys


def pytest_report_header() -> str:
    """Adds header to pytest runner."""
    return (
        f'Running on {sys.platform} platform'
        f": {'{}.{}.{}'.format(*sys.version_info[:3])} python versions"
    )
