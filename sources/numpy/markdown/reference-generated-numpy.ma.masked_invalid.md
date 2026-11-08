[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_invalid.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_invalid.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_invalid.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_invalid.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_invalid.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_invalid.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_invalid.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_invalid.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_invalid.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_invalid.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_invalid.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_invalid.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_invalid.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_invalid.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_invalid.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_invalid.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_invalid.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_invalid.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_invalid.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_invalid.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_invalid[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#numpy-ma-masked-invalid "Link to this heading")

==========================================================================================================================================================

ma.masked\_invalid(_a_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2400-L2434)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#numpy.ma.masked_invalid "Link to this definition")

Mask an array where invalid values occur (NaNs or infs).

This function is a shortcut to `masked_where`, with _condition_ = ~(np.isfinite(a)). Any pre-existing mask is conserved. Only applies to arrays with a dtype where NaNs or infs make sense (i.e. floating point types), but accepts any array\_like object.

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.arange(5, dtype\=np.float64)
\>>> a\[2\] \= np.nan
\>>> a\[3\] \= np.inf
\>>> a
array(\[ 0.,  1., nan, inf,  4.\])
\>>> ma.masked\_invalid(a)
masked\_array(data=\[0.0, 1.0, --, --, 4.0\],
             mask=\[False, False,  True,  True, False\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page