[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.non_negative_factorization.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.non_negative_factorization.html)

Collapse Sidebar Expand Sidebar

non\_negative\_factorization[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#non-negative-factorization "Link to this heading")

===========================================================================================================================================================================================

sklearn.decomposition.non\_negative\_factorization(_X_, _W\=None_, _H\=None_, _n\_components\='auto'_, _\*_, _init\=None_, _update\_H\=True_, _solver\='cd'_, _beta\_loss\='frobenius'_, _tol\=0.0001_, _max\_iter\=200_, _alpha\_W\=0.0_, _alpha\_H\='same'_, _l1\_ratio\=0.0_, _random\_state\=None_, _verbose\=0_, _shuffle\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L891)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "Link to this definition")

Compute Non-negative Matrix Factorization (NMF).

Find two non-negative matrices (W, H) whose product approximates the non- negative matrix X. This factorization can be used for example for dimensionality reduction, source separation or topic extraction.

The objective function is:

L(W,H)\=0.5∗||X−WH||loss2+alpha\_W∗l1\_ratio∗n\_features∗||vec(W)||1+alpha\_H∗l1\_ratio∗n\_samples∗||vec(H)||1+0.5∗alpha\_W∗(1−l1\_ratio)∗n\_features∗||W||Fro2+0.5∗alpha\_H∗(1−l1\_ratio)∗n\_samples∗||H||Fro2,

where ||A||Fro2\=∑i,jAij2 (Frobenius norm) and ||vec(A)||1\=∑i,jabs(Aij) (Elementwise L1 norm)

The generic norm ||X−WH||loss2 may represent the Frobenius norm or another supported beta-divergence loss. The choice between options is controlled by the `beta_loss` parameter.

The regularization terms are scaled by `n_features` for `W` and by `n_samples` for `H` to keep their impact balanced with respect to one another and to the data fit term as independent as possible of the size `n_samples` of the training set.

The objective function is minimized with an alternating minimization of W and H. If H is given and update\_H=False, it solves for W only.

Note that the transformed data is named W and the components matrix is named H. In the NMF literature, the naming convention is usually the opposite since the data matrix X is transposed.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Constant matrix.

**W**array-like of shape (n\_samples, n\_components), default=None

If `init='custom'`, it is used as initial guess for the solution. If `update_H=False`, it is initialised as an array of zeros, unless `solver='mu'`, then it is filled with values calculated by `np.sqrt(X.mean() / self._n_components)`. If `None`, uses the initialisation method specified in `init`.

**H**array-like of shape (n\_components, n\_features), default=None

If `init='custom'`, it is used as initial guess for the solution. If `update_H=False`, it is used as a constant, to solve for W only. If `None`, uses the initialisation method specified in `init`.

**n\_components**int or {‘auto’} or None, default=’auto’

Number of components. If `None`, all features are kept. If `n_components='auto'`, the number of components is automatically inferred from `W` or `H` shapes.

Changed in version 1.4: Added `'auto'` value.

Changed in version 1.6: Default value changed from `None` to `'auto'`.

**init**{‘random’, ‘nndsvd’, ‘nndsvda’, ‘nndsvdar’, ‘custom’}, default=None

Method used to initialize the procedure.

Valid options:

*   None: ‘nndsvda’ if n\_components < n\_features, otherwise ‘random’.
    
*   ‘random’: non-negative random matrices, scaled with: `sqrt(X.mean() / n_components)`
    
*   ‘nndsvd’: Nonnegative Double Singular Value Decomposition (NNDSVD) initialization (better for sparseness)
    
*   ‘nndsvda’: NNDSVD with zeros filled with the average of X (better when sparsity is not desired)
    
*   ‘nndsvdar’: NNDSVD with zeros filled with small random values (generally faster, less accurate alternative to NNDSVDa for when sparsity is not desired)
    
*   ‘custom’: If `update_H=True`, use custom matrices W and H which must both be provided. If `update_H=False`, then only custom matrix H is used.
    

Changed in version 0.23: The default value of `init` changed from ‘random’ to None in 0.23.

Changed in version 1.1: When `init=None` and n\_components is less than n\_samples and n\_features defaults to `nndsvda` instead of `nndsvd`.

**update\_H**bool, default=True

Set to True, both W and H will be estimated from initial guesses. Set to False, only W will be estimated.

**solver**{‘cd’, ‘mu’}, default=’cd’

Numerical solver to use:

*   ‘cd’ is a Coordinate Descent solver that uses Fast Hierarchical Alternating Least Squares (Fast HALS).
    
*   ‘mu’ is a Multiplicative Update solver.
    

Added in version 0.17: Coordinate Descent solver.

Added in version 0.19: Multiplicative Update solver.

**beta\_loss**float or {‘frobenius’, ‘kullback-leibler’, ‘itakura-saito’}, default=’frobenius’

Beta divergence to be minimized, measuring the distance between X and the dot product WH. Note that values different from ‘frobenius’ (or 2) and ‘kullback-leibler’ (or 1) lead to significantly slower fits. Note that for beta\_loss <= 0 (or ‘itakura-saito’), the input matrix X cannot contain zeros. Used only in ‘mu’ solver.

Added in version 0.19.

**tol**float, default=1e-4

Tolerance of the stopping condition.

**max\_iter**int, default=200

Maximum number of iterations before timing out.

**alpha\_W**float, default=0.0

Constant that multiplies the regularization terms of `W`. Set it to zero (default) to have no regularization on `W`.

Added in version 1.0.

**alpha\_H**float or “same”, default=”same”

Constant that multiplies the regularization terms of `H`. Set it to zero to have no regularization on `H`. If “same” (default), it takes the same value as `alpha_W`.

Added in version 1.0.

**l1\_ratio**float, default=0.0

The regularization mixing parameter, with 0 <= l1\_ratio <= 1. For l1\_ratio = 0 the penalty is an elementwise L2 penalty (aka Frobenius Norm). For l1\_ratio = 1 it is an elementwise L1 penalty. For 0 < l1\_ratio < 1, the penalty is a combination of L1 and L2.

**random\_state**int, RandomState instance or None, default=None

Used for NMF initialisation (when `init` == ‘nndsvdar’ or ‘random’), and in Coordinate Descent. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**int, default=0

The verbosity level.

**shuffle**bool, default=False

If true, randomize the order of coordinates in the CD solver.

Returns:

**W**ndarray of shape (n\_samples, n\_components)

Solution to the non-negative least squares problem.

**H**ndarray of shape (n\_components, n\_features)

Solution to the non-negative least squares problem.

**n\_iter**int

Actual number of iterations.

References

\[1\]

[“Fast local algorithms for large scale nonnegative matrix and tensor factorizations”](https://doi.org/10.1587/transfun.E92.A.708)
 Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals of electronics, communications and computer sciences 92.3: 708-721, 2009.

\[2\]

[“Algorithms for nonnegative matrix factorization with the beta-divergence”](https://doi.org/10.1162/NECO_a_00168)
 Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

Examples

\>>> import numpy as np
\>>> X \= np.array(\[\[1,1\], \[2, 1\], \[3, 1.2\], \[4, 1\], \[5, 0.8\], \[6, 1\]\])
\>>> from sklearn.decomposition import non\_negative\_factorization
\>>> W, H, n\_iter \= non\_negative\_factorization(
...     X, n\_components\=2, init\='random', random\_state\=0)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)