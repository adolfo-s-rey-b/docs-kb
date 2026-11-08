[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_array_almost_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_array_almost_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_array_almost_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_array\_almost\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html#numpy-testing-assert-array-almost-equal "Link to this heading")

============================================================================================================================================================================================================

testing.assert\_array\_almost\_equal(_actual_, _desired_, _decimal\=6_, _err\_msg\=''_, _verbose\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1133-L1231)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html#numpy.testing.assert_array_almost_equal "Link to this definition")

Raises an AssertionError if two objects are not equal up to desired precision.

Note

It is recommended to use one of [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
, [`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
 or [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")
 instead of this function for more consistent floating point comparisons.

The test verifies identical shapes and that the elements of `actual` and `desired` satisfy:

abs(desired\-actual) < 1.5 \* 10\*\*(\-decimal)

Copy to clipboard

That is a looser test than originally documented, but agrees with what the actual implementation did up to rounding vagaries. An exception is raised at shape mismatch or conflicting values. In contrast to the standard usage in numpy, NaNs are compared like numbers, no assertion is raised if both objects have NaNs in the same positions.

Parameters:

**actual**array\_like

The actual object to check.

**desired**array\_like

The desired, expected object.

**decimal**int, optional

Desired precision, default is 6.

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

the first assert does not raise an exception

\>>> np.testing.assert\_array\_almost\_equal(\[1.0,2.333,np.nan\],
...                                      \[1.0,2.333,np.nan\])

Copy to clipboard

\>>> np.testing.assert\_array\_almost\_equal(\[1.0,2.33333,np.nan\],
...                                      \[1.0,2.33339,np.nan\], decimal\=5)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not almost equal to 5 decimals

Mismatched elements: 1 / 3 (33.3%)
Mismatch at index:
 \[1\]: 2.33333 (ACTUAL), 2.33339 (DESIRED)
Max absolute difference among violations: 6.e-05
Max relative difference among violations: 2.57136612e-05
 ACTUAL: array(\[1.     , 2.33333,     nan\])
 DESIRED: array(\[1.     , 2.33339,     nan\])

Copy to clipboard

\>>> np.testing.assert\_array\_almost\_equal(\[1.0,2.33333,np.nan\],
...                                      \[1.0,2.33333, 5\], decimal\=5)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not almost equal to 5 decimals

nan location mismatch:
 ACTUAL: array(\[1.     , 2.33333,     nan\])
 DESIRED: array(\[1.     , 2.33333, 5.     \])

Copy to clipboard

Go BackOpen In Tab

On this page