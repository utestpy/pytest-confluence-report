Versions
========

0.4.0
=======
_Release date: 14.04.2022_

**Features**
- Support python3.9
- Add Continuous Integration via Github Actions

**Changes**
- Use 'space' instead of 'parent' name for Confluence pages 
- Fix shorten version option usage in readme 
- Document plugin usage in pytest config file
- Update mypy package version

0.0.3
=======
_Release date: 06.11.2020_

**Features**

- Add colorized purple font for table headers
- Create 'failures' table
- Create 'opened bugs' table
- Implement date section

**Changes**

- Fix Confluence page link forming
- Fix package group unit test
- Fix package import order
- Introduce helper package
- Create API to build report
- Mention about bats integration
- Fix failing Travis CI builds
- Implement package setup unit tests
- Release package setup from internal python dependencies
- Warn that project in under construction
- Add colorized purple font for table headers
- Create failures table
- Introduce HTML page builder
- Implement date section

0.0.2
========

_Release date: 17.10.2020_

**Features**

- Remove `--pytest-xml-path` pytest parameter

**Changes**

- Fix usage within documentation

0.0.1
========

_Release date: 17.10.2020_

**Features**

- Create test status report table based on XML file
- Use `--confluence-upload/--cu` pytest parameter to enable plugin
- Use `--confluence-settings/--sc` and `--pytest-xml-path/--px` optional pytest parameters to customize behaviour

**Changes**

- Build test status table from XML file
- Note about settings file completion
- Simplify report page builder interface
- Create report page instance
- Implement report from XML logic
- Implement initial XML composition
- Use typer CLI tool
- Add empty page unit tests
- Define used tools
- Create Confluence page interface
- Integrate confluence uploader within pytest
- Use `--confluence-upload` pytest parameter
