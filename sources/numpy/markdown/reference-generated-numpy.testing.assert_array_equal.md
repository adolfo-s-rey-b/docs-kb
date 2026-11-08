[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.assert_array_equal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.assert_array_equal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.assert_array_equal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.assert_array_equal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.assert_array_equal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.assert_array_equal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.assert_array_equal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.assert_array_equal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.assert_array_equal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.assert_array_equal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.assert_array_equal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.assert_array_equal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.assert_array_equal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.assert_array_equal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.assert_array_equal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.assert_array_equal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.assert_array_equal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.assert_array_equal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.assert_array_equal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.assert_array_equal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_array\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy-testing-assert-array-equal "Link to this heading")

======================================================================================================================================================================================

testing.assert\_array\_equal(_actual_, _desired_, _err\_msg\=''_, _verbose\=True_, _\*_, _strict\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L999-L1130)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy.testing.assert_array_equal "Link to this definition")

Raises an AssertionError if two array\_like objects are not equal.

Given two array\_like objects, check that the shape is equal and all elements of these objects are equal (but see the Notes for the special handling of a scalar). An exception is raised at shape mismatch or conflicting values. In contrast to the standard usage in numpy, NaNs are compared like numbers, no assertion is raised if both objects have NaNs in the same positions.

The usual caution for verifying equality with floating point numbers is advised.

Note

When either _actual_ or _desired_ is already an instance of [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 and _desired_ is not a `dict`, the behavior of `assert_equal(actual, desired)` is identical to the behavior of this function. Otherwise, this function performs _np.asanyarray_ on the inputs before comparison, whereas [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")
 defines special comparison rules for common Python types. For example, only [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")
 can be used to compare nested Python lists. In new code, consider using only [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")
, explicitly converting either _actual_ or _desired_ to arrays if the behavior of [`assert_array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy.testing.assert_array_equal "numpy.testing.assert_array_equal")
 is desired.

Parameters:

**actual**array\_like

The actual object to check.

**desired**array\_like

The desired, expected object.

**err\_msg**str, optional

The error message to be printed in case of failure.

**verbose**bool, optional

If True, the conflicting values are appended to the error message.

**strict**bool, optional

If True, raise an AssertionError when either the shape or the data type of the array\_like objects does not match. The special handling for scalars mentioned in the Notes section is disabled.

New in version 1.24.0.

Raises:

AssertionError

If actual and desired objects are not equal.

See also

[`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")

Compare two array\_like objects for equality with desired relative and/or absolute precision.

[`assert_array_almost_equal_nulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_almost_equal_nulp.html#numpy.testing.assert_array_almost_equal_nulp "numpy.testing.assert_array_almost_equal_nulp")
, [`assert_array_max_ulp`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_max_ulp.html#numpy.testing.assert_array_max_ulp "numpy.testing.assert_array_max_ulp")
, [`assert_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal "numpy.testing.assert_equal")

Notes

When one of _actual_ and _desired_ is a scalar and the other is array\_like, the function checks that each element of the array\_like is equal to the scalar. Note that empty arrays are therefore considered equal to scalars. This behaviour can be disabled by setting `strict==True`.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

The first assert does not raise an exception:

\>>> np.testing.assert\_array\_equal(\[1.0,2.33333,np.nan\],
...                               \[np.exp(0),2.33333, np.nan\])

Copy to clipboard

Assert fails with numerical imprecision with floats:

\>>> np.testing.assert\_array\_equal(\[1.0,np.pi,np.nan\],
...                               \[1, np.sqrt(np.pi)\*\*2, np.nan\])
Traceback (most recent call last):
    ...
AssertionError:
Arrays are not equal

Mismatched elements: 1 / 3 (33.3%)
Mismatch at index:
 \[1\]: 3.141592653589793 (ACTUAL), 3.1415926535897927 (DESIRED)
Max absolute difference among violations: 4.4408921e-16
Max relative difference among violations: 1.41357986e-16
 ACTUAL: array(\[1.      , 3.141593,      nan\])
 DESIRED: array(\[1.      , 3.141593,      nan\])

Copy to clipboard

Use [`assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose "numpy.testing.assert_allclose")
 or one of the nulp (number of floating point values) functions for these cases instead:

\>>> np.testing.assert\_allclose(\[1.0,np.pi,np.nan\],
...                            \[1, np.sqrt(np.pi)\*\*2, np.nan\],
...                            rtol\=1e-10, atol\=0)

Copy to clipboard

As mentioned in the Notes section, [`assert_array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_array_equal.html#numpy.testing.assert_array_equal "numpy.testing.assert_array_equal")
 has special handling for scalars. Here the test checks that each value in _x_ is 3:

\>>> x \= np.full((2, 5), fill\_value\=3)
\>>> np.testing.assert\_array\_equal(x, 3)

Copy to clipboard

Use _strict_ to raise an AssertionError when comparing a scalar with an array:

\>>> np.testing.assert\_array\_equal(x, 3, strict\=True)
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
\>>> np.testing.assert\_array\_equal(x, y, strict\=True)
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