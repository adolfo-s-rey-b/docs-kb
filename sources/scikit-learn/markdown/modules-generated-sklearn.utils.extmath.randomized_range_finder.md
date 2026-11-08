[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.randomized_range_finder.html)

Collapse Sidebar Expand Sidebar

randomized\_range\_finder[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#randomized-range-finder "Link to this heading")

==================================================================================================================================================================================

sklearn.utils.extmath.randomized\_range\_finder(_A_, _\*_, _size_, _n\_iter_, _power\_iteration\_normalizer\='auto'_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L241)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "Link to this definition")

Compute an orthonormal matrix whose range approximates the range of A.

Parameters:

**A**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data matrix.

**size**int

Size of the return array.

**n\_iter**int

Number of power iterations used to stabilize the result.

**power\_iteration\_normalizer**{‘auto’, ‘QR’, ‘LU’, ‘none’}, default=’auto’

Whether the power iterations are normalized with step-by-step QR factorization (the slowest but most accurate), ‘none’ (the fastest but numerically unstable when `n_iter` is large, e.g. typically 5 or larger), or ‘LU’ factorization (numerically stable but can lose slightly in accuracy). The ‘auto’ mode applies no normalization if `n_iter` <= 2 and switches to LU otherwise.

Added in version 0.18.

**random\_state**int, RandomState instance or None, default=None

The seed of the pseudo random number generator to use when shuffling the data, i.e. getting the random vectors to initialize the algorithm. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**Q**ndarray of shape (size, size)

A projection matrix, the range of which approximates well the range of the input matrix A.

Notes

Follows Algorithm 4.3 of [“Finding structure with randomness: Stochastic algorithms for constructing approximate matrix decompositions”](https://arxiv.org/abs/0909.4061)
 Halko, et al. (2009)

An implementation of a randomized algorithm for principal component analysis A. Szlam et al. 2014

Examples

\>>> import numpy as np
\>>> from sklearn.utils.extmath import randomized\_range\_finder
\>>> A \= np.array(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\])
\>>> randomized\_range\_finder(A, size\=2, n\_iter\=2, random\_state\=42)
array(\[\[-0.214,  0.887\],\
       \[-0.521,  0.249\],\
       \[-0.826, -0.388\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)