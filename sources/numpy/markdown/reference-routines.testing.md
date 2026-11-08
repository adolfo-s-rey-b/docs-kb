[Skip to main content](https://numpy.org/doc/stable/reference/routines.testing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.testing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.testing.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.testing.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.testing.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.testing.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.testing.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.testing.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.testing.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.testing.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.testing.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.testing.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.testing.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.testing.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.testing.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.testing.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.testing.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.testing.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.testing.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.testing.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.testing.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.testing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Test support[#](https://numpy.org/doc/stable/reference/routines.testing.html#test-support "Link to this heading")

==================================================================================================================

Common test support for all numpy test scripts.

This single module should provide all the common functionality for numpy tests in a single location, so that [test scripts](https://numpy.org/doc/stable/dev/development_environment.html#development-environment)
 can just import it and work right away. For background, see the [Testing guidelines](https://numpy.org/doc/stable/reference/testing.html#testing-guidelines)

Asserts[#](https://numpy.org/doc/stable/reference/routines.testing.html#asserts "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")<br>(actual, desired\[, rtol, ...\]) | Raises an AssertionError if two objects are not equal up to desired tolerance. |
| [`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")<br>(x, y\[, nulp\]) | Compare two arrays relatively to their spacing. |
| [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")<br>(a, b\[, maxulp, dtype\]) | Check that all items of arrays differ in at most N Units in the Last Place. |
| [`assert_array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy.testing.assert_array_equal "numpy.testing.assert_array_equal")<br>(actual, desired\[, ...\]) | Raises an AssertionError if two array\_like objects are not equal. |
| [`assert_array_less`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html#numpy.testing.assert_array_less "numpy.testing.assert_array_less")<br>(x, y\[, err\_msg, verbose, ...\]) | Raises an AssertionError if two array\_like objects are not ordered by less than. |
| [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")<br>(actual, desired\[, err\_msg, ...\]) | Raises an AssertionError if two objects are not equal. |
| [`assert_raises`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy.testing.assert_raises "numpy.testing.assert_raises")<br>(assert\_raises) | Fail unless an exception of class exception\_class is thrown by callable when invoked with arguments args and keyword arguments kwargs. |
| [`assert_raises_regex`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises_regex.html#numpy.testing.assert_raises_regex "numpy.testing.assert_raises_regex")<br>(exception\_class, ...) | Fail unless an exception of class exception\_class and with message that matches expected\_regexp is thrown by callable when invoked with arguments args and keyword arguments kwargs. |
| [`assert_warns`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html#numpy.testing.assert_warns "numpy.testing.assert_warns")<br>(warning\_class, \*args, \*\*kwargs) | Fail unless the given callable throws the specified warning. |
| [`assert_no_warnings`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_warnings.html#numpy.testing.assert_no_warnings "numpy.testing.assert_no_warnings")<br>(\*args, \*\*kwargs) | Fail if the given callable produces any warnings. |
| [`assert_no_gc_cycles`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_gc_cycles.html#numpy.testing.assert_no_gc_cycles "numpy.testing.assert_no_gc_cycles")<br>(\*args, \*\*kwargs) | Fail if the given callable produces any reference cycles. |
| [`assert_string_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html#numpy.testing.assert_string_equal "numpy.testing.assert_string_equal")<br>(actual, desired) | Test if two strings are equal. |

Asserts (not recommended)[#](https://numpy.org/doc/stable/reference/routines.testing.html#asserts-not-recommended "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

It is recommended to use one of [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
, [`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
 or [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")
 instead of these functions for more consistent floating point comparisons.

|     |     |
| --- | --- |
| [`assert_`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_.html#numpy.testing.assert_ "numpy.testing.assert_")<br>(val\[, msg\]) | Assert that works in release mode. |
| [`assert_almost_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_almost_equal.html#numpy.testing.assert_almost_equal "numpy.testing.assert_almost_equal")<br>(actual, desired\[, ...\]) | Raises an AssertionError if two items are not equal up to desired precision. |
| [`assert_approx_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_approx_equal.html#numpy.testing.assert_approx_equal "numpy.testing.assert_approx_equal")<br>(actual, desired\[, ...\]) | Raises an AssertionError if two items are not equal up to significant digits. |
| [`assert_array_almost_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html#numpy.testing.assert_array_almost_equal "numpy.testing.assert_array_almost_equal")<br>(actual, desired\[, ...\]) | Raises an AssertionError if two objects are not equal up to desired precision. |
| [`print_assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.print_assert_equal.html#numpy.testing.print_assert_equal "numpy.testing.print_assert_equal")<br>(test\_string, actual, desired) | Test if two objects are equal, and print an error message if test fails. |

Decorators[#](https://numpy.org/doc/stable/reference/routines.testing.html#decorators "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`decorate_methods`](https://numpy.org/doc/stable/reference/generated/numpy.testing.decorate_methods.html#numpy.testing.decorate_methods "numpy.testing.decorate_methods")<br>(cls, decorator\[, testmatch\]) | Apply a decorator to all methods in a class matching a regular expression. |

Test running[#](https://numpy.org/doc/stable/reference/routines.testing.html#test-running "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`clear_and_catch_warnings`](https://numpy.org/doc/stable/reference/generated/numpy.testing.clear_and_catch_warnings.html#numpy.testing.clear_and_catch_warnings "numpy.testing.clear_and_catch_warnings")<br>(\[record, modules\]) | Context manager that resets warning registry for catching warnings |
| [`measure`](https://numpy.org/doc/stable/reference/generated/numpy.testing.measure.html#numpy.testing.measure "numpy.testing.measure")<br>(code\_str\[, times, label\]) | Return elapsed time for executing code in the namespace of the caller. |
| [`rundocs`](https://numpy.org/doc/stable/reference/generated/numpy.testing.rundocs.html#numpy.testing.rundocs "numpy.testing.rundocs")<br>(\[filename, raise\_on\_error\]) | Run doctests found in the given file. |
| [`suppress_warnings`](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.html#numpy.testing.suppress_warnings "numpy.testing.suppress_warnings")<br>(\[forwarding\_rule, \_warn\]) | Context manager and decorator doing much the same as `warnings.catch_warnings`. |

Testing custom array containers ([`numpy.testing.overrides`](https://numpy.org/doc/stable/reference/routines.testing.html#module-numpy.testing.overrides "numpy.testing.overrides")
)[#](https://numpy.org/doc/stable/reference/routines.testing.html#testing-custom-array-containers-numpy-testing-overrides "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These functions can be useful when testing custom array container implementations which make use of `__array_ufunc__`/`__array_function__`.

|     |     |
| --- | --- |
| [`allows_array_function_override`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_function_override.html#numpy.testing.overrides.allows_array_function_override "numpy.testing.overrides.allows_array_function_override")<br>(func) | Determine if a Numpy function can be overridden via _\_\_array\_function\_\__ |
| [`allows_array_ufunc_override`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_ufunc_override.html#numpy.testing.overrides.allows_array_ufunc_override "numpy.testing.overrides.allows_array_ufunc_override")<br>(func) | Determine if a function can be overridden via _\_\_array\_ufunc\_\__ |
| [`get_overridable_numpy_ufuncs`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.get_overridable_numpy_ufuncs.html#numpy.testing.overrides.get_overridable_numpy_ufuncs "numpy.testing.overrides.get_overridable_numpy_ufuncs")<br>() | List all numpy ufuncs overridable via _\_\_array\_ufunc\_\__ |
| [`get_overridable_numpy_array_functions`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.get_overridable_numpy_array_functions.html#numpy.testing.overrides.get_overridable_numpy_array_functions "numpy.testing.overrides.get_overridable_numpy_array_functions")<br>() | List all numpy functions overridable via _\_\_array\_function\_\__ |

Guidelines[#](https://numpy.org/doc/stable/reference/routines.testing.html#guidelines "Link to this heading")

--------------------------------------------------------------------------------------------------------------

*   [Testing guidelines](https://numpy.org/doc/stable/reference/testing.html)
    *   [Introduction](https://numpy.org/doc/stable/reference/testing.html#introduction)
        
    *   [Testing NumPy](https://numpy.org/doc/stable/reference/testing.html#testing-numpy)
        *   [Running tests from inside Python](https://numpy.org/doc/stable/reference/testing.html#running-tests-from-inside-python)
            
        *   [Running tests from the command line](https://numpy.org/doc/stable/reference/testing.html#running-tests-from-the-command-line)
            
        *   [Running tests in multiple threads](https://numpy.org/doc/stable/reference/testing.html#running-tests-in-multiple-threads)
            
        *   [Running doctests](https://numpy.org/doc/stable/reference/testing.html#running-doctests)
            
        *   [Other methods of running tests](https://numpy.org/doc/stable/reference/testing.html#other-methods-of-running-tests)
            
    *   [Writing your own tests](https://numpy.org/doc/stable/reference/testing.html#writing-your-own-tests)
        *   [Using C code in tests](https://numpy.org/doc/stable/reference/testing.html#using-c-code-in-tests)
            *   [`build_and_import_extension`](https://numpy.org/doc/stable/reference/testing.html#numpy.testing.extbuild.build_and_import_extension)
                
        *   [Labeling tests](https://numpy.org/doc/stable/reference/testing.html#labeling-tests)
            
        *   [Setup and teardown methods](https://numpy.org/doc/stable/reference/testing.html#setup-and-teardown-methods)
            
        *   [Parametric tests](https://numpy.org/doc/stable/reference/testing.html#parametric-tests)
            
        *   [Doctests](https://numpy.org/doc/stable/reference/testing.html#doctests)
            
        *   [`tests/`](https://numpy.org/doc/stable/reference/testing.html#tests)
            
        *   [`__init__.py` and `setup.py`](https://numpy.org/doc/stable/reference/testing.html#init-py-and-setup-py)
            
    *   [Tips & Tricks](https://numpy.org/doc/stable/reference/testing.html#tips-tricks)
        *   [Known failures & skipping tests](https://numpy.org/doc/stable/reference/testing.html#known-failures-skipping-tests)
            
        *   [Tests on random data](https://numpy.org/doc/stable/reference/testing.html#tests-on-random-data)
            
        *   [Writing thread-safe tests](https://numpy.org/doc/stable/reference/testing.html#writing-thread-safe-tests)
            
        *   [Documentation for `numpy.test`](https://numpy.org/doc/stable/reference/testing.html#documentation-for-numpy-test)
            *   [`test`](https://numpy.org/doc/stable/reference/testing.html#numpy.test)
                

On this page