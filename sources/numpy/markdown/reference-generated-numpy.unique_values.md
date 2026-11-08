[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unique_values.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unique_values.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unique_values.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unique_values.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unique_values.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unique_values.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unique_values.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unique_values.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unique_values.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unique_values.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unique_values.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unique_values.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unique_values.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unique_values.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unique_values.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unique_values.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unique_values.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unique_values.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unique_values.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unique_values.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unique_values.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unique_values.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unique\_values[#](https://numpy.org/doc/stable/reference/generated/numpy.unique_values.html#numpy-unique-values "Link to this heading")

==============================================================================================================================================

numpy.unique\_values(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L617-L658)
[#](https://numpy.org/doc/stable/reference/generated/numpy.unique_values.html#numpy.unique_values "Link to this definition")

Returns the unique elements of an input array _x_.

This function is an Array API compatible alternative to:

np.unique(x, equal\_nan\=False, sorted\=False)

Copy to clipboard

Changed in version 2.3: The algorithm was changed to a faster one that does not rely on sorting, and hence the results are no longer implicitly sorted.

Parameters:

**x**array\_like

Input array. It will be flattened if it is not already 1-D.

Returns:

**out**ndarray

The unique elements of an input array.

See also

[`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")

Find the unique elements of an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.unique\_values(\[1, 1, 2\])
array(\[1, 2\])  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page