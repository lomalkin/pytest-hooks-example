import pytest
from termcolor import colored

FIXT_PRINT_COLOR = "green"

# Fixtures:


@pytest.fixture(scope="session", autouse=True)
def fixture_session():
    print(colored("fixture_session()", FIXT_PRINT_COLOR, attrs=["bold"]))


@pytest.fixture(scope="function", autouse=True)
def fixture_function():
    print(colored("fixture_function()", FIXT_PRINT_COLOR, attrs=["bold"]))


@pytest.fixture(scope="module", autouse=True)
def fixture_module():
    print(colored("fixture_module()", FIXT_PRINT_COLOR, attrs=["bold"]))


# Tests:


def test_simpletest_passes():
    assert True


def test_simpletest_fails():
    assert False


def test_simpletest_fails_with_exception():
    raise Exception("Test failed with exception")


@pytest.mark.xfail
def test_simpletest_fails_xfail():
    assert False


@pytest.mark.skip
def test_simpletest_skipped():
    pass
