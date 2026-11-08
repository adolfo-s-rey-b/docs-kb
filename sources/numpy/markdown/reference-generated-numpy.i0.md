[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.i0.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.i0.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.i0.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.i0.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.i0.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.i0.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.i0.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.i0.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.i0.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.i0.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.i0.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.i0.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.i0.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.i0.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.i0.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.i0.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.i0.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.i0.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.i0.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.i0.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.i0.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.i0[#](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#numpy-i0 "Link to this heading")

============================================================================================================

numpy.i0(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3544-L3602)
[#](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#numpy.i0 "Link to this definition")

Modified Bessel function of the first kind, order 0.

Usually denoted \\(I\_0\\).

Parameters:

**x**array\_like of float

Argument of the Bessel function.

Returns:

**out**ndarray, shape = x.shape, dtype = float

The modified Bessel function evaluated at each of the elements of _x_.

See also

[`scipy.special.i0`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.i0.html#scipy.special.i0 "(in SciPy v1.18.0)")
, [`scipy.special.iv`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.iv.html#scipy.special.iv "(in SciPy v1.18.0)")
, [`scipy.special.ive`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ive.html#scipy.special.ive "(in SciPy v1.18.0)")

Notes

The scipy implementation is recommended over this function: it is a proper ufunc written in C, and more than an order of magnitude faster.

We use the algorithm published by Clenshaw [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#rfd38a370b188-1)
 and referenced by Abramowitz and Stegun [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#rfd38a370b188-2)
, for which the function domain is partitioned into the two intervals \[0,8\] and (8,inf), and Chebyshev polynomial expansions are employed in each interval. Relative error on the domain \[0,30\] using IEEE arithmetic is documented [\[3\]](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#rfd38a370b188-3)
 as having a peak of 5.8e-16 with an rms of 1.4e-16 (n = 30000).

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#id1)\
\]

C. W. Clenshaw, “Chebyshev series for mathematical functions”, in _National Physical Laboratory Mathematical Tables_, vol. 5, London: Her Majesty’s Stationery Office, 1962.

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#id2)\
\]

M. Abramowitz and I. A. Stegun, _Handbook of Mathematical Functions_, 10th printing, New York: Dover, 1964, pp. 379. [https://personal.math.ubc.ca/~cbm/aands/page\_379.htm](https://personal.math.ubc.ca/~cbm/aands/page_379.htm)

\[[3](https://numpy.org/doc/stable/reference/generated/numpy.i0.html#id3)\
\]

[https://metacpan.org/pod/distribution/Math-Cephes/lib/Math/Cephes.pod#i0:-Modified-Bessel-function-of-order-zero](https://metacpan.org/pod/distribution/Math-Cephes/lib/Math/Cephes.pod#i0:-Modified-Bessel-function-of-order-zero)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.i0(0.)
array(1.0)
\>>> np.i0(\[0, 1, 2, 3\])
array(\[1.        , 1.26606588, 2.2795853 , 4.88079259\])

Copy to clipboard

Go BackOpen In Tab

On this page