[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nbytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.recarray.nbytes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nbytes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.recarray.nbytes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.recarray.nbytes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.recarray.nbytes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.recarray.nbytes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.recarray.nbytes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.recarray.nbytes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.recarray.nbytes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.recarray.nbytes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.recarray.nbytes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.recarray.nbytes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.recarray.nbytes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.recarray.nbytes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.recarray.nbytes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.recarray.nbytes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.recarray.nbytes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.recarray.nbytes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.recarray.nbytes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.recarray.nbytes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.recarray.nbytes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.recarray.nbytes[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nbytes.html#numpy-recarray-nbytes "Link to this heading")

===================================================================================================================================================

attribute

recarray.nbytes[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nbytes.html#numpy.recarray.nbytes "Link to this definition")

Total bytes consumed by the elements of the array.

See also

[`sys.getsizeof`](https://docs.python.org/3/library/sys.html#sys.getsizeof "(in Python v3.14)")

Memory consumed by the object itself without parents in case view. This does include memory consumed by non-element attributes.

Notes

Does not include memory consumed by non-element attributes of the array object.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.zeros((3,5,2), dtype\=np.complex128)
\>>> x.nbytes
480
\>>> np.prod(x.shape) \* x.itemsize
480

Copy to clipboard

Go BackOpen In Tab

On this page