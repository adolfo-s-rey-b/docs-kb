[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_array_less.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_array_less.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_array_less.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_array_less.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_array_less.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_array_less.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_array_less.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_array_less.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_array_less.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_array_less.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_array_less.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_array_less.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_array_less.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_array_less.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_array_less.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_array_less.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_array_less.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_array_less.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_array_less.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_array_less.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_array\_less[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html#numpy-testing-assert-array-less "Link to this heading")

===================================================================================================================================================================================

testing.assert\_array\_less(_x_, _y_, _err\_msg\=''_, _verbose\=True_, _\*_, _strict\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L1234-L1348)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_less.html#numpy.testing.assert_array_less "Link to this definition")

Raises an AssertionError if two array\_like objects are not ordered by less than.

Given two array\_like objects _x_ and _y_, check that the shape is equal and all elements of _x_ are strictly less than the corresponding elements of _y_ (but see the Notes for the special handling of a scalar). An exception is raised at shape mismatch or values that are not correctly ordered. In contrast to the standard usage in NumPy, no assertion is raised if both objects have NaNs in the same positions.

Parameters:

**x**array\_like

The smaller object to check.

**y**array\_like

The larger object to compare.

**err\_msg**string

The error message to be printed in case of failure.

**verbose**bool

If True, the conflicting values are appended to the error message.

**strict**bool, optional

If True, raise an AssertionError when either the shape or the data type of the array\_like objects does not match. The special handling for scalars mentioned in the Notes section is disabled.

New in version 2.0.0.

Raises:

AssertionError

If x is not strictly smaller than y, element-wise.

See also

[`assert_array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy.testing.assert_array_equal "numpy.testing.assert_array_equal")

tests objects for equality

[`assert_array_almost_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal.html#numpy.testing.assert_array_almost_equal "numpy.testing.assert_array_almost_equal")

test objects for equality up to precision

Notes

When one of _x_ and _y_ is a scalar and the other is array\_like, the function performs the comparison as though the scalar were broadcasted to the shape of the array. This behaviour can be disabled with the _strict_ parameter.

Examples

Try it in your browser!

The following assertion passes because each finite element of _x_ is strictly less than the corresponding element of _y_, and the NaNs are in corresponding locations.

\>>> x \= \[1.0, 1.0, np.nan\]
\>>> y \= \[1.1, 2.0, np.nan\]
\>>> np.testing.assert\_array\_less(x, y)

Copy to clipboard

The following assertion fails because the zeroth element of _x_ is no longer strictly less than the zeroth element of _y_.

\>>> y\[0\] \= 1
\>>> np.testing.assert\_array\_less(x, y)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not strictly ordered \`x < y\`

Mismatched elements: 1 / 3 (33.3%)
Mismatch at index:
 \[0\]: 1.0 (x), 1.0 (y)
Max absolute difference among violations: 0.
Max relative difference among violations: 0.
 x: array(\[ 1.,  1., nan\])
 y: array(\[ 1.,  2., nan\])

Copy to clipboard

Here, _y_ is a scalar, so each element of _x_ is compared to _y_, and the assertion passes.

\>>> x \= \[1.0, 4.0\]
\>>> y \= 5.0
\>>> np.testing.assert\_array\_less(x, y)

Copy to clipboard

However, with `strict=True`, the assertion will fail because the shapes do not match.

\>>> np.testing.assert\_array\_less(x, y, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not strictly ordered \`x < y\`

(shapes (2,), () mismatch)
 x: array(\[1., 4.\])
 y: array(5.)

Copy to clipboard

With `strict=True`, the assertion also fails if the dtypes of the two arrays do not match.

\>>> y \= \[5, 5\]
\>>> np.testing.assert\_array\_less(x, y, strict\=True)
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not strictly ordered \`x < y\`

(dtypes float64, int64 mismatch)
 x: array(\[1., 4.\])
 y: array(\[5, 5\])

Copy to clipboard

Go BackOpen In Tab

On this page