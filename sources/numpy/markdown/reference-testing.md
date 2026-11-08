[Skip to main content](https://numpy.org/doc/stable/reference/testing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/testing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/testing.html)
[2.4](https://numpy.org/doc/2.4/reference/testing.html)
[2.3](https://numpy.org/doc/2.3/reference/testing.html)
[2.2](https://numpy.org/doc/2.2/reference/testing.html)
[2.1](https://numpy.org/doc/2.1/reference/testing.html)
[2.0](https://numpy.org/doc/2.0/reference/testing.html)
[1.26](https://numpy.org/doc/1.26/reference/testing.html)
[1.25](https://numpy.org/doc/1.25/reference/testing.html)
[1.24](https://numpy.org/doc/1.24/reference/testing.html)
[1.23](https://numpy.org/doc/1.23/reference/testing.html)
[1.22](https://numpy.org/doc/1.22/reference/testing.html)
[1.21](https://numpy.org/doc/1.21/reference/testing.html)
[1.20](https://numpy.org/doc/1.20/reference/testing.html)
[1.19](https://numpy.org/doc/1.19/reference/testing.html)
[1.18](https://numpy.org/doc/1.18/reference/testing.html)
[1.17](https://numpy.org/doc/1.17/reference/testing.html)
[1.16](https://numpy.org/doc/1.16/reference/testing.html)
[1.15](https://numpy.org/doc/1.15/reference/testing.html)
[1.14](https://numpy.org/doc/1.14/reference/testing.html)
[1.13](https://numpy.org/doc/1.13/reference/testing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Testing guidelines[#](https://numpy.org/doc/stable/reference/testing.html#testing-guidelines "Link to this heading")

=====================================================================================================================

Introduction[#](https://numpy.org/doc/stable/reference/testing.html#introduction "Link to this heading")

---------------------------------------------------------------------------------------------------------

Until the 1.15 release, NumPy used the [nose](https://nose.readthedocs.io/en/latest/)
 testing framework, it now uses the [pytest](https://pytest.readthedocs.io/)
 framework. The older framework is still maintained in order to support downstream projects that use the old numpy framework, but all tests for NumPy should use pytest.

Our goal is that every module and package in NumPy should have a thorough set of unit tests. These tests should exercise the full functionality of a given routine as well as its robustness to erroneous or unexpected input arguments. Well-designed tests with good coverage make an enormous difference to the ease of refactoring. Whenever a new bug is found in a routine, you should write a new test for that specific case and add it to the test suite to prevent that bug from creeping back in unnoticed.

Note

SciPy uses the testing framework from [`numpy.testing`](https://numpy.org/doc/stable/reference/routines.testing.html#module-numpy.testing "numpy.testing")
, so all of the NumPy examples shown below are also applicable to SciPy

Testing NumPy[#](https://numpy.org/doc/stable/reference/testing.html#testing-numpy "Link to this heading")

-----------------------------------------------------------------------------------------------------------

NumPy can be tested in a number of ways, choose any way you feel comfortable.

### Running tests from inside Python[#](https://numpy.org/doc/stable/reference/testing.html#running-tests-from-inside-python "Link to this heading")

You can test an installed NumPy by [`numpy.test`](https://numpy.org/doc/stable/reference/testing.html#numpy.test "numpy.test")
, for example, To run NumPy’s full test suite, use the following:

\>>> import numpy
\>>> numpy.test(label\='slow')

Copy to clipboard

The test method may take two or more arguments; the first `label` is a string specifying what should be tested and the second `verbose` is an integer giving the level of output verbosity. See the docstring [`numpy.test`](https://numpy.org/doc/stable/reference/testing.html#numpy.test "numpy.test")
 for details. The default value for `label` is ‘fast’ - which will run the standard tests. The string ‘full’ will run the full battery of tests, including those identified as being slow to run. If `verbose` is 1 or less, the tests will just show information messages about the tests that are run; but if it is greater than 1, then the tests will also provide warnings on missing tests. So if you want to run every test and get messages about which modules don’t have tests:

\>>> numpy.test(label\='full', verbose\=2)  \# or numpy.test('full', 2)

Copy to clipboard

Finally, if you are only interested in testing a subset of NumPy, for example, the `_core` module, use the following:

\>>> numpy.\_core.test()

Copy to clipboard

### Running tests from the command line[#](https://numpy.org/doc/stable/reference/testing.html#running-tests-from-the-command-line "Link to this heading")

If you want to build NumPy in order to work on NumPy itself, use the [spin utility](https://numpy.org/doc/stable/dev/spin.html#spin-tool)
.

To run NumPy’s full test suite:

$ spin test -m full

Copy to clipboard

Testing a subset of NumPy:

$ spin test -t numpy/\_core/tests

Copy to clipboard

For detailed info on testing, see [Testing builds](https://numpy.org/doc/stable/dev/development_environment.html#testing-builds)

### Running tests in multiple threads[#](https://numpy.org/doc/stable/reference/testing.html#running-tests-in-multiple-threads "Link to this heading")

To help with stress testing NumPy for thread safety, the test suite can be run under [pytest-run-parallel](https://github.com/Quansight-Labs/pytest-run-parallel)
. To install `pytest-run-parallel`:

$ pip install pytest-run-parallel

Copy to clipboard

To run the test suite in multiple threads:

$ spin test -p auto # have pytest-run-parallel detect the number of available cores
$ spin test -p 4 # run each test under 4 threads
$ spin test -p auto -- --skip-thread-unsafe=true # run ONLY tests that are thread-safe

Copy to clipboard

When you write new tests, it is worth testing to make sure they do not fail under `pytest-run-parallel`, since the CI jobs make use of it. Some tips on how to write thread-safe tests can be found [here](https://numpy.org/doc/stable/reference/testing.html#writing-thread-safe-tests)
.

Note

Ideally you should run `pytest-run-parallel` using a [free-threaded build of Python](https://docs.python.org/3/howto/free-threading-python.html)
 that is 3.14 or higher. If you decide to use a version of Python that is not free-threaded, you will need to set the environment variables `PYTHON_CONTEXT_AWARE_WARNINGS` and `PYTHON_THREAD_INHERIT_CONTEXT` to 1.

### Running doctests[#](https://numpy.org/doc/stable/reference/testing.html#running-doctests "Link to this heading")

NumPy documentation contains code examples, “doctests”. To check that the examples are correct, install the `scipy-doctest` package:

$ pip install scipy-doctest

Copy to clipboard

and run one of:

$ spin check-docs -v
$ spin check-docs numpy/linalg
$ spin check-docs -- -k 'det and not slogdet'

Copy to clipboard

Note that the doctests are not run when you use `spin test`.

### Other methods of running tests[#](https://numpy.org/doc/stable/reference/testing.html#other-methods-of-running-tests "Link to this heading")

Run tests using your favourite IDE such as [vscode](https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework)
 or [pycharm](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html)

Writing your own tests[#](https://numpy.org/doc/stable/reference/testing.html#writing-your-own-tests "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

If you are writing code that you’d like to become part of NumPy, please write the tests as you develop your code. Every Python module, extension module, or subpackage in the NumPy package directory should have a corresponding `test_<name>.py` file. Pytest examines these files for test methods (named `test*`) and test classes (named `Test*`).

Suppose you have a NumPy module `numpy/xxx/yyy.py` containing a function `zzz()`. To test this function you would create a test module called `test_yyy.py`. If you only need to test one aspect of `zzz`, you can simply add a test function:

def test\_zzz():
    assert zzz() \== 'Hello from zzz'

Copy to clipboard

More often, we need to group a number of tests together, so we create a test class:

\# import xxx symbols
from numpy.xxx.yyy import zzz
import pytest

class TestZzz:
    def test\_simple(self):
        assert zzz() \== 'Hello from zzz'

    def test\_invalid\_parameter(self):
        with pytest.raises(ValueError, match\='.\*some matching regex.\*'):
            ...

Copy to clipboard

Within these test methods, the `assert` statement or a specialized assertion function is used to test whether a certain assumption is valid. If the assertion fails, the test fails. Common assertion functions include:

*   [`numpy.testing.assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")
     for testing exact elementwise equality between a result array and a reference,
    
*   [`numpy.testing.assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
     for testing near elementwise equality between a result array and a reference (i.e. with specified relative and absolute tolerances), and
    
*   [`numpy.testing.assert_array_less`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html#numpy.testing.assert_array_less "numpy.testing.assert_array_less")
     for testing (strict) elementwise ordering between a result array and a reference.
    

By default, these assertion functions only compare the numerical values in the arrays. Consider using the `strict=True` option to check the array dtype and shape, too.

When you need custom assertions, use the Python `assert` statement. Note that `pytest` internally rewrites `assert` statements to give informative output when it fails, so it should be preferred over the legacy variant `numpy.testing.assert_`. Whereas plain `assert` statements are ignored when running Python in optimized mode with `-O`, this is not an issue when running tests with pytest.

Similarly, the pytest functions [`pytest.raises`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "(in pytest v9.1.1)")
 and [`pytest.warns`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.warns "(in pytest v9.1.1)")
 should be preferred over their legacy counterparts [`numpy.testing.assert_raises`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy.testing.assert_raises "numpy.testing.assert_raises")
 and [`numpy.testing.assert_warns`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html#numpy.testing.assert_warns "numpy.testing.assert_warns")
, which are more broadly used. These versions also accept a `match` parameter, which should always be used to precisely target the intended warning or error.

Note that `test_` functions or methods should not have a docstring, because that makes it hard to identify the test from the output of running the test suite with `verbose=2` (or similar verbosity setting). Use plain comments (`#`) to describe the intent of the test and help the unfamiliar reader to interpret the code.

Also, since much of NumPy is legacy code that was originally written without unit tests, there are still several modules that don’t have tests yet. Please feel free to choose one of these modules and develop tests for it.

### Using C code in tests[#](https://numpy.org/doc/stable/reference/testing.html#using-c-code-in-tests "Link to this heading")

NumPy exposes a rich [C-API](https://numpy.org/doc/stable/reference/c-api/index.html#c-api)
 . These are tested using c-extension modules written “as-if” they know nothing about the internals of NumPy, rather using the official C-API interfaces only. Examples of such modules are tests for a user-defined `rational` dtype in `_rational_tests` or the ufunc machinery tests in `_umath_tests` which are part of the binary distribution. Starting from version 1.21, you can also write snippets of C code in tests that will be compiled locally into c-extension modules and loaded into python.

numpy.testing.extbuild.build\_and\_import\_extension(_modname_, _functions_, _\*_, _prologue\=''_, _build\_dir\=None_, _include\_dirs\=None_, _more\_init\=''_)[#](https://numpy.org/doc/stable/reference/testing.html#numpy.testing.extbuild.build_and_import_extension "Link to this definition")

Build and imports a c-extension module _modname_ from a list of function fragments _functions_.

Parameters:

**functions**list of fragments

Each fragment is a sequence of func\_name, calling convention, snippet.

**prologue**string

Code to precede the rest, usually extra `#include` or `#define` macros.

**build\_dir**pathlib.Path

Where to build the module, usually a temporary directory

**include\_dirs**list

Extra directories to find include files when compiling

**more\_init**string

Code to appear in the module PyMODINIT\_FUNC

Returns:

out: module

The module will have been loaded and is ready for use

Examples

Try it in your browser!

\>>> functions \= \[("test\_bytes", "METH\_O", """\
    if ( !PyBytesCheck(args)) {\
        Py\_RETURN\_FALSE;\
    }\
    Py\_RETURN\_TRUE;\
""")\]
\>>> mod = build\_and\_import\_extension("testme", functions)
\>>> assert not mod.test\_bytes('abc')
\>>> assert mod.test\_bytes(b'abc')

Copy to clipboard

Go BackOpen In Tab

### Labeling tests[#](https://numpy.org/doc/stable/reference/testing.html#labeling-tests "Link to this heading")

Unlabeled tests like the ones above are run in the default `numpy.test()` run. If you want to label your test as slow - and therefore reserved for a full `numpy.test(label='full')` run, you can label it with `pytest.mark.slow`:

import pytest

@pytest.mark.slow
def test\_big(self):
    print('Big, slow test')

Copy to clipboard

Similarly for methods:

class test\_zzz:
    @pytest.mark.slow
    def test\_simple(self):
        assert\_(zzz() \== 'Hello from zzz')

Copy to clipboard

### Setup and teardown methods[#](https://numpy.org/doc/stable/reference/testing.html#setup-and-teardown-methods "Link to this heading")

NumPy originally used xunit setup and teardown, a feature of [`pytest`](https://docs.pytest.org/en/stable/index.html#module-pytest "(in pytest v9.1.1)")
. We now encourage the usage of setup and teardown methods that are called explicitly by the tests that need them:

class TestMe:
    def setup(self):
        print('doing setup')
        return 1

    def teardown(self):
        print('doing teardown')

    def test\_xyz(self):
        x \= self.setup()
        assert x \== 1
        self.teardown()

Copy to clipboard

This approach is thread-safe, ensuring tests can run under `pytest-run-parallel`. Using pytest setup fixtures (such as xunit setup methods) is generally not thread-safe and will likely cause thread-safety test failures.

`pytest` supports more general fixture at various scopes which may be used automatically via special arguments. For example, the special argument name `tmp_path` is used in tests to create temporary directories. However, fixtures should be used sparingly.

### Parametric tests[#](https://numpy.org/doc/stable/reference/testing.html#parametric-tests "Link to this heading")

One very nice feature of `pytest` is the ease of testing across a range of parameter values using the `pytest.mark.parametrize` decorator. For example, suppose you wish to test `linalg.solve` for all combinations of three array sizes and two data types:

@pytest.mark.parametrize('dimensionality', \[3, 10, 25\])
@pytest.mark.parametrize('dtype', \[np.float32, np.float64\])
def test\_solve(dimensionality, dtype):
    np.random.seed(842523)
    A \= np.random.random(size\=(dimensionality, dimensionality)).astype(dtype)
    b \= np.random.random(size\=dimensionality).astype(dtype)
    x \= np.linalg.solve(A, b)
    eps \= np.finfo(dtype).eps
    assert\_allclose(A @ x, b, rtol\=eps\*1e2, atol\=0)
    assert x.dtype \== np.dtype(dtype)

Copy to clipboard

### Doctests[#](https://numpy.org/doc/stable/reference/testing.html#doctests "Link to this heading")

Doctests are a convenient way of documenting the behavior of a function and allowing that behavior to be tested at the same time. The output of an interactive Python session can be included in the docstring of a function, and the test framework can run the example and compare the actual output to the expected output.

The doctests can be run by adding the `doctests` argument to the `test()` call; for example, to run all tests (including doctests) for numpy.lib:

\>>> import numpy as np
\>>> np.lib.test(doctests\=True)

Copy to clipboard

The doctests are run as if they are in a fresh Python instance which has executed `import numpy as np`. Tests that are part of a NumPy subpackage will have that subpackage already imported. E.g. for a test in `numpy/linalg/tests/`, the namespace will be created such that `from numpy import linalg` has already executed.

### `tests/`[#](https://numpy.org/doc/stable/reference/testing.html#tests "Link to this heading")

Rather than keeping the code and the tests in the same directory, we put all the tests for a given subpackage in a `tests/` subdirectory. For our example, if it doesn’t already exist you will need to create a `tests/` directory in `numpy/xxx/`. So the path for `test_yyy.py` is `numpy/xxx/tests/test_yyy.py`.

Once the `numpy/xxx/tests/test_yyy.py` is written, its possible to run the tests by going to the `tests/` directory and typing:

python test\_yyy.py

Copy to clipboard

Or if you add `numpy/xxx/tests/` to the Python path, you could run the tests interactively in the interpreter like this:

\>>> import test\_yyy
\>>> test\_yyy.test()

Copy to clipboard

### `__init__.py` and `setup.py`[#](https://numpy.org/doc/stable/reference/testing.html#init-py-and-setup-py "Link to this heading")

Usually, however, adding the `tests/` directory to the python path isn’t desirable. Instead it would better to invoke the test straight from the module `xxx`. To this end, simply place the following lines at the end of your package’s `__init__.py` file:

...
def test(level\=1, verbosity\=1):
    from numpy.testing import Tester
    return Tester().test(level, verbosity)

Copy to clipboard

You will also need to add the tests directory in the configuration section of your setup.py:

...
def configuration(parent\_package\='', top\_path\=None):
    ...
    config.add\_subpackage('tests')
    return config
...

Copy to clipboard

Now you can do the following to test your module:

\>>> import numpy
\>>> numpy.xxx.test()

Copy to clipboard

Also, when invoking the entire NumPy test suite, your tests will be found and run:

\>>> import numpy
\>>> numpy.test()
\# your tests are included and run automatically!

Copy to clipboard

Tips & Tricks[#](https://numpy.org/doc/stable/reference/testing.html#tips-tricks "Link to this heading")

---------------------------------------------------------------------------------------------------------

### Known failures & skipping tests[#](https://numpy.org/doc/stable/reference/testing.html#known-failures-skipping-tests "Link to this heading")

Sometimes you might want to skip a test or mark it as a known failure, such as when the test suite is being written before the code it’s meant to test, or if a test only fails on a particular architecture.

To skip a test, simply use `skipif`:

import pytest

@pytest.mark.skipif(SkipMyTest, reason\="Skipping this test because...")
def test\_something(foo):
    ...

Copy to clipboard

The test is marked as skipped if `SkipMyTest` evaluates to nonzero, and the message in verbose test output is the second argument given to `skipif`. Similarly, a test can be marked as a known failure by using `xfail`:

import pytest

@pytest.mark.xfail(MyTestFails, reason\="This test is known to fail because...")
def test\_something\_else(foo):
    ...

Copy to clipboard

Of course, a test can be unconditionally skipped or marked as a known failure by using `skip` or `xfail` without argument, respectively.

A total of the number of skipped and known failing tests is displayed at the end of the test run. Skipped tests are marked as `'S'` in the test results (or `'SKIPPED'` for `verbose > 1`), and known failing tests are marked as `'x'` (or `'XFAIL'` if `verbose > 1`).

### Tests on random data[#](https://numpy.org/doc/stable/reference/testing.html#tests-on-random-data "Link to this heading")

Tests on random data are good, but since test failures are meant to expose new bugs or regressions, a test that passes most of the time but fails occasionally with no code changes is not helpful. Make the random data deterministic by setting the random number seed before generating it. Use `rng = numpy.random.RandomState(some_number)` to set a seed on a local instance of [`numpy.random.RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
.

Alternatively, you can use [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)
 to generate arbitrary data. Hypothesis manages both Python’s and Numpy’s random seeds for you, and provides a very concise and powerful way to describe data (including `hypothesis.extra.numpy`, e.g. for a set of mutually-broadcastable shapes).

The advantages over random generation include tools to replay and share failures without requiring a fixed seed, reporting _minimal_ examples for each failure, and better-than-naive-random techniques for triggering bugs.

### Writing thread-safe tests[#](https://numpy.org/doc/stable/reference/testing.html#writing-thread-safe-tests "Link to this heading")

Writing thread-safe tests may require some trial-and-error. Generally you should follow the guidelines stated so far, especially when it comes to [setup methods](https://numpy.org/doc/stable/reference/testing.html#setup-and-teardown-methods)
 and [seeding random data](https://numpy.org/doc/stable/reference/testing.html#tests-on-random-data)
. Explicit setup and the usage of local RNG are thread-safe practices. Here are tips for some other common problems you may run into.

Using `pytest.mark.parametrize` may occasionally cause thread-safety issues. To fix this, you can use `copy()`:

@pytest.mark.parametrize('dimensionality', \[3, 10, 25\])
@pytest.mark.parametrize('dtype', \[np.float32, np.float64\])
def test\_solve(dimensionality, dtype):
    dimen \= dimensionality.copy()
    d \= dtype.copy()
    \# use these copied variables instead
    ...

Copy to clipboard

If you are testing something that is inherently thread-unsafe, you can label your test with `pytest.mark.thread_unsafe` so that it will run under a single thread and not cause test failures:

@pytest.mark.thread\_unsafe(reason\="reason this test is thread-unsafe")
def test\_thread\_unsafe():
  ...

Copy to clipboard

Some examples of what should be labeled as thread-unsafe:

*   Usage of `sys.stdout` and `sys.stderr`
    
*   Mutation of global data, like docstrings, modules, garbage collectors, etc.
    
*   Tests that require a lot of memory, since they could cause crashes.
    

Additionally, some `pytest` fixtures are thread-unsafe, such as `monkeypatch` and `capsys`. However, `pytest-run-parallel` will automatically mark these as thread-unsafe if you decide to use them. Some fixtures have been patched to be thread-safe, like `tmp_path`.

### Documentation for `numpy.test`[#](https://numpy.org/doc/stable/reference/testing.html#documentation-for-numpy-test "Link to this heading")

numpy.test(_label\='fast'_, _verbose\=1_, _extra\_argv\=None_, _doctests\=False_, _coverage\=False_, _durations\=\-1_, _tests\=None_)[#](https://numpy.org/doc/stable/reference/testing.html#numpy.test "Link to this definition")

Pytest test runner.

A test function is typically added to a package’s \_\_init\_\_.py like so:

from numpy.\_pytesttester import PytestTester
test \= PytestTester(\_\_name\_\_).test
del PytestTester

Copy to clipboard

Calling this test function finds and runs all tests associated with the module and all its sub-modules.

Parameters:

**module\_name**module name

The name of the module to test.

Attributes:

**module\_name**str

Full path to the package to test.

Notes

Unlike the previous `nose`\-based implementation, this class is not publicly exposed as it performs some `numpy`\-specific warning suppression.

On this page