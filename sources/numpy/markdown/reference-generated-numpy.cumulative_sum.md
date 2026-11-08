[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_sum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.cumulative_sum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_sum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.cumulative_sum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.cumulative_sum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.cumulative_sum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.cumulative_sum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.cumulative_sum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.cumulative_sum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.cumulative_sum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.cumulative_sum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.cumulative_sum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.cumulative_sum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.cumulative_sum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.cumulative_sum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.cumulative_sum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.cumulative_sum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.cumulative_sum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.cumulative_sum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.cumulative_sum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.cumulative_sum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.cumulative_sum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cumulative\_sum[#](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_sum.html#numpy-cumulative-sum "Link to this heading")

=================================================================================================================================================

numpy.cumulative\_sum(_x_, _/_, _\*_, _axis\=None_, _dtype\=None_, _out\=None_, _include\_initial\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2787-L2869)
[#](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_sum.html#numpy.cumulative_sum "Link to this definition")

Return the cumulative sum of the elements along a given axis.

This function is an Array API compatible alternative to [`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
.

Parameters:

**x**array\_like

Input array.

**axis**int, optional

Axis along which the cumulative sum is computed. The default (None) is only allowed for one-dimensional arrays. For arrays with more than one dimension `axis` is required.

**dtype**dtype, optional

Type of the returned array and of the accumulator in which the elements are summed. If `dtype` is not specified, it defaults to the dtype of `x`, unless `x` has an integer dtype with a precision less than that of the default platform integer. In that case, the default platform integer is used.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**include\_initial**bool, optional

Boolean indicating whether to include the initial value (zeros) as the first value in the output. With `include_initial=True` the shape of the output is different than the shape of the input. Default: `False`.

Returns:

**cumulative\_sum\_along\_axis**ndarray

A new array holding the result is returned unless `out` is specified, in which case a reference to `out` is returned. The result has the same shape as `x` if `include_initial=False`.

See also

[`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")

Sum array elements.

[`trapezoid`](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy.trapezoid "numpy.trapezoid")

Integration of array values using composite trapezoidal rule.

[`diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")

Calculate the n-th discrete difference along given axis.

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow.

`cumulative_sum(a)[-1]` may not be equal to `sum(a)` for floating-point values since `sum` may use a pairwise summation routine, reducing the roundoff-error. See [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 for more information.

Examples

Try it in your browser!

\>>> a \= np.array(\[1, 2, 3, 4, 5, 6\])
\>>> a
array(\[1, 2, 3, 4, 5, 6\])
\>>> np.cumulative\_sum(a)
array(\[ 1,  3,  6, 10, 15, 21\])
\>>> np.cumulative\_sum(a, dtype\=np.float64)  \# specifies type of output value(s)
array(\[  1.,   3.,   6.,  10.,  15.,  21.\])

Copy to clipboard

\>>> b \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> np.cumulative\_sum(b,axis\=0)  \# sum over rows for each of the 3 columns
array(\[\[1, 2, 3\],\
       \[5, 7, 9\]\])
\>>> np.cumulative\_sum(b,axis\=1)  \# sum over columns for each of the 2 rows
array(\[\[ 1,  3,  6\],\
       \[ 4,  9, 15\]\])

Copy to clipboard

`cumulative_sum(c)[-1]` may not be equal to `sum(c)`

\>>> c \= np.array(\[1, 2e-9, 3e-9\] \* 1000000)
\>>> np.cumulative\_sum(c)\[\-1\]
1000000.0050045159
\>>> c.sum()
1000000.0050000029

Copy to clipboard

Go BackOpen In Tab

On this page