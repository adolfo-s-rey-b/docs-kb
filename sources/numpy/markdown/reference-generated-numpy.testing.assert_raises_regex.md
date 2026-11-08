[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises_regex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_raises_regex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises_regex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_raises_regex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_raises_regex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_raises_regex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_raises_regex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_raises_regex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_raises_regex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_raises_regex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_raises_regex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_raises_regex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_raises_regex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_raises_regex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_raises_regex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_raises_regex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_raises_regex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_raises_regex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_raises_regex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_raises_regex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_raises_regex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_raises_regex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_raises\_regex[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises_regex.html#numpy-testing-assert-raises-regex "Link to this heading")

=========================================================================================================================================================================================

testing.assert\_raises\_regex(_exception\_class_, _expected\_regexp_, _callable_, _\*args_, _\*\*kwargs) assert\_raises\_regex(exception\_class_, _expected\_regexp_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1537-L1550)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises_regex.html#numpy.testing.assert_raises_regex "Link to this definition")

Fail unless an exception of class exception\_class and with message that matches expected\_regexp is thrown by callable when invoked with arguments args and keyword arguments kwargs.

Alternatively, can be used as a context manager like [`assert_raises`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_raises.html#numpy.testing.assert_raises "numpy.testing.assert_raises")
.

On this page