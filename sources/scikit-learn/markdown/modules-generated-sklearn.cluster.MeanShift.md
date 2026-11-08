[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.MeanShift.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.MeanShift.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.MeanShift.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.MeanShift.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.MeanShift.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.MeanShift.html)

Collapse Sidebar Expand Sidebar

MeanShift[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#meanshift "Link to this heading")

================================================================================================================================

class sklearn.cluster.MeanShift(_\*_, _bandwidth\=None_, _seeds\=None_, _bin\_seeding\=False_, _min\_bin\_freq\=1_, _cluster\_all\=True_, _n\_jobs\=None_, _max\_iter\=300_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_mean_shift.py#L300)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "Link to this definition")

Mean shift clustering using a flat kernel.

Mean shift clustering aims to discover “blobs” in a smooth density of samples. It is a centroid-based algorithm, which works by updating candidates for centroids to be the mean of the points within a given region. These candidates are then filtered in a post-processing stage to eliminate near-duplicates to form the final set of centroids.

Seeding is performed using a binning technique for scalability.

For an example of how to use MeanShift clustering, refer to: [A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#sphx-glr-auto-examples-cluster-plot-mean-shift-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mean-shift)
.

Parameters:

**bandwidth**float, default=None

Bandwidth used in the flat kernel.

If not given, the bandwidth is estimated using sklearn.cluster.estimate\_bandwidth; see the documentation for that function for hints on scalability (see also the Notes, below).

**seeds**array-like of shape (n\_samples, n\_features), default=None

Seeds used to initialize kernels. If not set, the seeds are calculated by clustering.get\_bin\_seeds with bandwidth as the grid size and default values for other parameters.

**bin\_seeding**bool, default=False

If true, initial kernel locations are not locations of all points, but rather the location of the discretized version of points, where points are binned onto a grid whose coarseness corresponds to the bandwidth. Setting this option to True will speed up the algorithm because fewer seeds will be initialized. The default value is False. Ignored if seeds argument is not None.

**min\_bin\_freq**int, default=1

To speed up the algorithm, accept only those bins with at least min\_bin\_freq points as seeds.

**cluster\_all**bool, default=True

If true, then all points are clustered, even those orphans that are not within any kernel. Orphans are assigned to the nearest kernel. If false, then orphans are given cluster label -1.

**n\_jobs**int, default=None

The number of jobs to use for the computation. The following tasks benefit from the parallelization:

*   The search of nearest neighbors for bandwidth estimation and label assignments. See the details in the docstring of the `NearestNeighbors` class.
    
*   Hill-climbing optimization for all seeds.
    

See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**max\_iter**int, default=300

Maximum number of iterations, per seed point before the clustering operation terminates (for that seed point), if has not converged yet.

Added in version 0.22.

Attributes:

**cluster\_centers\_**ndarray of shape (n\_clusters, n\_features)

Coordinates of cluster centers.

**labels\_**ndarray of shape (n\_samples,)

Labels of each point.

**n\_iter\_**int

Maximum number of iterations performed on each seed.

Added in version 0.22.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

K-Means clustering.

Notes

Scalability:

Because this implementation uses a flat kernel and a Ball Tree to look up members of each kernel, the complexity will tend towards O(T\*n\*log(n)) in lower dimensions, with n the number of samples and T the number of points. In higher dimensions the complexity will tend towards O(T\*n^2).

Scalability can be boosted by using fewer seeds, for example by using a higher value of min\_bin\_freq in the get\_bin\_seeds function.

Note that the estimate\_bandwidth function is much less scalable than the mean shift algorithm and will be the bottleneck if it is used.

References

Dorin Comaniciu and Peter Meer, “Mean Shift: A robust approach toward feature space analysis”. IEEE Transactions on Pattern Analysis and Machine Intelligence. 2002. pp. 603-619.

Examples

\>>> from sklearn.cluster import MeanShift
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> clustering \= MeanShift(bandwidth\=2).fit(X)
\>>> clustering.labels\_
array(\[1, 1, 1, 0, 0, 0\])
\>>> clustering.predict(\[\[0, 0\], \[5, 5\]\])
array(\[1, 0\])
\>>> clustering
MeanShift(bandwidth=2)

Copy to clipboard

For a comparison of Mean Shift clustering with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_mean_shift.py#L469)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.fit "Link to this definition")

Perform clustering.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Samples to cluster.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Fitted instance.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L745)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.fit_predict "Link to this definition")

Perform clustering on `X` and returns cluster labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**labels**ndarray of shape (n\_samples,), dtype=np.int64

Cluster labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_mean_shift.py#L563)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.predict "Link to this definition")

Predict the closest cluster each sample in X belongs to.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

New data to predict.

Returns:

**labels**ndarray of shape (n\_samples,)

Index of the cluster each sample belongs to.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)