[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.corrcoef.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.corrcoef.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.corrcoef.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.corrcoef.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.corrcoef.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.corrcoef.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.corrcoef.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.corrcoef.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.corrcoef.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.corrcoef.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.corrcoef.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.corrcoef.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.corrcoef.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.corrcoef.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.corrcoef.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.corrcoef.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.corrcoef.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.corrcoef.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.corrcoef.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.corrcoef.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.corrcoef[#](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy-corrcoef "Link to this heading")

==============================================================================================================================

numpy.corrcoef(_x_, _y\=None_, _rowvar\=True_, _\*_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L2910-L3046)
[#](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "Link to this definition")

Return Pearson product-moment correlation coefficients.

Please refer to the documentation for [`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")
 for more detail. The relationship between the correlation coefficient matrix, _R_, and the covariance matrix, _C_, is

\\\[R\_{ij} = \\frac{ C\_{ij} } { \\sqrt{ C\_{ii} C\_{jj} } }\\\]

The values of _R_ are between -1 and 1, inclusive.

Parameters:

**x**array\_like

A 1-D or 2-D array containing multiple variables and observations. Each row of _x_ represents a variable, and each column a single observation of all those variables. Also see _rowvar_ below.

**y**array\_like, optional

An additional set of variables and observations. _y_ has the same shape as _x_.

**rowvar**bool, optional

If _rowvar_ is True (default), then each row represents a variable, with observations in the columns. Otherwise, the relationship is transposed: each column represents a variable, while the rows contain observations.

**dtype**data-type, optional

Data-type of the result. By default, the return data-type will have at least [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 precision.

New in version 1.20.

Returns:

**R**ndarray

The correlation coefficient matrix of the variables.

See also

[`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")

Covariance matrix

Notes

Due to floating point rounding the resulting array may not be Hermitian, the diagonal elements may not be 1, and the elements may not satisfy the inequality abs(a) <= 1. The real and imaginary parts are clipped to the interval \[-1, 1\] in an attempt to improve on that situation but is not much help in the complex case.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

In this example we generate two random arrays, `xarr` and `yarr`, and compute the row-wise and column-wise Pearson correlation coefficients, `R`. Since `rowvar` is true by default, we first find the row-wise Pearson correlation coefficients between the variables of `xarr`.

\>>> import numpy as np
\>>> rng \= np.random.default\_rng(seed\=42)
\>>> xarr \= rng.random((3, 3))
\>>> xarr
array(\[\[0.77395605, 0.43887844, 0.85859792\],\
       \[0.69736803, 0.09417735, 0.97562235\],\
       \[0.7611397 , 0.78606431, 0.12811363\]\])
\>>> R1 \= np.corrcoef(xarr)
\>>> R1
array(\[\[ 1.        ,  0.99256089, -0.68080986\],\
       \[ 0.99256089,  1.        , -0.76492172\],\
       \[-0.68080986, -0.76492172,  1.        \]\])

Copy to clipboard

If we add another set of variables and observations `yarr`, we can compute the row-wise Pearson correlation coefficients between the variables in `xarr` and `yarr`.

\>>> yarr \= rng.random((3, 3))
\>>> yarr
array(\[\[0.45038594, 0.37079802, 0.92676499\],\
       \[0.64386512, 0.82276161, 0.4434142 \],\
       \[0.22723872, 0.55458479, 0.06381726\]\])
\>>> R2 \= np.corrcoef(xarr, yarr)
\>>> R2
array(\[\[ 1.        ,  0.99256089, -0.68080986,  0.75008178, -0.934284  ,\
        -0.99004057\],\
       \[ 0.99256089,  1.        , -0.76492172,  0.82502011, -0.97074098,\
        -0.99981569\],\
       \[-0.68080986, -0.76492172,  1.        , -0.99507202,  0.89721355,\
         0.77714685\],\
       \[ 0.75008178,  0.82502011, -0.99507202,  1.        , -0.93657855,\
        -0.83571711\],\
       \[-0.934284  , -0.97074098,  0.89721355, -0.93657855,  1.        ,\
         0.97517215\],\
       \[-0.99004057, -0.99981569,  0.77714685, -0.83571711,  0.97517215,\
         1.        \]\])

Copy to clipboard

Finally if we use the option `rowvar=False`, the columns are now being treated as the variables and we will find the column-wise Pearson correlation coefficients between variables in `xarr` and `yarr`.

\>>> R3 \= np.corrcoef(xarr, yarr, rowvar\=False)
\>>> R3
array(\[\[ 1.        ,  0.77598074, -0.47458546, -0.75078643, -0.9665554 ,\
         0.22423734\],\
       \[ 0.77598074,  1.        , -0.92346708, -0.99923895, -0.58826587,\
        -0.44069024\],\
       \[-0.47458546, -0.92346708,  1.        ,  0.93773029,  0.23297648,\
         0.75137473\],\
       \[-0.75078643, -0.99923895,  0.93773029,  1.        ,  0.55627469,\
         0.47536961\],\
       \[-0.9665554 , -0.58826587,  0.23297648,  0.55627469,  1.        ,\
        -0.46666491\],\
       \[ 0.22423734, -0.44069024,  0.75137473,  0.47536961, -0.46666491,\
         1.        \]\])

Copy to clipboard

Go BackOpen In Tab

On this page