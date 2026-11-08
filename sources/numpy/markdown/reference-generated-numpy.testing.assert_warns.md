[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_warns.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_warns.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_warns.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_warns.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_warns.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_warns.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_warns.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_warns.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_warns.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_warns.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_warns.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_warns.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_warns.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_warns.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_warns.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_warns.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_warns.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_warns.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_warns.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_warns.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_warns[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html#numpy-testing-assert-warns "Link to this heading")

===================================================================================================================================================================

testing.assert\_warns(_warning\_class_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2000-L2066)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_warns.html#numpy.testing.assert_warns "Link to this definition")

Fail unless the given callable throws the specified warning.

A warning of class warning\_class should be thrown by the callable when invoked with arguments args and keyword arguments kwargs. If a different type of warning is thrown, it will not be caught.

If called with all arguments other than the warning class omitted, may be used as a context manager:

with assert\_warns(SomeWarning):
    do\_something()

Copy to clipboard

The ability to be used as a context manager is new in NumPy v1.11.0.

Deprecated since version 2.4: This is deprecated. Use [`warnings.catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "(in Python v3.14)")
 or `pytest.warns` instead.

Parameters:

**warning\_class**class

The class defining the warning that _func_ is expected to throw.

**func**callable, optional

Callable to test

**\*args**Arguments

Arguments for _func_.

**\*\*kwargs**Kwargs

Keyword arguments for _func_.

Returns:

The value returned by _func_.

Examples

Try it in your browser!

\>>> import warnings
\>>> def deprecated\_func(num):
...     warnings.warn("Please upgrade", DeprecationWarning)
...     return num\*num
\>>> with np.testing.assert\_warns(DeprecationWarning):
...     assert deprecated\_func(4) \== 16
\>>> \# or passing a func
\>>> ret \= np.testing.assert\_warns(DeprecationWarning, deprecated\_func, 4)
\>>> assert ret \== 16

Copy to clipboard

Go BackOpen In Tab

On this page