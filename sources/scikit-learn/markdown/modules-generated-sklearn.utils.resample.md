[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.resample.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.resample.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.resample.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.resample.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.resample.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.resample.html)

Collapse Sidebar Expand Sidebar

resample[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#resample "Link to this heading")

===========================================================================================================================

sklearn.utils.resample(_\*arrays_, _replace\=True_, _n\_samples\=None_, _random\_state\=None_, _stratify\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_indexing.py#L418)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#sklearn.utils.resample "Link to this definition")

Resample arrays or sparse matrices in a consistent way.

The default strategy implements one step of the bootstrapping procedure.

Parameters:

**\*arrays**sequence of array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Indexable data-structures can be arrays, lists, dataframes or scipy sparse matrices with consistent first dimension.

**replace**bool, default=True

Implements resampling with replacement. It must be set to True whenever sampling with non-uniform weights: a few data points with very large weights are expected to be sampled several times with probability to preserve the distribution induced by the weights. If False, this will implement (sliced) random permutations.

**n\_samples**int, default=None

Number of samples to generate. If left to None this is automatically set to the first dimension of the arrays. If replace is False it should not be larger than the length of arrays.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for shuffling the data. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**stratify**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

If not None, data is split in a stratified fashion, using this as the class labels.

**sample\_weight**array-like of shape (n\_samples,), default=None

Contains weight values to be associated with each sample. Values are normalized to sum to one and interpreted as probability for sampling each data point.

Added in version 1.7.

Returns:

**resampled\_arrays**sequence of array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Sequence of resampled copies of the collections. The original arrays are not impacted.

See also

[`shuffle`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")

Shuffle arrays or sparse matrices in a consistent way.

Examples

It is possible to mix sparse and dense arrays in the same run:

\>>> import numpy as np
\>>> X \= np.array(\[\[1., 0.\], \[2., 1.\], \[0., 0.\]\])
\>>> y \= np.array(\[0, 1, 2\])

\>>> from scipy.sparse import coo\_array
\>>> X\_sparse \= coo\_array(X)

\>>> from sklearn.utils import resample
\>>> X, X\_sparse, y \= resample(X, X\_sparse, y, random\_state\=0)
\>>> X
array(\[\[1., 0.\],\
       \[2., 1.\],\
       \[1., 0.\]\])

\>>> X\_sparse
<Compressed Sparse Row sparse array of dtype 'float64'
    with 4 stored elements and shape (3, 2)>

\>>> X\_sparse.toarray()
array(\[\[1., 0.\],\
       \[2., 1.\],\
       \[1., 0.\]\])

\>>> y
array(\[0, 1, 0\])

\>>> resample(y, n\_samples\=2, random\_state\=0)
array(\[0, 1\])

Copy to clipboard

Example using stratification:

\>>> y \= \[0, 0, 1, 1, 1, 1, 1, 1, 1\]
\>>> resample(y, n\_samples\=5, replace\=False, stratify\=y,
...          random\_state\=0)
\[1, 1, 1, 0, 1\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)