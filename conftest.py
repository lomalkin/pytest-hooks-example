import pytest
from termcolor import colored

HOOKS_PRINT_COLOR = "blue"


# Pytest session hooks:
def pytest_configure(config):
    # here you can add setup before launching session!
    print(colored("pytest_configure()", HOOKS_PRINT_COLOR, attrs=["bold"]))


def pytest_unconfigure(config):
    # here you can add teardown after session!
    print(colored("pytest_unconfigure()", HOOKS_PRINT_COLOR, attrs=["bold"]))


# Tests hooks:
def pytest_runtest_setup(item):
    print(colored("pytest_runtest_setup()", HOOKS_PRINT_COLOR, attrs=["bold"]))


def pytest_runtest_call(item):
    print(colored("pytest_runtest_call()", HOOKS_PRINT_COLOR, attrs=["bold"]))


def pytest_runtest_teardown(item, nextitem):
    print(colored("pytest_runtest_teardown()", HOOKS_PRINT_COLOR, attrs=["bold"]))


#


def pytest_runtest_protocol(item, nextitem):
    print(colored("pytest_runtest_protocol()", HOOKS_PRINT_COLOR, attrs=["bold"]))


def pytest_exception_interact(node, call, report):
    print(colored("pytest_exception_interact()", HOOKS_PRINT_COLOR, attrs=["bold"]))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    print(
        colored(
            "pytest_runtest_makereport(), when=%s" % (report.when),
            HOOKS_PRINT_COLOR,
            attrs=["bold"],
        )
    )
