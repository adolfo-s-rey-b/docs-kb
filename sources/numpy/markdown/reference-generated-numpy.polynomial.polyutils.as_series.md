[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.as_series.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polyutils.as\_series[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.as_series.html#numpy-polynomial-polyutils-as-series "Link to this heading")

=================================================================================================================================================================================================

polynomial.polyutils.as\_series(_alist_, _trim\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L63-L141)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.as_series.html#numpy.polynomial.polyutils.as_series "Link to this definition")

Return argument as a list of 1-d arrays.

The returned list contains array(s) of dtype double, complex double, or object. A 1-d argument of shape `(N,)` is parsed into `N` arrays of size one; a 2-d argument of shape `(M,N)` is parsed into `M` arrays of size `N` (i.e., is “parsed by row”); and a higher dimensional array raises a Value Error if it is not first reshaped into either a 1-d or 2-d array.

Parameters:

**alist**array\_like

A 1- or 2-d array\_like

**trim**boolean, optional

When True, trailing zeros are removed from the inputs. When False, the inputs are passed through intact.

Returns:

**\[a1, a2,…\]**list of 1-D arrays

A copy of the input data as a list of 1-d arrays.

Raises:

ValueError

Raised when [`as_series`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.as_series.html#numpy.polynomial.polyutils.as_series "numpy.polynomial.polyutils.as_series")
 cannot convert its input to 1-d arrays, or at least one of the resulting arrays is empty.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial import polyutils as pu
\>>> a \= np.arange(4)
\>>> pu.as\_series(a)
\[array(\[0.\]), array(\[1.\]), array(\[2.\]), array(\[3.\])\]
\>>> b \= np.arange(6).reshape((2,3))
\>>> pu.as\_series(b)
\[array(\[0., 1., 2.\]), array(\[3., 4., 5.\])\]

Copy to clipboard

\>>> pu.as\_series((1, np.arange(3), np.arange(2, dtype\=np.float16)))
\[array(\[1.\]), array(\[0., 1., 2.\]), array(\[0., 1.\])\]

Copy to clipboard

\>>> pu.as\_series(\[2, \[1.1, 0.\]\])
\[array(\[2.\]), array(\[1.1\])\]

Copy to clipboard

\>>> pu.as\_series(\[2, \[1.1, 0.\]\], trim\=False)
\[array(\[2.\]), array(\[1.1, 0. \])\]

Copy to clipboard

Go BackOpen In Tab

On this page