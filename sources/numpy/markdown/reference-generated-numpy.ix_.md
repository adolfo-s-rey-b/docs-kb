[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ix_.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ix_.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ix_.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ix_.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ix_.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ix_.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ix_.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ix_.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ix_.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ix_.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ix_.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ix_.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ix_.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ix_.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ix_.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ix_.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ix_.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ix_.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ix_.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ix_.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ix\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy-ix "Link to this heading")

===============================================================================================================

numpy.ix\_(_\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L31-L104)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy.ix_ "Link to this definition")

Construct an open mesh from multiple sequences.

This function takes N 1-D sequences and returns N outputs with N dimensions each, such that the shape is 1 in all but one dimension and the dimension with the non-unit shape value cycles through all N dimensions.

Using [`ix_`](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_")
 one can quickly construct index arrays that will index the cross product. `a[np.ix_([1,3],[2,5])]` returns the array `[[a[1,2] a[1,5]], [a[3,2] a[3,5]]]`.

Parameters:

**args**1-D sequences

Each sequence should be of integer or boolean type. Boolean sequences will be interpreted as boolean masks for the corresponding dimension (equivalent to passing in `np.nonzero(boolean_sequence)`).

Returns:

**out**tuple of ndarrays

N arrays with N dimensions each, with N the number of input sequences. Together these arrays form an open mesh.

See also

[`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
, [`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
, [`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(10).reshape(2, 5)
\>>> a
array(\[\[0, 1, 2, 3, 4\],\
       \[5, 6, 7, 8, 9\]\])
\>>> ixgrid \= np.ix\_(\[0, 1\], \[2, 4\])
\>>> ixgrid
(array(\[\[0\],\
       \[1\]\]), array(\[\[2, 4\]\]))
\>>> ixgrid\[0\].shape, ixgrid\[1\].shape
((2, 1), (1, 2))
\>>> a\[ixgrid\]
array(\[\[2, 4\],\
       \[7, 9\]\])

Copy to clipboard

\>>> ixgrid \= np.ix\_(\[True, True\], \[2, 4\])
\>>> a\[ixgrid\]
array(\[\[2, 4\],\
       \[7, 9\]\])
\>>> ixgrid \= np.ix\_(\[True, True\], \[False, False, True, False, True\])
\>>> a\[ixgrid\]
array(\[\[2, 4\],\
       \[7, 9\]\])

Copy to clipboard

Go BackOpen In Tab

On this page