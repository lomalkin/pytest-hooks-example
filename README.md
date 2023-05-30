# pytest-hooks-example

Pytest hooks invocation order example.

## Run
```pytest```
OR
```pytest -sv --setup-show```

## Output
```
% pytest -sv --setup-show
pytest_configure()
========================================================= test session starts ==========================================================
platform darwin -- Python 3.10.10, pytest-7.2.0, pluggy-1.0.0 -- /opt/homebrew/opt/python@3.10/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/user/pytest-hooks-example
plugins: allure-pytest-2.11.1
collected 5 items                                                                                                                      
pytest_runtest_protocol()

test_hooks.py::test_simpletest_passes pytest_runtest_setup()
fixture_session()

SETUP    S fixture_sessionfixture_module()

    SETUP    M fixture_modulefixture_function()

        SETUP    F fixture_functionpytest_runtest_makereport(), when=setup

        test_hooks.py::test_simpletest_passes (fixtures used: fixture_function, fixture_module, fixture_session)pytest_runtest_call()
pytest_runtest_makereport(), when=call
PASSEDpytest_runtest_teardown()

        TEARDOWN F fixture_functionpytest_runtest_makereport(), when=teardown
pytest_runtest_protocol()

test_hooks.py::test_simpletest_fails pytest_runtest_setup()
fixture_function()

        SETUP    F fixture_functionpytest_runtest_makereport(), when=setup

        test_hooks.py::test_simpletest_fails (fixtures used: fixture_function, fixture_module, fixture_session)pytest_runtest_call()
pytest_runtest_makereport(), when=call
FAILEDpytest_exception_interact()
pytest_runtest_teardown()

        TEARDOWN F fixture_functionpytest_runtest_makereport(), when=teardown
pytest_runtest_protocol()

test_hooks.py::test_simpletest_fails_with_exception pytest_runtest_setup()
fixture_function()

        SETUP    F fixture_functionpytest_runtest_makereport(), when=setup

        test_hooks.py::test_simpletest_fails_with_exception (fixtures used: fixture_function, fixture_module, fixture_session)pytest_runtest_call()
pytest_runtest_makereport(), when=call
FAILEDpytest_exception_interact()
pytest_runtest_teardown()

        TEARDOWN F fixture_functionpytest_runtest_makereport(), when=teardown
pytest_runtest_protocol()

test_hooks.py::test_simpletest_fails_xfail pytest_runtest_setup()
fixture_function()

        SETUP    F fixture_functionpytest_runtest_makereport(), when=setup

        test_hooks.py::test_simpletest_fails_xfail (fixtures used: fixture_function, fixture_module, fixture_session)pytest_runtest_call()
pytest_runtest_makereport(), when=call
XFAILpytest_runtest_teardown()

        TEARDOWN F fixture_functionpytest_runtest_makereport(), when=teardown
pytest_runtest_protocol()

test_hooks.py::test_simpletest_skipped pytest_runtest_makereport(), when=setup
SKIPPED (unconditional skip)pytest_runtest_teardown()

    TEARDOWN M fixture_module
TEARDOWN S fixture_sessionpytest_runtest_makereport(), when=teardown


=============================================================== FAILURES ===============================================================
________________________________________________________ test_simpletest_fails _________________________________________________________

    def test_simpletest_fails():
>       assert False
E       assert False

test_hooks.py:32: AssertionError
_________________________________________________ test_simpletest_fails_with_exception _________________________________________________

    def test_simpletest_fails_with_exception():
>       raise Exception("Test failed with exception")
E       Exception: Test failed with exception

test_hooks.py:36: Exception
======================================================= short test summary info ========================================================
FAILED test_hooks.py::test_simpletest_fails - assert False
FAILED test_hooks.py::test_simpletest_fails_with_exception - Exception: Test failed with exception
========================================== 2 failed, 1 passed, 1 skipped, 1 xfailed in 0.02s ===========================================
pytest_unconfigure()
```