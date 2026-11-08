[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.corrcoef.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.corrcoef.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.corrcoef.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.corrcoef.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.corrcoef.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.corrcoef.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.corrcoef.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.corrcoef.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.corrcoef.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.corrcoef.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.corrcoef.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.corrcoef.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.corrcoef.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.corrcoef.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.corrcoef.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.corrcoef.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.corrcoef.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.corrcoef.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.corrcoef.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.corrcoef.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.corrcoef.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.corrcoef.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.corrcoef[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.corrcoef.html#numpy-ma-corrcoef "Link to this heading")

=======================================================================================================================================

ma.corrcoef(_x_, _y\=None_, _rowvar\=True_, _allow\_masked\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1675-L1730)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.corrcoef.html#numpy.ma.corrcoef "Link to this definition")

Return Pearson product-moment correlation coefficients.

Except for the handling of missing data this function does the same as [`numpy.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
. For more details and examples, see [`numpy.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
.

Parameters:

**x**array\_like

A 1-D or 2-D array containing multiple variables and observations. Each row of _x_ represents a variable, and each column a single observation of all those variables. Also see _rowvar_ below.

**y**array\_like, optional

An additional set of variables and observations. _y_ has the same shape as _x_.

**rowvar**bool, optional

If _rowvar_ is True (default), then each row represents a variable, with observations in the columns. Otherwise, the relationship is transposed: each column represents a variable, while the rows contain observations.

**allow\_masked**bool, optional

If True, masked values are propagated pair-wise: if a value is masked in _x_, the corresponding value is masked in _y_. If False, raises an exception. Because _bias_ is deprecated, this argument needs to be treated as keyword only to avoid a warning.

See also

[`numpy.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")

Equivalent function in top-level NumPy module.

[`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")

Estimate the covariance matrix.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[0, 1\], \[1, 1\]\], mask\=\[0, 1, 0, 1\])
\>>> np.ma.corrcoef(x)
masked\_array(
  data=\[\[--, --\],\
        \[--, --\]\],
  mask=\[\[ True,  True\],\
        \[ True,  True\]\],
  fill\_value=1e+20,
  dtype=float64)

Copy to clipboard

Go BackOpen In Tab

On this page