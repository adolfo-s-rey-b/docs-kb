[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_array\_almost\_equal\_nulp[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy-testing-assert-array-almost-equal-nulp "Link to this heading")

============================================================================================================================================================================================================================

testing.assert\_array\_almost\_equal\_nulp(_x_, _y_, _nulp\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1785-L1845)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "Link to this definition")

Compare two arrays relatively to their spacing.

This is a relatively robust method to compare two arrays whose amplitude is variable.

Parameters:

**x, y**array\_like

Input arrays.

**nulp**int, optional

The maximum number of unit in the last place for tolerance (see Notes). Default is 1.

Returns:

None

Raises:

AssertionError

If the spacing between _x_ and _y_ for one or more elements is larger than _nulp_.

See also

[`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")

Check that all items of arrays differ in at most N Units in the Last Place.

[`spacing`](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy.spacing "numpy.spacing")

Return the distance between x and the nearest adjacent number.

Notes

An assertion is raised if the following condition is not met:

abs(x \- y) <= nulp \* spacing(maximum(abs(x), abs(y)))

Copy to clipboard

Examples

Try it in your browser!

\>>> x \= np.array(\[1., 1e-10, 1e-20\])
\>>> eps \= np.finfo(x.dtype).eps
\>>> np.testing.assert\_array\_almost\_equal\_nulp(x, x\*eps/2 + x)

Copy to clipboard

\>>> np.testing.assert\_array\_almost\_equal\_nulp(x, x\*eps + x)
Traceback (most recent call last):
  ...
AssertionError: Arrays are not equal to 1 ULP (max is 2)

Copy to clipboard

Go BackOpen In Tab

On this page