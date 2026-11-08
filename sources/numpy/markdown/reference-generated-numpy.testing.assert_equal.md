[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy-testing-assert-equal "Link to this heading")

===================================================================================================================================================================

testing.assert\_equal(_actual_, _desired_, _err\_msg\=''_, _verbose\=True_, _\*_, _strict\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L260-L468)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "Link to this definition")

Raises an AssertionError if two objects are not equal.

Given two objects (scalars, lists, tuples, dictionaries or numpy arrays), check that all elements of these objects are equal. An exception is raised at the first conflicting values.

This function handles NaN comparisons as if NaN was a “normal” number. That is, AssertionError is not raised if both objects have NaNs in the same positions. This is in contrast to the IEEE standard on NaNs, which says that NaN compared to anything must return False.

Parameters:

**actual**array\_like

The object to check.

**desired**array\_like

The expected object.

**err\_msg**str, optional

The error message to be printed in case of failure.

**verbose**bool, optional

If True, the conflicting values are appended to the error message.

**strict**bool, optional

If True and either of the _actual_ and _desired_ arguments is an array, raise an `AssertionError` when either the shape or the data type of the arguments does not match. If neither argument is an array, this parameter has no effect.

New in version 2.0.0.

Raises:

AssertionError

If actual and desired are not equal.

See also

[`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")

[`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")

[`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")

Notes

When one of _actual_ and _desired_ is a scalar and the other is array\_like, the function checks that each element of the array\_like is equal to the scalar. Note that empty arrays are therefore considered equal to scalars. This behaviour can be disabled by setting `strict==True`.

Examples

Try it in your browser!

\>>> np.testing.assert\_equal(\[4, 5\], \[4, 6\])
Traceback (most recent call last):
    ...
AssertionError:
Items are not equal:
item=1
 ACTUAL: 5
 DESIRED: 6

Copy to clipboard

The following comparison does not raise an exception. There are NaNs in the inputs, but they are in the same positions.

\>>> np.testing.assert\_equal(np.array(\[1.0, 2.0, np.nan\]), \[1, 2, np.nan\])

Copy to clipboard

As mentioned in the Notes section, [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")
 has special handling for scalars when one of the arguments is an array. Here, the test checks that each value in _x_ is 3:

\>>> x \= np.full((2, 5), fill\_value\=3)
\>>> np.testing.assert\_equal(x, 3)

Copy to clipboard

Use _strict_ to raise an AssertionError when comparing a scalar with an array of a different shape:

\>>> np.testing.assert\_equal(x, 3, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not equal

(shapes (2, 5), () mismatch)
 ACTUAL: array(\[\[3, 3, 3, 3, 3\],\
       \[3, 3, 3, 3, 3\]\])
 DESIRED: array(3)

Copy to clipboard

The _strict_ parameter also ensures that the array data types match:

\>>> x \= np.array(\[2, 2, 2\])
\>>> y \= np.array(\[2., 2., 2.\], dtype\=np.float32)
\>>> np.testing.assert\_equal(x, y, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not equal

(dtypes int64, float32 mismatch)
 ACTUAL: array(\[2, 2, 2\])
 DESIRED: array(\[2., 2., 2.\], dtype=float32)

Copy to clipboard

Go BackOpen In Tab

On this page