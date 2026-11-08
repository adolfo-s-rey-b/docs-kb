[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_raises.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_raises.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_raises.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_raises.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_raises.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_raises.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_raises.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_raises.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_raises.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_raises.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_raises.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_raises.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_raises.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_raises.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_raises.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_raises.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_raises.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_raises.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_raises.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_raises.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_raises[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy-testing-assert-raises "Link to this heading")

======================================================================================================================================================================

testing.assert\_raises(_exception\_class_, _callable_, _\*args_, _\*\*kwargs) assert\_raises(exception\_class_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1508-L1534)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy.testing.assert_raises "Link to this definition")

testing.assert\_raises(_exception\_class_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

Fail unless an exception of class exception\_class is thrown by callable when invoked with arguments args and keyword arguments kwargs. If a different type of exception is thrown, it will not be caught, and the test case will be deemed to have suffered an error, exactly as for an unexpected exception.

Alternatively, [`assert_raises`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy.testing.assert_raises "numpy.testing.assert_raises")
 can be used as a context manager:

\>>> from numpy.testing import assert\_raises
\>>> with assert\_raises(ZeroDivisionError):
...     1 / 0

Copy to clipboard

is equivalent to

\>>> def div(x, y):
...     return x / y
\>>> assert\_raises(ZeroDivisionError, div, 1, 0)

Copy to clipboard

On this page