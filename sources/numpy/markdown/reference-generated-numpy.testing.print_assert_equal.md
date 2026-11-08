[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.print_assert_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.print_assert_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.print_assert_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.print_assert_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.print_assert_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.print_assert_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.print_assert_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.print_assert_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.print_assert_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.print_assert_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.print_assert_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.print_assert_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.print_assert_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.print_assert_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.print_assert_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.print_assert_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.print_assert_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.print_assert_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.print_assert_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.print_assert_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.print_assert_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.print_assert_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.print\_assert\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.print_assert_equal.html#numpy-testing-print-assert-equal "Link to this heading")

======================================================================================================================================================================================

testing.print\_assert\_equal(_test\_string_, _actual_, _desired_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L471-L509)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.print_assert_equal.html#numpy.testing.print_assert_equal "Link to this definition")

Test if two objects are equal, and print an error message if test fails.

The test is performed with `actual == desired`.

Parameters:

**test\_string**str

The message supplied to AssertionError.

**actual**object

The object to test for equality against _desired_.

**desired**object

The expected result.

Examples

Try it in your browser!

\>>> np.testing.print\_assert\_equal('Test XYZ of func xyz', \[0, 1\], \[0, 1\])
\>>> np.testing.print\_assert\_equal('Test XYZ of func xyz', \[0, 1\], \[0, 2\])
Traceback (most recent call last):
...
AssertionError: Test XYZ of func xyz failed
ACTUAL:
\[0, 1\]
DESIRED:
\[0, 2\]

Copy to clipboard

Go BackOpen In Tab

On this page