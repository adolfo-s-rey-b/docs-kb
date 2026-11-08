[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unique_all.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unique_all.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unique_all.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unique_all.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unique_all.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unique_all.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unique_all.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unique_all.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unique_all.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unique_all.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unique_all.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unique_all.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unique_all.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unique_all.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unique_all.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unique_all.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unique_all.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unique_all.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unique_all.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unique_all.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unique_all.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unique_all.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unique\_all[#](https://numpy.org/doc/stable/reference/generated/numpy.unique_all.html#numpy-unique-all "Link to this heading")

=====================================================================================================================================

numpy.unique\_all(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L440-L497)
[#](https://numpy.org/doc/stable/reference/generated/numpy.unique_all.html#numpy.unique_all "Link to this definition")

Find the unique elements of an array, and counts, inverse, and indices.

This function is an Array API compatible alternative to:

np.unique(x, return\_index\=True, return\_inverse\=True,
          return\_counts\=True, equal\_nan\=False, sorted\=False)

Copy to clipboard

but returns a namedtuple for easier access to each output.

Note

This function currently always returns a sorted result, however, this could change in any NumPy minor release.

Parameters:

**x**array\_like

Input array. It will be flattened if it is not already 1-D.

Returns:

**out**namedtuple

The result containing:

*   values - The unique elements of an input array.
    
*   indices - The first occurring indices for each unique element.
    
*   inverse\_indices - The indices from the set of unique elements that reconstruct _x_.
    
*   counts - The corresponding counts for each unique element.
    

See also

[`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")

Find the unique elements of an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= \[1, 1, 2\]
\>>> uniq \= np.unique\_all(x)
\>>> uniq.values
array(\[1, 2\])
\>>> uniq.indices
array(\[0, 2\])
\>>> uniq.inverse\_indices
array(\[0, 0, 1\])
\>>> uniq.counts
array(\[2, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page