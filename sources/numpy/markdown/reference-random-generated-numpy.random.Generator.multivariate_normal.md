[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.multivariate_normal.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.multivariate_normal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.multivariate\_normal[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#numpy-random-generator-multivariate-normal "Link to this heading")

==========================================================================================================================================================================================================================

method

random.Generator.multivariate\_normal(_mean_, _cov_, _size\=None_, _check\_valid\='warn'_, _tol\=1e-8_, _\*_, _method\='svd'_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#numpy.random.Generator.multivariate_normal "Link to this definition")

Draw random samples from a multivariate normal distribution.

The multivariate normal, multinormal or Gaussian distribution is a generalization of the one-dimensional normal distribution to higher dimensions. Such a distribution is specified by its mean and covariance matrix. These parameters are analogous to the mean (average or “center”) and variance (the squared standard deviation, or “width”) of the one-dimensional normal distribution.

Parameters:

**mean**1-D array\_like, of length N

Mean of the N-dimensional distribution.

**cov**2-D array\_like, of shape (N, N)

Covariance matrix of the distribution. It must be symmetric and positive-semidefinite for proper sampling.

**size**int or tuple of ints, optional

Given a shape of, for example, `(m,n,k)`, `m*n*k` samples are generated, and packed in an _m_\-by-_n_\-by-_k_ arrangement. Because each sample is _N_\-dimensional, the output shape is `(m,n,k,N)`. If no shape is specified, a single (_N_\-D) sample is returned.

**check\_valid**{ ‘warn’, ‘raise’, ‘ignore’ }, optional

Behavior when the covariance matrix is not positive semidefinite.

**tol**float, optional

Tolerance when checking the singular values in covariance matrix. cov is cast to double before the check.

**method**{ ‘svd’, ‘eigh’, ‘cholesky’}, optional

The cov input is used to compute a factor matrix A such that `A @ A.T = cov`. This argument is used to select the method used to compute the factor matrix A. The default method ‘svd’ is the slowest, while ‘cholesky’ is the fastest but less robust than the slowest method. The method _eigh_ uses eigen decomposition to compute A and is faster than svd but slower than cholesky.

Returns:

**out**ndarray

The drawn samples, of shape _size_, if that was provided. If not, the shape is `(N,)`.

In other words, each entry `out[i,j,...,:]` is an N-dimensional value drawn from the distribution.

Notes

The mean is a coordinate in N-dimensional space, which represents the location where samples are most likely to be generated. This is analogous to the peak of the bell curve for the one-dimensional or univariate normal distribution.

Covariance indicates the level to which two variables vary together. From the multivariate normal distribution, we draw N-dimensional samples, \\(X = \[x\_1, x\_2, ..., x\_N\]\\). The covariance matrix element \\(C\_{ij}\\) is the covariance of \\(x\_i\\) and \\(x\_j\\). The element \\(C\_{ii}\\) is the variance of \\(x\_i\\) (i.e. its “spread”).

Instead of specifying the full covariance matrix, popular approximations include:

*   Spherical covariance ([`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")
     is a multiple of the identity matrix)
    
*   Diagonal covariance ([`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")
     has non-negative elements, and only on the diagonal)
    

This geometrical property can be seen in two dimensions by plotting generated data-points:

\>>> mean \= \[0, 0\]
\>>> cov \= \[\[1, 0\], \[0, 100\]\]  \# diagonal covariance

Copy to clipboard

Diagonal covariance means that the variables are independent, and the probability density contours have their axes aligned with the coordinate axes:

\>>> import matplotlib.pyplot as plt
\>>> rng \= np.random.default\_rng()
\>>> x, y \= rng.multivariate\_normal(mean, cov, 5000).T
\>>> plt.plot(x, y, 'x')
\>>> plt.axis('equal')
\>>> plt.show()

Copy to clipboard

Note that the covariance matrix must be positive semidefinite (a.k.a. nonnegative-definite). Otherwise, the behavior of this method is undefined and backwards compatibility is not guaranteed.

This function internally uses linear algebra routines, and thus results may not be identical (even up to precision) across architectures, OSes, or even builds. For example, this is likely if `cov` has multiple equal singular values and `method` is `'svd'` (default). In this case, `method='cholesky'` may be more robust.

References

\[1\]

Papoulis, A., “Probability, Random Variables, and Stochastic Processes,” 3rd ed., New York: McGraw-Hill, 1991.

\[2\]

Duda, R. O., Hart, P. E., and Stork, D. G., “Pattern Classification,” 2nd ed., New York: Wiley, 2001.

Examples

Try it in your browser!

\>>> mean \= (1, 2)
\>>> cov \= \[\[1, 0\], \[0, 1\]\]
\>>> rng \= np.random.default\_rng()
\>>> x \= rng.multivariate\_normal(mean, cov, (3, 3))
\>>> x.shape
(3, 3, 2)

Copy to clipboard

We can use a different method other than the default to factorize cov:

\>>> y \= rng.multivariate\_normal(mean, cov, (3, 3), method\='cholesky')
\>>> y.shape
(3, 3, 2)

Copy to clipboard

Here we generate 800 samples from the bivariate normal distribution with mean \[0, 0\] and covariance matrix \[\[6, -3\], \[-3, 3.5\]\]. The expected variances of the first and second components of the sample are 6 and 3.5, respectively, and the expected correlation coefficient is -3/sqrt(6\*3.5) ≈ -0.65465.

\>>> cov \= np.array(\[\[6, \-3\], \[\-3, 3.5\]\])
\>>> pts \= rng.multivariate\_normal(\[0, 0\], cov, size\=800)

Copy to clipboard

Check that the mean, covariance, and correlation coefficient of the sample are close to the expected values:

\>>> pts.mean(axis\=0)
array(\[ 0.0326911 , -0.01280782\])  # may vary
\>>> np.cov(pts.T)
array(\[\[ 5.96202397, -2.85602287\],\
       \[-2.85602287,  3.47613949\]\])  # may vary
\>>> np.corrcoef(pts.T)\[0, 1\]
\-0.6273591314603949  # may vary

Copy to clipboard

We can visualize this data with a scatter plot. The orientation of the point cloud illustrates the negative correlation of the components of this sample.

\>>> import matplotlib.pyplot as plt
\>>> plt.plot(pts\[:, 0\], pts\[:, 1\], '.', alpha\=0.5)
\>>> plt.axis('equal')
\>>> plt.grid()
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-multivariate_normal-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-multivariate_normal-1.png)

Go BackOpen In Tab

On this page