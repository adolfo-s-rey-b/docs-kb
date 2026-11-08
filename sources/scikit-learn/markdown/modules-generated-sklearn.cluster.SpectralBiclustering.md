[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.SpectralBiclustering.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.SpectralBiclustering.html)

Collapse Sidebar Expand Sidebar

SpectralBiclustering[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#spectralbiclustering "Link to this heading")

=================================================================================================================================================================

class sklearn.cluster.SpectralBiclustering(_n\_clusters\=3_, _\*_, _method\='bistochastic'_, _n\_components\=6_, _n\_best\=3_, _svd\_method\='randomized'_, _n\_svd\_vecs\=None_, _mini\_batch\=False_, _init\='k-means++'_, _n\_init\=10_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bicluster.py#L360)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "Link to this definition")

Spectral biclustering (Kluger, 2003) [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#r2af9f5762274-1)
.

Partitions rows and columns under the assumption that the data has an underlying checkerboard structure. For instance, if there are two row partitions and three column partitions, each row will belong to three biclusters, and each column will belong to two biclusters. The outer product of the corresponding row and column label vectors gives this checkerboard structure.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/biclustering.html#spectral-biclustering)
.

Parameters:

**n\_clusters**int or tuple (n\_row\_clusters, n\_column\_clusters), default=3

The number of row and column clusters in the checkerboard structure.

**method**{‘bistochastic’, ‘scale’, ‘log’}, default=’bistochastic’

Method of normalizing and converting singular vectors into biclusters. May be one of ‘scale’, ‘bistochastic’, or ‘log’. The authors recommend using ‘log’. If the data is sparse, however, log normalization will not work, which is why the default is ‘bistochastic’.

Warning

if `method='log'`, the data must not be sparse.

**n\_components**int, default=6

Number of singular vectors to check.

**n\_best**int, default=3

Number of best singular vectors to which to project the data for clustering.

**svd\_method**{‘randomized’, ‘arpack’}, default=’randomized’

Selects the algorithm for finding singular vectors. May be ‘randomized’ or ‘arpack’. If ‘randomized’, uses [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
, which may be faster for large matrices. If ‘arpack’, uses `scipy.sparse.linalg.svds`, which is more accurate, but possibly slower in some cases.

**n\_svd\_vecs**int, default=None

Number of vectors to use in calculating the SVD. Corresponds to `ncv` when `svd_method=arpack` and `n_oversamples` when `svd_method` is ‘randomized\`.

**mini\_batch**bool, default=False

Whether to use mini-batch k-means, which is faster but may get different results.

**init**{‘k-means++’, ‘random’} or ndarray of shape (n\_clusters, n\_features), default=’k-means++’

Method for initialization of k-means algorithm; defaults to ‘k-means++’.

**n\_init**int, default=10

Number of random initializations that are tried with the k-means algorithm.

If mini-batch k-means is used, the best initialization is chosen and the algorithm runs once. Otherwise, the algorithm is run for each initialization and the best solution chosen.

**random\_state**int, RandomState instance, default=None

Used for randomizing the singular value decomposition and the k-means initialization. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**rows\_**array-like of shape (n\_row\_clusters, n\_rows)

Results of the clustering. `rows[i, r]` is True if cluster `i` contains row `r`. Available only after calling `fit`.

**columns\_**array-like of shape (n\_column\_clusters, n\_columns)

Results of the clustering, like `rows`.

**row\_labels\_**array-like of shape (n\_rows,)

Row partition labels.

**column\_labels\_**array-like of shape (n\_cols,)

Column partition labels.

`biclusters_`tuple of two ndarrays

Convenient way to get row and column indicators together.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`SpectralCoclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")

Clusters rows and columns of an array `X` to solve the relaxed normalized cut of the bipartite graph created from `X`.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#id1)\
\]

[Kluger, Yuval, et. al., 2003. Spectral biclustering of microarray data: coclustering genes and conditions.](https://doi.org/10.1101/gr.648603)

Examples

\>>> from sklearn.cluster import SpectralBiclustering
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> clustering \= SpectralBiclustering(n\_clusters\=2, random\_state\=0).fit(X)
\>>> clustering.row\_labels\_
array(\[1, 1, 1, 0, 0, 0\], dtype=int32)
\>>> clustering.column\_labels\_
array(\[1, 0\], dtype=int32)
\>>> clustering
SpectralBiclustering(n\_clusters=2, random\_state=0)

Copy to clipboard

For a more detailed example, see [A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#sphx-glr-auto-examples-bicluster-plot-spectral-biclustering-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bicluster.py#L117)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.fit "Link to this definition")

Create a biclustering for X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

SpectralBiclustering instance.

get\_indices(_i_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L809)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.get_indices "Link to this definition")

Row and column indices of the `i`’th bicluster.

Only works if `rows_` and `columns_` attributes exist.

Parameters:

**i**int

The index of the cluster.

Returns:

**row\_ind**ndarray, dtype=np.intp

Indices of rows in the dataset that belong to the bicluster.

**col\_ind**ndarray, dtype=np.intp

Indices of columns in the dataset that belong to the bicluster.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_shape(_i_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L830)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.get_shape "Link to this definition")

Shape of the `i`’th bicluster.

Parameters:

**i**int

The index of the cluster.

Returns:

**n\_rows**int

Number of rows in the bicluster.

**n\_cols**int

Number of columns in the bicluster.

get\_submatrix(_i_, _data_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L849)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.get_submatrix "Link to this definition")

Return the submatrix corresponding to bicluster `i`.

Parameters:

**i**int

The index of the cluster.

**data**array-like of shape (n\_samples, n\_features)

The data.

Returns:

**submatrix**ndarray of shape (n\_rows, n\_cols)

The submatrix corresponding to bicluster `i`.

Notes

Works with sparse matrices. Only works if `rows_` and `columns_` attributes exist.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_thumb.png)

[A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)

A demo of the Spectral Biclustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)