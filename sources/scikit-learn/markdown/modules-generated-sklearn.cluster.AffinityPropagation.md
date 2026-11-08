[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.AffinityPropagation.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.AffinityPropagation.html)

Collapse Sidebar Expand Sidebar

AffinityPropagation[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#affinitypropagation "Link to this heading")

==============================================================================================================================================================

class sklearn.cluster.AffinityPropagation(_\*_, _damping\=0.5_, _max\_iter\=200_, _convergence\_iter\=15_, _copy\=True_, _preference\=None_, _affinity\='euclidean'_, _verbose\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_affinity_propagation.py#L312)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "Link to this definition")

Perform Affinity Propagation Clustering of data.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation)
.

Parameters:

**damping**float, default=0.5

Damping factor in the range `[0.5, 1.0)` is the extent to which the current value is maintained relative to incoming values (weighted 1 - damping). This in order to avoid numerical oscillations when updating these values (messages).\
\
**max\_iter**int, default=200\
\
Maximum number of iterations.\
\
**convergence\_iter**int, default=15\
\
Number of iterations with no change in the number of estimated clusters that stops the convergence.\
\
**copy**bool, default=True\
\
Make a copy of input data.\
\
**preference**array-like of shape (n\_samples,) or float, default=None\
\
Preferences for each point - points with larger values of preferences are more likely to be chosen as exemplars. The number of exemplars, ie of clusters, is influenced by the input preferences value. If the preferences are not passed as arguments, they will be set to the median of the input similarities.\
\
**affinity**{‘euclidean’, ‘precomputed’}, default=’euclidean’\
\
Which affinity to use. At the moment ‘precomputed’ and `euclidean` are supported. ‘euclidean’ uses the negative squared euclidean distance between points.\
\
**verbose**bool, default=False\
\
Whether to be verbose.\
\
**random\_state**int, RandomState instance or None, default=None\
\
Pseudo-random number generator to control the starting state. Use an int for reproducible results across function calls. See the [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
.\
\
Added in version 0.23: this parameter was previously hardcoded as 0.\
\
Attributes:\
\
**cluster\_centers\_indices\_**ndarray of shape (n\_clusters,)\
\
Indices of cluster centers.\
\
**cluster\_centers\_**ndarray of shape (n\_clusters, n\_features)\
\
Cluster centers (if affinity != `precomputed`).\
\
**labels\_**ndarray of shape (n\_samples,)\
\
Labels of each point.\
\
**affinity\_matrix\_**ndarray of shape (n\_samples, n\_samples)\
\
Stores the affinity matrix used in `fit`.\
\
**n\_iter\_**int\
\
Number of iterations taken to converge.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
See also\
\
[`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")\
\
Recursively merges the pair of clusters that minimally increases a given linkage distance.\
\
[`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")\
\
Similar to AgglomerativeClustering, but recursively merges features instead of samples.\
\
[`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
\
K-Means clustering.\
\
[`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")\
\
Mini-Batch K-Means clustering.\
\
[`MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")\
\
Mean shift clustering using a flat kernel.\
\
[`SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")\
\
Apply clustering to a projection of the normalized Laplacian.\
\
Notes\
\
The algorithmic complexity of affinity propagation is quadratic in the number of points.\
\
When the algorithm does not converge, it will still return an array of `cluster_center_indices` and labels if there are any exemplars/clusters, however they may be degenerate and should be used with caution.\
\
When `fit` does not converge, `cluster_centers_` is still populated however it may be degenerate. In such a case, proceed with caution. If `fit` does not converge and fails to produce any `cluster_centers_` then `predict` will label every sample as `-1`.\
\
When all training samples have equal similarities and equal preferences, the assignment of cluster centers and labels depends on the preference. If the preference is smaller than the similarities, `fit` will result in a single cluster center and label `0` for every sample. Otherwise, every training sample becomes its own cluster center and is assigned a unique label.\
\
References\
\
Brendan J. Frey and Delbert Dueck, “Clustering by Passing Messages Between Data Points”, Science Feb. 2007\
\
Examples\
\
\>>> from sklearn.cluster import AffinityPropagation\
\>>> import numpy as np\
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[4, 2\], \[4, 4\], \[4, 0\]\])\
\>>> clustering \= AffinityPropagation(random\_state\=5).fit(X)\
\>>> clustering\
AffinityPropagation(random\_state=5)\
\>>> clustering.labels\_\
array(\[0, 0, 0, 1, 1, 1\])\
\>>> clustering.predict(\[\[0, 0\], \[4, 4\]\])\
array(\[0, 1\])\
\>>> clustering.cluster\_centers\_\
array(\[\[1, 2\],\
       \[4, 2\]\])\
\
Copy to clipboard\
\
For an example usage, see [Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-auto-examples-cluster-plot-affinity-propagation-py)\
.\
\
For a comparison of Affinity Propagation with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)\
\
fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_affinity_propagation.py#L492)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.fit "Link to this definition")\
\
Fit the clustering from features, or affinity matrix.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or array-like of shape (n\_samples, n\_samples)\
\
Training instances to cluster, or similarities / affinities between instances if `affinity='precomputed'`. If a sparse feature matrix is provided, it will be converted into a sparse `csr_matrix`.\
\
**y**Ignored\
\
Not used, present here for API consistency by convention.\
\
Returns:\
\
self\
\
Returns the instance itself.\
\
fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_affinity_propagation.py#L588)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.fit_predict "Link to this definition")\
\
Fit clustering from features/affinity matrix; return cluster labels.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or array-like of shape (n\_samples, n\_samples)\
\
Training instances to cluster, or similarities / affinities between instances if `affinity='precomputed'`. If a sparse feature matrix is provided, it will be converted into a sparse `csr_matrix`.\
\
**y**Ignored\
\
Not used, present here for API consistency by convention.\
\
Returns:\
\
**labels**ndarray of shape (n\_samples,)\
\
Cluster labels.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_affinity_propagation.py#L553)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.predict "Link to this definition")\
\
Predict the closest cluster each sample in X belongs to.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
New data to predict. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.\
\
Returns:\
\
**labels**ndarray of shape (n\_samples,)\
\
Cluster labels.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#gallery-examples "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)\
\
[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)\
\
Demo of affinity propagation clustering algorithm\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)\
\
[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)\
\
Comparing different clustering algorithms on toy datasets\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)