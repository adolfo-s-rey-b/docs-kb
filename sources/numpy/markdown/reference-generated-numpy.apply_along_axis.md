[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.apply_along_axis.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.apply_along_axis.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.apply_along_axis.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.apply_along_axis.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.apply_along_axis.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.apply_along_axis.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.apply_along_axis.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.apply_along_axis.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.apply_along_axis.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.apply_along_axis.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.apply_along_axis.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.apply_along_axis.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.apply_along_axis.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.apply_along_axis.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.apply_along_axis.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.apply_along_axis.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.apply_along_axis.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.apply_along_axis.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.apply_along_axis.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.apply_along_axis.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.apply\_along\_axis[#](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy-apply-along-axis "Link to this heading")

========================================================================================================================================================

numpy.apply\_along\_axis(_func1d_, _axis_, _arr_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L276-L414)
[#](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "Link to this definition")

Apply a function to 1-D slices along the given axis.

Execute _func1d(a, \*args, \*\*kwargs)_ where _func1d_ operates on 1-D arrays and _a_ is a 1-D slice of _arr_ along _axis_.

This is equivalent to (but faster than) the following use of [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
 and [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
, which sets each of `ii`, `jj`, and `kk` to a tuple of indices:

Ni, Nk \= a.shape\[:axis\], a.shape\[axis+1:\]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        f \= func1d(arr\[ii + s\_\[:,\] + kk\])
        Nj \= f.shape
        for jj in ndindex(Nj):
            out\[ii + jj + kk\] \= f\[jj\]

Copy to clipboard

Equivalently, eliminating the inner loop, this can be expressed as:

Ni, Nk \= a.shape\[:axis\], a.shape\[axis+1:\]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        out\[ii + s\_\[...,\] + kk\] \= func1d(arr\[ii + s\_\[:,\] + kk\])

Copy to clipboard

Parameters:

**func1d**function (M,) -> (Nj…)

This function should accept 1-D arrays. It is applied to 1-D slices of _arr_ along the specified axis.

**axis**integer

Axis along which _arr_ is sliced.

**arr**ndarray (Ni…, M, Nk…)

Input array.

**args**any

Additional arguments to _func1d_.

**kwargs**any

Additional named arguments to _func1d_.

Returns:

**out**ndarray (Ni…, Nj…, Nk…)

The output array. The shape of _out_ is identical to the shape of _arr_, except along the _axis_ dimension. This axis is removed, and replaced with new dimensions equal to the shape of the return value of _func1d_. So if _func1d_ returns a scalar _out_ will have one fewer dimensions than _arr_.

See also

[`apply_over_axes`](https://numpy.org/doc/stable/reference/generated/numpy.apply_over_axes.html#numpy.apply_over_axes "numpy.apply_over_axes")

Apply a function repeatedly over multiple axes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> def my\_func(a):
... """Average first and last element of a 1-D array"""
...     return (a\[0\] + a\[\-1\]) \* 0.5
\>>> b \= np.array(\[\[1,2,3\], \[4,5,6\], \[7,8,9\]\])
\>>> np.apply\_along\_axis(my\_func, 0, b)
array(\[4., 5., 6.\])
\>>> np.apply\_along\_axis(my\_func, 1, b)
array(\[2.,  5.,  8.\])

Copy to clipboard

For a function that returns a 1D array, the number of dimensions in _outarr_ is the same as _arr_.

\>>> b \= np.array(\[\[8,1,7\], \[4,3,9\], \[5,2,6\]\])
\>>> np.apply\_along\_axis(sorted, 1, b)
array(\[\[1, 7, 8\],\
       \[3, 4, 9\],\
       \[2, 5, 6\]\])

Copy to clipboard

For a function that returns a higher dimensional array, those dimensions are inserted in place of the _axis_ dimension.

\>>> b \= np.array(\[\[1,2,3\], \[4,5,6\], \[7,8,9\]\])
\>>> np.apply\_along\_axis(np.diag, \-1, b)
array(\[\[\[1, 0, 0\],\
        \[0, 2, 0\],\
        \[0, 0, 3\]\],\
       \[\[4, 0, 0\],\
        \[0, 5, 0\],\
        \[0, 0, 6\]\],\
       \[\[7, 0, 0\],\
        \[0, 8, 0\],\
        \[0, 0, 9\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page