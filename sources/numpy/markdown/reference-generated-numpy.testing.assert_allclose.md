[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_allclose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_allclose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_allclose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_allclose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_allclose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_allclose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_allclose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_allclose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_allclose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_allclose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_allclose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_allclose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_allclose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_allclose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_allclose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_allclose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_allclose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_allclose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_allclose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_allclose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_allclose[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy-testing-assert-allclose "Link to this heading")

============================================================================================================================================================================

testing.assert\_allclose(_actual_, _desired_, _rtol\=1e-07_, _atol\=0_, _equal\_nan\=True_, _err\_msg\=''_, _verbose\=True_, _\*_, _strict\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1671-L1782)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "Link to this definition")

Raises an AssertionError if two objects are not equal up to desired tolerance.

Given two array\_like objects, check that their shapes and all elements are equal (but see the Notes for the special handling of a scalar). An exception is raised if the shapes mismatch or any values conflict. In contrast to the standard usage in numpy, NaNs are compared like numbers, no assertion is raised if both objects have NaNs in the same positions.

The test is equivalent to `allclose(actual, desired, rtol, atol)`, except that it is stricter: it doesn’t broadcast its operands, and has tighter default tolerance values. It compares the difference between _actual_ and _desired_ to `atol + rtol * abs(desired)`.

Parameters:

**actual**array\_like

Array obtained.

**desired**array\_like

Array desired.

**rtol**float, optional

Relative tolerance.

**atol**float | np.timedelta64, optional

Absolute tolerance.

**equal\_nan**bool, optional.

If True, NaNs will compare equal.

**err\_msg**str, optional

The error message to be printed in case of failure.

**verbose**bool, optional

If True, the conflicting values are appended to the error message.

**strict**bool, optional

If True, raise an `AssertionError` when either the shape or the data type of the arguments does not match. The special handling of scalars mentioned in the Notes section is disabled.

New in version 2.0.0.

Raises:

AssertionError

If actual and desired are not equal up to specified precision.

See also

[`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
, [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")

Notes

When one of _actual_ and _desired_ is a scalar and the other is array\_like, the function performs the comparison as if the scalar were broadcasted to the shape of the array. Note that empty arrays are therefore considered equal to scalars. This behaviour can be disabled by setting `strict==True`.

Examples

Try it in your browser!

\>>> x \= \[1e-5, 1e-3, 1e-1\]
\>>> y \= np.arccos(np.cos(x))
\>>> np.testing.assert\_allclose(x, y, rtol\=1e-5, atol\=0)

Copy to clipboard

As mentioned in the Notes section, [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
 has special handling for scalars. Here, the test checks that the value of [`numpy.sin`](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
 is nearly zero at integer multiples of π.

\>>> x \= np.arange(3) \* np.pi
\>>> np.testing.assert\_allclose(np.sin(x), 0, atol\=1e-15)

Copy to clipboard

Use _strict_ to raise an `AssertionError` when comparing an array with one or more dimensions against a scalar.

\>>> np.testing.assert\_allclose(np.sin(x), 0, atol\=1e-15, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Not equal to tolerance rtol=1e-07, atol=1e-15

(shapes (3,), () mismatch)
 ACTUAL: array(\[ 0.000000e+00,  1.224647e-16, -2.449294e-16\])
 DESIRED: array(0)

Copy to clipboard

The _strict_ parameter also ensures that the array data types match:

\>>> y \= np.zeros(3, dtype\=np.float32)
\>>> np.testing.assert\_allclose(np.sin(x), y, atol\=1e-15, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Not equal to tolerance rtol=1e-07, atol=1e-15

(dtypes float64, float32 mismatch)
 ACTUAL: array(\[ 0.000000e+00,  1.224647e-16, -2.449294e-16\])
 DESIRED: array(\[0., 0., 0.\], dtype=float32)

Copy to clipboard

Go BackOpen In Tab

On this page