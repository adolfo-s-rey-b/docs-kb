[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.shuffle.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.shuffle.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.shuffle.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.shuffle.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.shuffle.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.shuffle.html)

Collapse Sidebar Expand Sidebar

shuffle[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#shuffle "Link to this heading")

========================================================================================================================

sklearn.utils.shuffle(_\*arrays_, _random\_state\=None_, _n\_samples\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_indexing.py#L615)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "Link to this definition")

Shuffle arrays or sparse matrices in a consistent way.

This is a convenience alias to `resample(*arrays, replace=False)` to do random permutations of the collections.

Parameters:

**\*arrays**sequence of indexable data-structures

Indexable data-structures can be arrays, lists, dataframes or scipy sparse matrices with consistent first dimension.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for shuffling the data. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_samples**int, default=None

Number of samples to generate. If left to None this is automatically set to the first dimension of the arrays. It should not be larger than the length of arrays.

Returns:

**shuffled\_arrays**sequence of indexable data-structures

Sequence of shuffled copies of the collections. The original arrays are not impacted.

See also

[`resample`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#sklearn.utils.resample "sklearn.utils.resample")

Resample arrays or sparse matrices in a consistent way.

Examples

It is possible to mix sparse and dense arrays in the same run:

\>>> import numpy as np
\>>> X \= np.array(\[\[1., 0.\], \[2., 1.\], \[0., 0.\]\])
\>>> y \= np.array(\[0, 1, 2\])

\>>> from scipy.sparse import coo\_array
\>>> X\_sparse \= coo\_array(X)

\>>> from sklearn.utils import shuffle
\>>> X, X\_sparse, y \= shuffle(X, X\_sparse, y, random\_state\=0)
\>>> X
array(\[\[0., 0.\],\
       \[2., 1.\],\
       \[1., 0.\]\])

\>>> X\_sparse
<Compressed Sparse Row sparse array of dtype 'float64'
    with 3 stored elements and shape (3, 2)>

\>>> X\_sparse.toarray()
array(\[\[0., 0.\],\
       \[2., 1.\],\
       \[1., 0.\]\])

\>>> y
array(\[2, 1, 0\])

\>>> shuffle(y, n\_samples\=2, random\_state\=0)
array(\[0, 1\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_thumb.png)

[Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)

Prediction Latency

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_thumb.png)

[Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)

Early stopping of Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)