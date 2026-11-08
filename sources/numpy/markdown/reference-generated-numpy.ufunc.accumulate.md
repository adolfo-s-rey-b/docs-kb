[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.accumulate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.accumulate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.accumulate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.accumulate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.accumulate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.accumulate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.accumulate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.accumulate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.accumulate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.accumulate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.accumulate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.accumulate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.accumulate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.accumulate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.accumulate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.accumulate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.accumulate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.accumulate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.accumulate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.accumulate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.accumulate[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#numpy-ufunc-accumulate "Link to this heading")

======================================================================================================================================================

method

ufunc.accumulate(_array_, _axis\=0_, _dtype\=None_, _out\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.accumulate.html#numpy.ufunc.accumulate "Link to this definition")

Accumulate the result of applying the operator to all elements.

For a one-dimensional array, accumulate produces results equivalent to:

r \= np.empty(len(A))
t \= op.identity        \# op = the ufunc being applied to A's  elements
for i in range(len(A)):
    t \= op(t, A\[i\])
    r\[i\] \= t
return r

Copy to clipboard

For example, add.accumulate() is equivalent to np.cumsum().

For a multi-dimensional array, accumulate is applied along only one axis (axis zero by default; see Examples below) so repeated use is necessary if one wants to accumulate over multiple axes.

Parameters:

**array**array\_like

The array to act on.

**axis**int, optional

The axis along which to apply the accumulation; default is zero.

**dtype**data-type code, optional

The data-type used to represent the intermediate results. Defaults to the data-type of the output array if such is provided, or the data-type of the input array if no output array is provided.

**out**ndarray, None, or tuple of ndarray and None, optional

Location into which the result is stored. If not provided or None, a freshly-allocated array is returned. For consistency with `ufunc.__call__`, if passed as a keyword argument, can be Ellipses (`out=...`, which has the same effect as None as an array is always returned), or a 1-element tuple.

Returns:

**r**ndarray

The accumulated values. If _out_ was supplied, _r_ is a reference to _out_.

Examples

Try it in your browser!

1-D array examples:

\>>> import numpy as np
\>>> np.add.accumulate(\[2, 3, 5\])
array(\[ 2,  5, 10\])
\>>> np.multiply.accumulate(\[2, 3, 5\])
array(\[ 2,  6, 30\])

Copy to clipboard

2-D array examples:

\>>> I \= np.eye(2)
\>>> I
array(\[\[1.,  0.\],\
       \[0.,  1.\]\])

Copy to clipboard

Accumulate along axis 0 (rows), down columns:

\>>> np.add.accumulate(I, 0)
array(\[\[1.,  0.\],\
       \[1.,  1.\]\])
\>>> np.add.accumulate(I) \# no axis specified = axis zero
array(\[\[1.,  0.\],\
       \[1.,  1.\]\])

Copy to clipboard

Accumulate along axis 1 (columns), through rows:

\>>> np.add.accumulate(I, 1)
array(\[\[1.,  1.\],\
       \[0.,  1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page