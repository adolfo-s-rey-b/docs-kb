[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.copy.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.copy.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.copy.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.copy.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.copy.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.copy.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.copy.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.copy.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.copy.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.copy.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.copy.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.copy.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.copy.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.copy.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.copy.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.copy.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.copy.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.copy.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.copy.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.copy.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.copy.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.copy[#](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy-copy "Link to this heading")

==================================================================================================================

numpy.copy(_a_, _order\='K'_, _subok\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L935-L1003)
[#](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "Link to this definition")

Return an array copy of the given object.

Parameters:

**a**array\_like

Input data.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Controls the memory layout of the copy. ‘C’ means C-order, ‘F’ means F-order, ‘A’ means ‘F’ if _a_ is Fortran contiguous, ‘C’ otherwise. ‘K’ means match the layout of _a_ as closely as possible. (Note that this function and [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")
 are very similar, but have different default values for their order= arguments.)

**subok**bool, optional

If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (defaults to False).

Returns:

**arr**ndarray

Array interpretation of _a_.

See also

[`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")

Preferred method for creating an array copy

Notes

This is equivalent to:

\>>> np.array(a, copy\=True)  

Copy to clipboard

The copy made of the data is shallow, i.e., for arrays with object dtype, the new array will point to the same objects. See Examples from [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")
.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create an array x, with a reference y and a copy z:

\>>> x \= np.array(\[1, 2, 3\])
\>>> y \= x
\>>> z \= np.copy(x)

Copy to clipboard

Note that, when we modify x, y changes, but not z:

\>>> x\[0\] \= 10
\>>> x\[0\] \== y\[0\]
True
\>>> x\[0\] \== z\[0\]
False

Copy to clipboard

Note that, np.copy clears previously set WRITEABLE=False flag.

\>>> a \= np.array(\[1, 2, 3\])
\>>> a.flags\["WRITEABLE"\] \= False
\>>> b \= np.copy(a)
\>>> b.flags\["WRITEABLE"\]
True
\>>> b\[0\] \= 3
\>>> b
array(\[3, 2, 3\])

Copy to clipboard

Go BackOpen In Tab

On this page