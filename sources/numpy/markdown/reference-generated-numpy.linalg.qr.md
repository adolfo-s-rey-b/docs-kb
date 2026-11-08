[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.qr.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.qr.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.qr.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.qr.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.qr.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.qr.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.qr.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.qr.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.qr.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.qr.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.qr.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.qr.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.qr.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.qr.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.qr.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.qr.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.qr.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.qr.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.qr.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.qr.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.qr[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html#numpy-linalg-qr "Link to this heading")

=================================================================================================================================

linalg.qr(_a_, _mode\='reduced'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L976-L1176)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html#numpy.linalg.qr "Link to this definition")

Compute the qr factorization of a matrix.

Factor the matrix _a_ as _qr_, where _q_ is orthonormal and _r_ is upper-triangular.

Parameters:

**a**array\_like, shape (…, M, N)

An array-like object with the dimensionality of at least 2.

**mode**{‘reduced’, ‘complete’, ‘r’, ‘raw’}, optional, default: ‘reduced’

If K = min(M, N), then

*   ‘reduced’ : returns Q, R with dimensions (…, M, K), (…, K, N)
    
*   ‘complete’ : returns Q, R with dimensions (…, M, M), (…, M, N)
    
*   ‘r’ : returns R only with dimensions (…, K, N)
    
*   ‘raw’ : returns h, tau with dimensions (…, N, M), (…, K,)
    

The options ‘reduced’, ‘complete, and ‘raw’ are new in numpy 1.8, see the notes for more information. The default is ‘reduced’, and to maintain backward compatibility with earlier versions of numpy both it and the old default ‘full’ can be omitted. Note that array h returned in ‘raw’ mode is transposed for calling Fortran. The ‘economic’ mode is deprecated. The modes ‘full’ and ‘economic’ may be passed using only the first letter for backwards compatibility, but all others must be spelled out. See the Notes for more explanation.

Returns:

**Q**ndarray of float or complex, optional

A matrix with orthonormal columns. When mode = ‘complete’ the result is an orthogonal/unitary matrix depending on whether or not a is real/complex. The determinant may be either +/- 1 in that case. In case the number of dimensions in the input array is greater than 2 then a stack of the matrices with above properties is returned.

**R**ndarray of float or complex, optional

The upper-triangular matrix or a stack of upper-triangular matrices if the number of dimensions in the input array is greater than 2.

**(h, tau)**ndarrays of np.double or np.cdouble, optional

The array h contains the Householder reflectors that generate q along with r. The tau array contains scaling factors for the reflectors. In the deprecated ‘economic’ mode only h is returned.

Raises:

LinAlgError

If factoring fails.

See also

[`scipy.linalg.qr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr.html#scipy.linalg.qr "(in SciPy v1.18.0)")

Similar function in SciPy.

[`scipy.linalg.rq`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.rq.html#scipy.linalg.rq "(in SciPy v1.18.0)")

Compute RQ decomposition of a matrix.

Notes

When mode is ‘reduced’ or ‘complete’, the result will be a namedtuple with the attributes `Q` and `R`.

This is an interface to the LAPACK routines `dgeqrf`, `zgeqrf`, `dorgqr`, and `zungqr`.

For more information on the qr factorization, see for example: [https://en.wikipedia.org/wiki/QR\_factorization](https://en.wikipedia.org/wiki/QR_factorization)

Subclasses of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 are preserved except for the ‘raw’ mode. So if _a_ is of type [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
, all the return values will be matrices too.

New ‘reduced’, ‘complete’, and ‘raw’ options for mode were added in NumPy 1.8.0 and the old option ‘full’ was made an alias of ‘reduced’. In addition the options ‘full’ and ‘economic’ were deprecated. Because ‘full’ was the previous default and ‘reduced’ is the new default, backward compatibility can be maintained by letting _mode_ default. The ‘raw’ option was added so that LAPACK routines that can multiply arrays by q using the Householder reflectors can be used. Note that in this case the returned arrays are of type np.double or np.cdouble and the h array is transposed to be FORTRAN compatible. No routines using the ‘raw’ return are currently exposed by numpy, but some are available in lapack\_lite and just await the necessary work.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()
\>>> a \= rng.normal(size\=(9, 6))
\>>> Q, R \= np.linalg.qr(a)
\>>> np.allclose(a, np.dot(Q, R))  \# a does equal QR
True
\>>> R2 \= np.linalg.qr(a, mode\='r')
\>>> np.allclose(R, R2)  \# mode='r' returns the same R as mode='full'
True
\>>> a \= np.random.normal(size\=(3, 2, 2)) \# Stack of 2 x 2 matrices as input
\>>> Q, R \= np.linalg.qr(a)
\>>> Q.shape
(3, 2, 2)
\>>> R.shape
(3, 2, 2)
\>>> np.allclose(a, np.matmul(Q, R))
True

Copy to clipboard

Example illustrating a common use of [`qr`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html#numpy.linalg.qr "numpy.linalg.qr")
: solving of least squares problems

What are the least-squares-best _m_ and _y0_ in `y = y0 + mx` for the following data: {(0,1), (1,0), (1,2), (2,1)}. (Graph the points and you’ll see that it should be y0 = 0, m = 1.) The answer is provided by solving the over-determined matrix equation `Ax = b`, where:

A \= array(\[\[0, 1\], \[1, 1\], \[1, 1\], \[2, 1\]\])
x \= array(\[\[y0\], \[m\]\])
b \= array(\[\[1\], \[0\], \[2\], \[1\]\])

Copy to clipboard

If A = QR such that Q is orthonormal (which is always possible via Gram-Schmidt), then `x = inv(R) * (Q.T) * b`. (In numpy practice, however, we simply use [`lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
.)

\>>> A \= np.array(\[\[0, 1\], \[1, 1\], \[1, 1\], \[2, 1\]\])
\>>> A
array(\[\[0, 1\],\
       \[1, 1\],\
       \[1, 1\],\
       \[2, 1\]\])
\>>> b \= np.array(\[1, 2, 2, 3\])
\>>> Q, R \= np.linalg.qr(A)
\>>> p \= np.dot(Q.T, b)
\>>> np.dot(np.linalg.inv(R), p)
array(\[  1.,   1.\])

Copy to clipboard

Go BackOpen In Tab

On this page