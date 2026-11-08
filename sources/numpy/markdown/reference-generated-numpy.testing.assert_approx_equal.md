[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_approx_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_approx_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_approx_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_approx_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_approx_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_approx_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_approx_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_approx_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_approx_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_approx_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_approx_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_approx_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_approx_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_approx_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_approx_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_approx_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_approx_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_approx_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_approx_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_approx_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_approx_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_approx_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_approx\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_approx_equal.html#numpy-testing-assert-approx-equal "Link to this heading")

=========================================================================================================================================================================================

testing.assert\_approx\_equal(_actual_, _desired_, _significant\=7_, _err\_msg\=''_, _verbose\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L639-L735)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_approx_equal.html#numpy.testing.assert_approx_equal "Link to this definition")

Raises an AssertionError if two items are not equal up to significant digits.

Note

It is recommended to use one of [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
, [`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
 or [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")
 instead of this function for more consistent floating point comparisons.

Given two numbers, check that they are approximately equal. Approximately equal is defined as the number of significant digits that agree.

Parameters:

**actual**scalar

The object to check.

**desired**scalar

The expected object.

**significant**int, optional

Desired precision, default is 7.

**err\_msg**str, optional

The error message to be printed in case of failure.

**verbose**bool, optional

If True, the conflicting values are appended to the error message.

Raises:

AssertionError

If actual and desired are not equal up to specified precision.

See also

[`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")

Compare two array\_like objects for equality with desired relative and/or absolute precision.

[`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
, [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")
, [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")

Examples

Try it in your browser!

\>>> np.testing.assert\_approx\_equal(0.12345677777777e-20, 0.1234567e-20)
\>>> np.testing.assert\_approx\_equal(0.12345670e-20, 0.12345671e-20,
...                                significant\=8)
\>>> np.testing.assert\_approx\_equal(0.12345670e-20, 0.12345672e-20,
...                                significant\=8)
Traceback (most recent call last):
    ...
AssertionError:
Items are not equal to 8 significant digits:
 ACTUAL: 1.234567e-21
 DESIRED: 1.2345672e-21

Copy to clipboard

the evaluated condition that raises the exception is

\>>> abs(0.12345670e-20/1e-21 \- 0.12345672e-20/1e-21) \>= 10\*\*-(8\-1)
True

Copy to clipboard

Go BackOpen In Tab

On this page