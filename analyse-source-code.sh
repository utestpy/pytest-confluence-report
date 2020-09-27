#!/usr/bin/env bash

# specifies a set of variables to declare files to be used for code assessment
PACKAGE="report"

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"


pretty-printer-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    echo "Start ${1} analysis ..."
}


remove-pycache() {
:<<DOC
    Removes python cache directories
DOC
    ( find . -depth -name __pycache__ | xargs rm -r )
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    pretty-printer-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
:<<DOC
    Runs "flake8" code analysers
DOC
    pretty-printer-box "flake" && ( flake8 ./ )
}


check-pylint() {
:<<DOC
    Runs "pylint" code analyser
DOC
    pretty-printer-box "pylint" && ( find ${PACKAGE} -type f -name "*.py" | xargs pylint )
}


check-mypy() {
:<<DOC
    Runs "mypy" code analyser
DOC
    pretty-printer-box "mypy" && ( mypy --package "${PACKAGE}" )
}


check-docstrings() {
:<<DOC
     Runs "pydocstyle" static documentation code style formatter
DOC
    pretty-printer-box "pydocstyle" && ( pydocstyle --explain --count ${PACKAGE} )
    pretty-printer-box "interrogate" && interrogate -vv ${PACKAGE}
}


check-unittests() {
:<<DOC
    Runs unittests using "pytest" framework
DOC
    pretty-printer-box "unitests" && pytest
}


check-pymanifest() {
:<<DOC
    Runs unittests using "check-manifest" tool
DOC
    pretty-printer-box "check-manifest" && check-manifest -v ./
}


is-passed() {
:<<DOC
    Checks if code assessment is passed
DOC
    if [[ $? -ne 0 ]]; then
      echo -e "${FAILED_OUT}Code assessment is failed, please fix errors!${NONE_OUT}"
      exit 100
    else
      echo -e "${PASSED_OUT}Congratulations, code assessment is passed!${NONE_OUT}"
    fi
}


main() {
:<<DOC
    Runs "main" code analyser
DOC
    (
      remove-pycache
      check-black && \
      check-mypy && \
      check-pylint && \
      check-flake && \
      check-docstrings && \
      check-pymanifest && \
      check-unittests && \
      is-passed
    )
    return 0
}

main