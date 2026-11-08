[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.KernelDensity.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.KernelDensity.html)

Collapse Sidebar Expand Sidebar

KernelDensity[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#kerneldensity "Link to this heading")

==============================================================================================================================================

class sklearn.neighbors.KernelDensity(_\*_, _bandwidth\=1.0_, _algorithm\='auto'_, _kernel\='gaussian'_, _metric\='euclidean'_, _atol\=0_, _rtol\=0_, _breadth\_first\=True_, _leaf\_size\=40_, _metric\_params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_kde.py#L42)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "Link to this definition")

Kernel Density Estimation.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/density.html#kernel-density)
.

Parameters:

**bandwidth**float or {“scott”, “silverman”}, default=1.0

The bandwidth of the kernel. If bandwidth is a float, it defines the bandwidth of the kernel. If bandwidth is a string, one of the estimation methods is implemented.

**algorithm**{‘kd\_tree’, ‘ball\_tree’, ‘auto’}, default=’auto’

The tree algorithm to use.

**kernel**{‘gaussian’, ‘tophat’, ‘epanechnikov’, ‘exponential’, ‘linear’, ‘cosine’}, default=’gaussian’

The kernel to use.

**metric**str, default=’euclidean’

Metric to use for distance computation. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

Not all metrics are valid with all algorithms: refer to the documentation of [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 and [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
. Note that the normalization of the density output is correct only for the Euclidean distance metric.

**atol**float, default=0

The desired absolute tolerance of the result. A larger tolerance will generally lead to faster execution.

**rtol**float, default=0

The desired relative tolerance of the result. A larger tolerance will generally lead to faster execution.

**breadth\_first**bool, default=True

If true (default), use a breadth-first approach to the problem. Otherwise use a depth-first approach.

**leaf\_size**int, default=40

Specify the leaf size of the underlying tree. See [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 or [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
 for details.

**metric\_params**dict, default=None

Additional parameters to be passed to the tree for use with the metric. For more information, see the documentation of [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 or [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
.

Attributes:

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**tree\_**`BinaryTree` instance

The tree algorithm for fast generalized N-point problems.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

**bandwidth\_**float

Value of the bandwidth, given directly by the bandwidth parameter or estimated using the ‘scott’ or ‘silverman’ method.

Added in version 1.0.

See also

[`sklearn.neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")

K-dimensional tree for fast generalized N-point problems.

[`sklearn.neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")

Ball tree for fast generalized N-point problems.

Examples

Compute a gaussian kernel density estimate with a fixed bandwidth.

\>>> from sklearn.neighbors import KernelDensity
\>>> import numpy as np
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.random\_sample((100, 3))
\>>> kde \= KernelDensity(kernel\='gaussian', bandwidth\=0.5).fit(X)
\>>> log\_density \= kde.score\_samples(X\[:3\])
\>>> log\_density
array(\[-1.52955942, -1.51462041, -1.60244657\])

Copy to clipboard

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_kde.py#L194)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.fit "Link to this definition")

Fit the Kernel Density model on the data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

**y**None

Ignored. This parameter exists only for compatibility with [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

**sample\_weight**array-like of shape (n\_samples,), default=None

List of sample weights attached to the data X.

Added in version 0.20.

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

sample(_n\_samples\=1_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_kde.py#L312)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.sample "Link to this definition")

Generate random samples from the model.

Currently, this is implemented only for gaussian and tophat kernels.

Parameters:

**n\_samples**int, default=1

Number of samples to generate.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation used to generate random samples. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**array-like of shape (n\_samples, n\_features)

List of samples.

score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_kde.py#L290)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.score "Link to this definition")

Compute the total log-likelihood under the model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

**y**None

Ignored. This parameter exists only for compatibility with [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

Returns:

**logprob**float

Total log-likelihood of the data in X. This is normalized to be a probability density, so the value will be low for high-dimensional data.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_kde.py#L252)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.score_samples "Link to this definition")

Compute the log-likelihood of each sample under the model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

An array of points to query. Last dimension should match dimension of training data (n\_features).

Returns:

**density**ndarray of shape (n\_samples,)

Log-likelihood of each sample in `X`. These are normalized to be probability densities, so values will be low for high-dimensional data.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors._kde.KernelDensity")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.set_fit_request "Link to this definition")

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

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)

[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)

Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_thumb.png)

[Simple 1D Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)

Simple 1D Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_kde_thumb.png)

[Kernel Density Estimate of Species Distributions](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html)

Kernel Density Estimate of Species Distributions

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)