[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_array_max_ulp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_array_max_ulp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_array_max_ulp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_array\_max\_ulp[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy-testing-assert-array-max-ulp "Link to this heading")

=============================================================================================================================================================================================

testing.assert\_array\_max\_ulp(_a_, _b_, _maxulp\=1_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1848-L1896)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "Link to this definition")

Check that all items of arrays differ in at most N Units in the Last Place.

Parameters:

**a, b**array\_like

Input arrays to be compared.

**maxulp**int, optional

The maximum number of units in the last place that elements of _a_ and _b_ can differ. Default is 1.

**dtype**dtype, optional

Data-type to convert _a_ and _b_ to if given. Default is None.

Returns:

**ret**ndarray

Array containing number of representable floating point numbers between items in _a_ and _b_.

Raises:

AssertionError

If one or more elements differ by more than _maxulp_.

See also

[`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")

Compare two arrays relatively to their spacing.

Notes

For computing the ULP difference, this API does not differentiate between various representations of NAN (ULP difference between 0x7fc00000 and 0xffc00000 is zero).

Examples

Try it in your browser!

\>>> a \= np.linspace(0., 1., 100)
\>>> res \= np.testing.assert\_array\_max\_ulp(a, np.arcsin(np.sin(a)))

Copy to clipboard

Go BackOpen In Tab

On this page