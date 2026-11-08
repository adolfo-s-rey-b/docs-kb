[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.smacof.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.smacof.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.smacof.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.smacof.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.smacof.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.smacof.html)

Collapse Sidebar Expand Sidebar

smacof[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#smacof "Link to this heading")

========================================================================================================================

sklearn.manifold.smacof(_dissimilarities_, _\*_, _metric\=True_, _n\_components\=2_, _init\=None_, _n\_init\=1_, _n\_jobs\=None_, _max\_iter\=300_, _verbose\=0_, _eps\=1e-06_, _random\_state\=None_, _return\_n\_iter\=False_, _normalized\_stress\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_mds.py#L198)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#sklearn.manifold.smacof "Link to this definition")

Compute multidimensional scaling using the SMACOF algorithm.

The SMACOF (Scaling by MAjorizing a COmplicated Function) algorithm is a multidimensional scaling algorithm which minimizes an objective function (the _stress_) using a majorization technique. Stress majorization, also known as the Guttman Transform, guarantees a monotone convergence of stress, and is more powerful than traditional techniques such as gradient descent.

The SMACOF algorithm for metric MDS can be summarized by the following steps:

1.  Set an initial start configuration, randomly or not.
    
2.  Compute the stress
    
3.  Compute the Guttman Transform
    
4.  Iterate 2 and 3 until convergence.
    

The nonmetric algorithm adds a monotonic regression step before computing the stress.

Parameters:

**dissimilarities**array-like of shape (n\_samples, n\_samples)

Pairwise dissimilarities between the points. Must be symmetric.

**metric**bool, default=True

Compute metric or nonmetric SMACOF algorithm. When `False` (i.e. non-metric MDS), dissimilarities with 0 are considered as missing values.

**n\_components**int, default=2

Number of dimensions in which to immerse the dissimilarities. If an `init` array is provided, this option is overridden and the shape of `init` is used to determine the dimensionality of the embedding space.

**init**array-like of shape (n\_samples, n\_components), default=None

Starting configuration of the embedding to initialize the algorithm. By default, the algorithm is initialized with a randomly chosen array.

**n\_init**int, default=1

Number of times the SMACOF algorithm will be run with different initializations. The final results will be the best output of the runs, determined by the run with the smallest final stress. If `init` is provided, this option is overridden and a single run is performed.

Changed in version 1.9: The default value for `n_iter` changed from 8 to 1.

**n\_jobs**int, default=None

The number of jobs to use for the computation. If multiple initializations are used (`n_init`), each run of the algorithm is computed in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**max\_iter**int, default=300

Maximum number of iterations of the SMACOF algorithm for a single run.

**verbose**int, default=0

Level of verbosity.

**eps**float, default=1e-6

The tolerance with respect to stress (normalized by the sum of squared embedding distances) at which to declare convergence.

Changed in version 1.7: The default value for `eps` has changed from 1e-3 to 1e-6, as a result of a bugfix in the computation of the convergence criterion.

**random\_state**int, RandomState instance or None, default=None

Determines the random number generator used to initialize the centers. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

**normalized\_stress**bool or “auto”, default=”auto”

Whether to return normalized stress value (Stress-1) instead of raw stress. By default, metric MDS returns raw stress while non-metric MDS returns normalized stress.

Added in version 1.2.

Changed in version 1.4: The default value changed from `False` to `"auto"` in version 1.4.

Changed in version 1.7: Normalized stress is now supported for metric MDS as well.

Returns:

**X**ndarray of shape (n\_samples, n\_components)

Coordinates of the points in a `n_components`\-space.

**stress**float

The final value of the stress (sum of squared distance of the disparities and the distances for all constrained points). If `normalized_stress=True`, returns Stress-1. A value of 0 indicates “perfect” fit, 0.025 excellent, 0.05 good, 0.1 fair, and 0.2 poor [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#r8e3dcaa71efe-1)
.

**n\_iter**int

The number of iterations corresponding to the best stress. Returned only if `return_n_iter` is set to `True`.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#id1)\
\]

“Nonmetric multidimensional scaling: a numerical method” Kruskal, J. Psychometrika, 29 (1964)

\[2\]

“Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis” Kruskal, J. Psychometrika, 29, (1964)

\[3\]

“Modern Multidimensional Scaling - Theory and Applications” Borg, I.; Groenen P. Springer Series in Statistics (1997)

Examples

\>>> import numpy as np
\>>> from sklearn.manifold import smacof
\>>> from sklearn.metrics import euclidean\_distances
\>>> X \= np.array(\[\[0, 1, 2\], \[1, 0, 3\], \[2, 3, 0\]\])
\>>> dissimilarities \= euclidean\_distances(X)
\>>> Z, stress \= smacof(
...     dissimilarities, n\_components\=2, n\_init\=1, eps\=1e-6, random\_state\=42
... )
\>>> Z.shape
(3, 2)
\>>> np.round(stress, 6).item()
3.2e-05

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)