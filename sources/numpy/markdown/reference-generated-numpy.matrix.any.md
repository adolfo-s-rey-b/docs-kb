[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.any.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.any.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.any.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.any.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.any.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.any.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.any.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.any.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.any.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.any.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.any.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.any.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.any.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.any.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.any.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.any.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.any.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.any.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.any.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.any.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.any.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.any.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.any[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.any.html#numpy-matrix-any "Link to this heading")

====================================================================================================================================

method

matrix.any(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L554-L575)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.any.html#numpy.matrix.any "Link to this definition")

Test whether any array element along a given axis evaluates to True.

Refer to [`numpy.any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
 for full documentation.

Parameters:

**axis**int, optional

Axis along which logical OR is performed

**out**ndarray, optional

Output to existing array instead of creating new one, must have same shape as expected output

Returns:

**any**bool, ndarray

Returns a single bool if _axis_ is `None`; otherwise, returns [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

On this page