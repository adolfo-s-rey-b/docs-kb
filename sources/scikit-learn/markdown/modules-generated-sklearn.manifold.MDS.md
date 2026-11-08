[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.MDS.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.MDS.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.MDS.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.MDS.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.MDS.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.MDS.html)

Collapse Sidebar Expand Sidebar

MDS[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#mds "Link to this heading")

===============================================================================================================

class sklearn.manifold.MDS(_n\_components\=2_, _\*_, _metric\_mds\=True_, _n\_init\=1_, _init\='warn'_, _max\_iter\=300_, _verbose\=0_, _eps\=1e-06_, _n\_jobs\=None_, _random\_state\=None_, _dissimilarity\='deprecated'_, _metric\='euclidean'_, _metric\_params\=None_, _normalized\_stress\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_mds.py#L431)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "Link to this definition")

Multidimensional scaling.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling)
.

Parameters:

**n\_components**int, default=2

Number of dimensions in which to immerse the dissimilarities.

**metric\_mds**bool, default=True

If `True`, perform metric MDS; otherwise, perform nonmetric MDS. When `False` (i.e. non-metric MDS), dissimilarities with 0 are considered as missing values.

Changed in version 1.8: The parameter `metric` was renamed into `metric_mds`.

**n\_init**int, default=1

Number of times the SMACOF algorithm will be run with different initializations. The final results will be the best output of the runs, determined by the run with the smallest final stress.

Changed in version 1.9: The default value for `n_init` changed from 4 to 1.

**init**{‘random’, ‘classical\_mds’}, default=’random’

The initialization approach. If `random`, random initialization is used. If `classical_mds`, then classical MDS is run and used as initialization for MDS (in this case, the value of `n_init` is ignored).

Added in version 1.8.

Changed in version 1.10: The default value for `init` will change to `classical_mds`.

**max\_iter**int, default=300

Maximum number of iterations of the SMACOF algorithm for a single run.

**verbose**int, default=0

Level of verbosity.

**eps**float, default=1e-6

The tolerance with respect to stress (normalized by the sum of squared embedding distances) at which to declare convergence.

Changed in version 1.7: The default value for `eps` has changed from 1e-3 to 1e-6, as a result of a bugfix in the computation of the convergence criterion.

**n\_jobs**int, default=None

The number of jobs to use for the computation. If multiple initializations are used (`n_init`), each run of the algorithm is computed in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=None

Determines the random number generator used to initialize the centers. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**dissimilarity**{‘euclidean’, ‘precomputed’}

Dissimilarity measure to use:

*   ‘euclidean’:
    
    Pairwise Euclidean distances between points in the dataset.
    
*   ‘precomputed’:
    
    Pre-computed dissimilarities are passed directly to `fit` and `fit_transform`.
    

Deprecated since version 1.8: `dissimilarity` was renamed `metric` in 1.8 and will be removed in 1.10.

**metric**str or callable, default=’euclidean’

Metric to use for dissimilarity computation. Default is “euclidean”.

If metric is a string, it must be one of the options allowed by `scipy.spatial.distance.pdist` for its metric parameter, or a metric listed in [`sklearn.metrics.pairwise.distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")

If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

Changed in version 1.8: Prior to 1.8, `metric=True/False` was used to select metric/non-metric MDS, which is now the role of `metric_mds`. The support for `True` and `False` will be dropped in version 1.10, use `metric_mds` instead.

**metric\_params**dict, default=None

Additional keyword arguments for the dissimilarity computation.

Added in version 1.8.

**normalized\_stress**bool or “auto” default=”auto”

Whether to return normalized stress value (Stress-1) instead of raw stress. By default, metric MDS returns raw stress while non-metric MDS returns normalized stress.

Added in version 1.2.

Changed in version 1.4: The default value changed from `False` to `"auto"` in version 1.4.

Changed in version 1.7: Normalized stress is now supported for metric MDS as well.

Attributes:

**embedding\_**ndarray of shape (n\_samples, n\_components)

Stores the position of the dataset in the embedding space.

**stress\_**float

The final value of the stress (sum of squared distance of the disparities and the distances for all constrained points). If `normalized_stress=True`, returns Stress-1. A value of 0 indicates “perfect” fit, 0.025 excellent, 0.05 good, 0.1 fair, and 0.2 poor [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#r77760563872b-1)
.

**dissimilarity\_matrix\_**ndarray of shape (n\_samples, n\_samples)

Pairwise dissimilarities between the points. Symmetric matrix that:

*   either uses a custom dissimilarity matrix by setting `dissimilarity` to ‘precomputed’;
    
*   or constructs a dissimilarity matrix from data using Euclidean distances.
    

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

The number of iterations corresponding to the best stress.

See also

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis that is a linear dimensionality reduction method.

[`sklearn.decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Non-linear dimensionality reduction using kernels and PCA.

[`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")

T-distributed Stochastic Neighbor Embedding.

[`Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")

Manifold learning based on Isometric Mapping.

[`LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")

Manifold learning using Locally Linear Embedding.

[`SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")

Spectral embedding for non-linear dimensionality.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#id1)\
\]

“Nonmetric multidimensional scaling: a numerical method” Kruskal, J. Psychometrika, 29 (1964)

\[2\]

“Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis” Kruskal, J. Psychometrika, 29, (1964)

\[3\]

“Modern Multidimensional Scaling - Theory and Applications” Borg, I.; Groenen P. Springer Series in Statistics (1997)

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import MDS
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> embedding \= MDS(n\_components\=2, n\_init\=1, init\="random")
\>>> X\_transformed \= embedding.fit\_transform(X\[:100\])
\>>> X\_transformed.shape
(100, 2)

Copy to clipboard

For a more detailed example of usage, see [Multi-dimensional scaling](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html#sphx-glr-auto-examples-manifold-plot-mds-py)
.

For a comparison of manifold learning techniques, see [Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#sphx-glr-auto-examples-manifold-plot-compare-methods-py)
.

fit(_X_, _y\=None_, _init\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_mds.py#L681)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.fit "Link to this definition")

Compute the position of the points in the embedding space.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Input data. If `metric=='precomputed'`, the input should be the dissimilarity matrix.

**y**Ignored

Not used, present for API consistency by convention.

**init**ndarray of shape (n\_samples, n\_components), default=None

Starting configuration of the embedding to initialize the SMACOF algorithm. By default, the algorithm is initialized with a randomly chosen array.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _init\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_mds.py#L708)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.fit_transform "Link to this definition")

Fit the data from `X`, and returns the embedded coordinates.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Input data. If `metric=='precomputed'`, the input should be the dissimilarity matrix.

**y**Ignored

Not used, present for API consistency by convention.

**init**ndarray of shape (n\_samples, n\_components), default=None

Starting configuration of the embedding to initialize the SMACOF algorithm. By default, the algorithm is initialized with a randomly chosen array.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

X transformed in the new space.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_fit\_request(_\*_, _init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold._mds.MDS")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `init` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mds_thumb.png)

[Multi-dimensional scaling](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html)

Multi-dimensional scaling

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)