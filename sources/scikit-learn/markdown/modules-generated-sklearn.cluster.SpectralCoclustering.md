[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.SpectralCoclustering.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.SpectralCoclustering.html)

Collapse Sidebar Expand Sidebar

SpectralCoclustering[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#spectralcoclustering "Link to this heading")

=================================================================================================================================================================

class sklearn.cluster.SpectralCoclustering(_n\_clusters\=3_, _\*_, _svd\_method\='randomized'_, _n\_svd\_vecs\=None_, _mini\_batch\=False_, _init\='k-means++'_, _n\_init\=10_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bicluster.py#L202)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "Link to this definition")

Spectral Co-Clustering algorithm (Dhillon, 2001) [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#r0dd0f3306ba7-1)
.

Clusters rows and columns of an array `X` to solve the relaxed normalized cut of the bipartite graph created from `X` as follows: the edge between row vertex `i` and column vertex `j` has weight `X[i, j]`.

The resulting bicluster structure is block-diagonal, since each row and each column belongs to exactly one bicluster.

Supports sparse matrices, as long as they are nonnegative.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/biclustering.html#spectral-coclustering)
.

Parameters:

**n\_clusters**int, default=3

The number of biclusters to find.

**svd\_method**{‘randomized’, ‘arpack’}, default=’randomized’

Selects the algorithm for finding singular vectors. May be ‘randomized’ or ‘arpack’. If ‘randomized’, use [`sklearn.utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
, which may be faster for large matrices. If ‘arpack’, use [`scipy.sparse.linalg.svds`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html#scipy.sparse.linalg.svds "(in SciPy v1.18.0)")
, which is more accurate, but possibly slower in some cases.

**n\_svd\_vecs**int, default=None

Number of vectors to use in calculating the SVD. Corresponds to `ncv` when `svd_method=arpack` and `n_oversamples` when `svd_method` is ‘randomized\`.

**mini\_batch**bool, default=False

Whether to use mini-batch k-means, which is faster but may get different results.

**init**{‘k-means++’, ‘random’}, or ndarray of shape (n\_clusters, n\_features), default=’k-means++’

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

The bicluster label of each row.

**column\_labels\_**array-like of shape (n\_cols,)

The bicluster label of each column.

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

[`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")

Partitions rows and columns under the assumption that the data has an underlying checkerboard structure.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#id1)\
\]

[Dhillon, Inderjit S, 2001. Co-clustering documents and words using bipartite spectral graph partitioning.](https://doi.org/10.1145/502512.502550)

Examples

\>>> from sklearn.cluster import SpectralCoclustering
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> clustering \= SpectralCoclustering(n\_clusters\=2, random\_state\=0).fit(X)
\>>> clustering.row\_labels\_
array(\[0, 1, 1, 0, 0, 0\], dtype=int32)
\>>> clustering.column\_labels\_
array(\[0, 0\], dtype=int32)
\>>> clustering
SpectralCoclustering(n\_clusters=2, random\_state=0)

Copy to clipboard

For a more detailed example, see the following: [A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html#sphx-glr-auto-examples-bicluster-plot-spectral-coclustering-py)
.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bicluster.py#L117)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.fit "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.get_indices "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_shape(_i_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L830)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.get_shape "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.get_submatrix "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_thumb.png)

[A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)

A demo of the Spectral Co-Clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)