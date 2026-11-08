[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_string_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_string_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_string_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_string_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_string_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_string_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_string_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_string_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_string_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_string_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_string_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_string_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_string_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_string_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_string_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_string_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_string_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_string_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_string_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_string_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_string\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html#numpy-testing-assert-string-equal "Link to this heading")

=========================================================================================================================================================================================

testing.assert\_string\_equal(_actual_, _desired_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1355-L1423)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html#numpy.testing.assert_string_equal "Link to this definition")

Test if two strings are equal.

If the given strings are equal, [`assert_string_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_string_equal.html#numpy.testing.assert_string_equal "numpy.testing.assert_string_equal")
 does nothing. If they are not equal, an AssertionError is raised, and the diff between the strings is shown.

Parameters:

**actual**str

The string to test for equality against the expected string.

**desired**str

The expected string.

Examples

Try it in your browser!

\>>> np.testing.assert\_string\_equal('abc', 'abc')
\>>> np.testing.assert\_string\_equal('abc', 'abcd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Differences in strings:
\- abc+ abcd?    +

Copy to clipboard

Go BackOpen In Tab

On this page