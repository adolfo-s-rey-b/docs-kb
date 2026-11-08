[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.cov.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.cov.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.cov.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.cov.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.cov.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.cov.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.cov.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.cov.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.cov.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.cov.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.cov.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.cov.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.cov.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.cov.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.cov.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.cov.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.cov.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.cov.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.cov.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.cov.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.cov.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cov[#](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy-cov "Link to this heading")

===============================================================================================================

numpy.cov(_m_, _y\=None_, _rowvar\=True_, _bias\=False_, _ddof\=None_, _fweights\=None_, _aweights\=None_, _\*_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L2687-L2902)
[#](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "Link to this definition")

Estimate a covariance matrix, given data and weights.

Covariance indicates the level to which two variables vary together. If we examine N-dimensional samples, \\(X = \[x\_1, x\_2, ..., x\_N\]^T\\), then the covariance matrix element \\(C\_{ij}\\) is the covariance of \\(x\_i\\) and \\(x\_j\\). The element \\(C\_{ii}\\) is the variance of \\(x\_i\\).

See the notes for an outline of the algorithm.

Parameters:

**m**array\_like

A 1-D or 2-D array containing multiple variables and observations. Each row of _m_ represents a variable, and each column a single observation of all those variables. Also see _rowvar_ below.

**y**array\_like, optional

An additional set of variables and observations. _y_ has the same form as that of _m_.

**rowvar**bool, optional

If _rowvar_ is True (default), then each row represents a variable, with observations in the columns. Otherwise, the relationship is transposed: each column represents a variable, while the rows contain observations.

**bias**bool, optional

Default normalization (False) is by `(N - 1)`, where `N` is the number of observations given (unbiased estimate). If _bias_ is True, then normalization is by `N`. These values can be overridden by using the keyword `ddof` in numpy versions >= 1.5.

**ddof**int, optional

If not `None` the default value implied by _bias_ is overridden. Note that `ddof=1` will return the unbiased estimate, even if both _fweights_ and _aweights_ are specified, and `ddof=0` will return the simple average. See the notes for the details. The default value is `None`.

**fweights**array\_like, int, optional

1-D array of integer frequency weights; the number of times each observation vector should be repeated.

**aweights**array\_like, optional

1-D array of observation vector weights. These relative weights are typically large for observations considered “important” and smaller for observations considered less “important”. If `ddof=0` the array of weights can be used to assign probabilities to observation vectors.

**dtype**data-type, optional

Data-type of the result. By default, the return data-type will have at least [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 precision.

New in version 1.20.

Returns:

**out**ndarray

The covariance matrix of the variables.

See also

[`corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")

Normalized covariance matrix

Notes

Assume that the observations are in the columns of the observation array _m_ and let `f = fweights` and `a = aweights` for brevity. The steps to compute the weighted covariance are as follows:

\>>> m \= np.arange(10, dtype\=np.float64)
\>>> f \= np.arange(10) \* 2
\>>> a \= np.arange(10) \*\* 2.
\>>> ddof \= 1
\>>> w \= f \* a
\>>> v1 \= np.sum(w)
\>>> v2 \= np.sum(w \* a)
\>>> m \-= np.sum(m \* w, axis\=None, keepdims\=True) / v1
\>>> cov \= np.dot(m \* w, m.T) \* v1 / (v1\*\*2 \- ddof \* v2)

Copy to clipboard

Note that when `a == 1`, the normalization factor `v1 / (v1**2 - ddof * v2)` goes over to `1 / (np.sum(f) - ddof)` as it should.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Consider two variables, \\(x\_0\\) and \\(x\_1\\), which correlate perfectly, but in opposite directions:

\>>> x \= np.array(\[\[0, 2\], \[1, 1\], \[2, 0\]\]).T
\>>> x
array(\[\[0, 1, 2\],\
       \[2, 1, 0\]\])

Copy to clipboard

Note how \\(x\_0\\) increases while \\(x\_1\\) decreases. The covariance matrix shows this clearly:

\>>> np.cov(x)
array(\[\[ 1., -1.\],\
       \[-1.,  1.\]\])

Copy to clipboard

Note that element \\(C\_{0,1}\\), which shows the correlation between \\(x\_0\\) and \\(x\_1\\), is negative.

Further, note how _x_ and _y_ are combined:

\>>> x \= \[\-2.1, \-1,  4.3\]
\>>> y \= \[3,  1.1,  0.12\]
\>>> X \= np.stack((x, y), axis\=0)
\>>> np.cov(X)
array(\[\[11.71      , -4.286     \], # may vary\
       \[-4.286     ,  2.144133\]\])
\>>> np.cov(x, y)
array(\[\[11.71      , -4.286     \], # may vary\
       \[-4.286     ,  2.144133\]\])
\>>> np.cov(x)
array(11.71)

Copy to clipboard

Go BackOpen In Tab

On this page