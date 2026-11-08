[Skip to main content](https://scikit-learn.org/stable/modules/generated/fastica-function.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/fastica-function.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/fastica-function.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/fastica-function.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/fastica-function.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/fastica-function.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/fastica-function.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/fastica-function.html)

Collapse Sidebar Expand Sidebar

fastica[#](https://scikit-learn.org/stable/modules/generated/fastica-function.html#fastica "Link to this heading")

===================================================================================================================

sklearn.decomposition.fastica(_X_, _n\_components\=None_, _\*_, _algorithm\='parallel'_, _whiten\='unit-variance'_, _fun\='logcosh'_, _fun\_args\=None_, _max\_iter\=200_, _tol\=0.0001_, _w\_init\=None_, _whiten\_solver\='svd'_, _random\_state\=None_, _return\_X\_mean\=False_, _compute\_sources\=True_, _return\_n\_iter\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L171)
[#](https://scikit-learn.org/stable/modules/generated/fastica-function.html#sklearn.decomposition.fastica "Link to this definition")

Perform Fast Independent Component Analysis.

The implementation is based on [\[1\]](https://scikit-learn.org/stable/modules/generated/fastica-function.html#r4ef46ec4ecf2-1)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#ica)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**n\_components**int, default=None

Number of components to use. If None is passed, all are used.

**algorithm**{‘parallel’, ‘deflation’}, default=’parallel’

Specify which algorithm to use for FastICA.

**whiten**str or bool, default=’unit-variance’

Specify the whitening strategy to use.

*   If ‘arbitrary-variance’, a whitening with variance arbitrary is used.
    
*   If ‘unit-variance’, the whitening matrix is rescaled to ensure that each recovered source has unit variance.
    
*   If False, the data is already considered to be whitened, and no whitening is performed.
    

Changed in version 1.3: The default value of `whiten` changed to ‘unit-variance’ in 1.3.

**fun**{‘logcosh’, ‘exp’, ‘cube’} or callable, default=’logcosh’

The functional form of the G function used in the approximation to neg-entropy. Could be either ‘logcosh’, ‘exp’, or ‘cube’. You can also provide your own function. It should return a tuple containing the value of the function, and of its derivative, in the point. The derivative should be averaged along its last dimension. Example:

def my\_g(x):
    return x \*\* 3, (3 \* x \*\* 2).mean(axis\=-1)

Copy to clipboard

**fun\_args**dict, default=None

Arguments to send to the functional form. If empty or None and if fun=’logcosh’, fun\_args will take value {‘alpha’ : 1.0}.

**max\_iter**int, default=200

Maximum number of iterations to perform.

**tol**float, default=1e-4

A positive scalar giving the tolerance at which the un-mixing matrix is considered to have converged.

**w\_init**ndarray of shape (n\_components, n\_components), default=None

Initial un-mixing array. If `w_init=None`, then an array of values drawn from a normal distribution is used.

**whiten\_solver**{“eigh”, “svd”}, default=”svd”

The solver to use for whitening.

*   “svd” is more stable numerically if the problem is degenerate, and often faster when `n_samples <= n_features`.
    
*   “eigh” is generally more memory efficient when `n_samples >= n_features`, and can be faster when `n_samples >= 50 * n_features`.
    

Added in version 1.2.

**random\_state**int, RandomState instance or None, default=None

Used to initialize `w_init` when not specified, with a normal distribution. Pass an int, for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**return\_X\_mean**bool, default=False

If True, X\_mean is returned too.

**compute\_sources**bool, default=True

If False, sources are not computed, but only the rotation matrix. This can save memory when working with big data. Defaults to True.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

Returns:

**K**ndarray of shape (n\_components, n\_features) or None

If whiten is ‘True’, K is the pre-whitening matrix that projects data onto the first n\_components principal components. If whiten is ‘False’, K is ‘None’.

**W**ndarray of shape (n\_components, n\_components)

The square matrix that unmixes the data after whitening. The mixing matrix is the pseudo-inverse of matrix `W K` if K is not None, else it is the inverse of W.

**S**ndarray of shape (n\_samples, n\_components) or None

Estimated source matrix.

**X\_mean**ndarray of shape (n\_features,)

The mean over features. Returned only if return\_X\_mean is True.

**n\_iter**int

If the algorithm is “deflation”, n\_iter is the maximum number of iterations run across all components. Else they are just the number of iterations taken to converge. This is returned only when return\_n\_iter is set to `True`.

Notes

The data matrix X is considered to be a linear combination of non-Gaussian (independent) components i.e. X = AS where columns of S contain the independent components and A is a linear mixing matrix. In short ICA attempts to ``` un-mix' the data by estimating an un-mixing matrix W where ``S = W K X.` ``` While FastICA was proposed to estimate as many sources as features, it is possible to estimate less by setting n\_components < n\_features. It this case K is not a square matrix and the estimated A is the pseudo-inverse of `W K`.

This implementation was originally made for data of shape \[n\_features, n\_samples\]. Now the input is transposed before the algorithm is applied. This makes it slightly faster for Fortran-ordered input.

References

\[[1](https://scikit-learn.org/stable/modules/generated/fastica-function.html#id1)\
\]

A. Hyvarinen and E. Oja, “Fast Independent Component Analysis”, Algorithms and Applications, Neural Networks, 13(4-5), 2000, pp. 411-430.

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.decomposition import fastica
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> K, W, S \= fastica(X, n\_components\=7, random\_state\=0, whiten\='unit-variance')
\>>> K.shape
(7, 64)
\>>> W.shape
(7, 7)
\>>> S.shape
(1797, 7)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)