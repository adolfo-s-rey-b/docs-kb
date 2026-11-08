[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ediff1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ediff1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ediff1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ediff1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ediff1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ediff1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ediff1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ediff1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ediff1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ediff1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ediff1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ediff1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ediff1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ediff1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ediff1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ediff1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ediff1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ediff1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ediff1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ediff1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ediff1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy-ediff1d "Link to this heading")

===========================================================================================================================

numpy.ediff1d(_ary_, _to\_end\=None_, _to\_begin\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L40-L128)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "Link to this definition")

The differences between consecutive elements of an array.

Parameters:

**ary**array\_like

If necessary, will be flattened before the differences are taken.

**to\_end**array\_like, optional

Number(s) to append at the end of the returned differences.

**to\_begin**array\_like, optional

Number(s) to prepend at the beginning of the returned differences.

Returns:

**ediff1d**ndarray

The differences. Loosely, this is `ary.flat[1:] - ary.flat[:-1]`.

See also

[`diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
, [`gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient "numpy.gradient")

Notes

When applied to masked arrays, this function drops the mask information if the _to\_begin_ and/or _to\_end_ parameters are used.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 4, 7, 0\])
\>>> np.ediff1d(x)
array(\[ 1,  2,  3, -7\])

Copy to clipboard

\>>> np.ediff1d(x, to\_begin\=-99, to\_end\=np.array(\[88, 99\]))
array(\[-99,   1,   2, ...,  -7,  88,  99\])

Copy to clipboard

The returned array is always 1D.

\>>> y \= \[\[1, 2, 4\], \[1, 6, 24\]\]
\>>> np.ediff1d(y)
array(\[ 1,  2, -3,  5, 18\])

Copy to clipboard

Go BackOpen In Tab

On this page