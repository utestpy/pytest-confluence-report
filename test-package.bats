#!/usr/bin/env bats


setup() {
:<<DOC
  Installs package
DOC
  python setup.py install
}


teardown() {
:<<DOC
  Removes package
DOC
  rm -rf ${PACKAGE_NAME}.egg-info dist build
}


@test "package name" {
:<<DOC
  Test package name
DOC
  pip list | grep ${PACKAGE_NAME}
  [ "$?" -eq 0 ]
}


@test "package version" {
:<<DOC
  Test package version
DOC
  pip list | grep ${PACKAGE_VERSION}
  [ "$?" -eq 0 ]
}


@test "pytest confluence group" {
:<<DOC
  Test pytest confluence group help message
DOC
  pytest --help | grep "Confluence report"
  [ "$?" -eq 0 ]
}


@test "pytest upload help" {
:<<DOC
  Test pytest upload help
DOC
  pytest --help | grep "Convert pytest results into Confluence page"
  [ "$?" -eq 0 ]
}


@test "pytest upload long flag" {
:<<DOC
  Test pytest upload long flag
DOC
  pytest --help | grep "--confluence-upload"
  [ "$?" -eq 0 ]
}


@test "pytest upload short flag" {
:<<DOC
  Test pytest upload short flag
DOC
  pytest --help | grep "--cu"
  [ "$?" -eq 0 ]
}


@test "pytest settings help" {
:<<DOC
  Test pytest settings help
DOC
  pytest --help | grep "Path to Confluence settings file"
  [ "$?" -eq 0 ]
}


@test "pytest settings long flag" {
:<<DOC
  Test pytest settings long flag
DOC
  pytest --help | grep "--confluence-settings"
  [ "$?" -eq 0 ]
}


@test "pytest settings short flag" {
:<<DOC
  Test pytest settings short flag
DOC
  pytest --help | grep "--cs"
  [ "$?" -eq 0 ]
}