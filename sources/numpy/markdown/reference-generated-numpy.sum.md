[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.sum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.sum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.sum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.sum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.sum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.sum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.sum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.sum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.sum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.sum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.sum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.sum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.sum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.sum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.sum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.sum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.sum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.sum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.sum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.sum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sum[#](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy-sum "Link to this heading")

===============================================================================================================

numpy.sum(_a_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2342-L2466)
[#](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "Link to this definition")

Sum of array elements over a given axis.

Parameters:

**a**array\_like

Elements to sum.

**axis**None or int or tuple of ints, optional

Axis or axes along which a sum is performed. The default, axis=None, will sum all of the elements of the input array. If axis is negative it counts from the last to the first axis. If axis is a tuple of ints, a sum is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.

**dtype**dtype, optional

The type of the returned array and of the accumulator in which the elements are summed. The dtype of _a_ is used by default unless _a_ has an integer dtype of less precision than the default platform integer. In that case, if _a_ is signed then the platform integer is used while if _a_ is unsigned then an unsigned integer of the same precision as the platform integer is used.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape as the expected output, but the type of the output values will be cast if necessary.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

Starting value for the sum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

**where**array\_like of bool, optional

Elements to include in the sum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

Returns:

**sum\_along\_axis**ndarray

An array with the same shape as _a_, with the specified axis removed. If _a_ is a 0-d array, or if _axis_ is None, a scalar is returned. If an output array is specified, a reference to _out_ is returned.

See also

[`ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")

Equivalent method.

[`add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")

`numpy.add.reduce` equivalent function.

[`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")

Cumulative sum of array elements.

[`trapezoid`](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy.trapezoid "numpy.trapezoid")

Integration of array values using composite trapezoidal rule.

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
, [`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow.

The sum of an empty array is the neutral element 0:

\>>> np.sum(\[\])
0.0

Copy to clipboard

For floating point numbers the numerical precision of sum (and `np.add.reduce`) is in general limited by directly adding each number individually to the result causing rounding errors in every step. However, often numpy will use a numerically better approach (partial pairwise summation) leading to improved precision in many use-cases. This improved precision is always provided when no `axis` is given. When `axis` is given, it will depend on which axis is summed. Technically, to provide the best speed possible, the improved precision is only used when the summation is along the fast axis in memory. Note that the exact precision may vary depending on other parameters. In contrast to NumPy, Python’s `math.fsum` function uses a slower but more precise approach to summation. Especially when summing a large number of lower precision floating point numbers, such as `float32`, numerical errors can become significant. In such cases it can be advisable to use _dtype=np.float64_ to use a higher precision for the output.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.sum(\[0.5, 1.5\])
2.0
\>>> np.sum(\[0.5, 0.7, 0.2, 1.5\], dtype\=np.int32)
np.int32(1)
\>>> np.sum(\[\[0, 1\], \[0, 5\]\])
6
\>>> np.sum(\[\[0, 1\], \[0, 5\]\], axis\=0)
array(\[0, 6\])
\>>> np.sum(\[\[0, 1\], \[0, 5\]\], axis\=1)
array(\[1, 5\])
\>>> np.sum(\[\[0, 1\], \[np.nan, 5\]\], where\=\[False, True\], axis\=1)
array(\[1., 5.\])

Copy to clipboard

If the accumulator is too small, overflow occurs:

\>>> np.ones(128, dtype\=np.int8).sum(dtype\=np.int8)
np.int8(-128)

Copy to clipboard

You can also start the sum with a value other than zero:

\>>> np.sum(\[10\], initial\=5)
15

Copy to clipboard

Go BackOpen In Tab

On this page