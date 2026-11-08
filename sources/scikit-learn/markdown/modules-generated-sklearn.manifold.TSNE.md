[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.TSNE.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.TSNE.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.TSNE.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.TSNE.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.TSNE.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.TSNE.html)

Collapse Sidebar Expand Sidebar

TSNE[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#tsne "Link to this heading")

==================================================================================================================

class sklearn.manifold.TSNE(_n\_components\=2_, _\*_, _perplexity\=30.0_, _early\_exaggeration\=12.0_, _learning\_rate\='auto'_, _max\_iter\=1000_, _n\_iter\_without\_progress\=300_, _min\_grad\_norm\=1e-07_, _metric\='euclidean'_, _metric\_params\=None_, _init\='pca'_, _verbose\=0_, _random\_state\=None_, _method\='barnes\_hut'_, _angle\=0.5_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_t_sne.py#L557)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "Link to this definition")

T-distributed Stochastic Neighbor Embedding.

t-SNE \[1\] is a tool to visualize high-dimensional data. It converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.

It is highly recommended to use another dimensionality reduction method (e.g. PCA for dense data or TruncatedSVD for sparse data) to reduce the number of dimensions to a reasonable amount (e.g. 50) if the number of features is very high. This will suppress some noise and speed up the computation of pairwise distances between samples. For more tips see Laurens van der Maaten’s FAQ \[2\].

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#t-sne)
.

Parameters:

**n\_components**int, default=2

Dimension of the embedded space.

**perplexity**float, default=30.0

The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms. Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50. Different values can result in significantly different results. The perplexity must be less than the number of samples.

**early\_exaggeration**float, default=12.0

Controls how tight natural clusters in the original space are in the embedded space and how much space will be between them. For larger values, the space between natural clusters will be larger in the embedded space. Again, the choice of this parameter is not very critical. If the cost function increases during initial optimization, the early exaggeration factor or the learning rate might be too high.

**learning\_rate**float or “auto”, default=”auto”

The learning rate for t-SNE is usually in the range \[10.0, 1000.0\]. If the learning rate is too high, the data may look like a ‘ball’ with any point approximately equidistant from its nearest neighbours. If the learning rate is too low, most points may look compressed in a dense cloud with few outliers. If the cost function gets stuck in a bad local minimum increasing the learning rate may help. Note that many other t-SNE implementations (bhtsne, FIt-SNE, openTSNE, etc.) use a definition of learning\_rate that is 4 times smaller than ours. So our learning\_rate=200 corresponds to learning\_rate=800 in those other implementations. The ‘auto’ option sets the learning\_rate to `max(N / early_exaggeration / 4, 50)` where N is the sample size, following \[4\] and \[5\].

Changed in version 1.2: The default value changed to `"auto"`.

**max\_iter**int, default=1000

Maximum number of iterations for the optimization. Should be at least 250.

Changed in version 1.5: Parameter name changed from `n_iter` to `max_iter`.

**n\_iter\_without\_progress**int, default=300

Maximum number of iterations without progress before we abort the optimization, used after 250 initial iterations with early exaggeration. Note that progress is only checked every 50 iterations so this value is rounded to the next multiple of 50.

Added in version 0.17: parameter _n\_iter\_without\_progress_ to control stopping criteria.

**min\_grad\_norm**float, default=1e-7

If the gradient norm is below this threshold, the optimization will be stopped.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by scipy.spatial.distance.pdist for its metric parameter, or a metric listed in pairwise.PAIRWISE\_DISTANCE\_FUNCTIONS. If metric is “precomputed”, X is assumed to be a distance matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from X as input and return a value indicating the distance between them. The default is “euclidean” which is interpreted as squared euclidean distance.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

Added in version 1.1.

**init**{“random”, “pca”} or ndarray of shape (n\_samples, n\_components), default=”pca”

Initialization of embedding. PCA initialization cannot be used with precomputed distances and is usually more globally stable than random initialization.

Changed in version 1.2: The default value changed to `"pca"`.

**verbose**int, default=0

Verbosity level.

**random\_state**int, RandomState instance or None, default=None

Determines the random number generator. Pass an int for reproducible results across multiple function calls. Note that different initializations might result in different local minima of the cost function. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**method**{‘barnes\_hut’, ‘exact’}, default=’barnes\_hut’

By default the gradient calculation algorithm uses Barnes-Hut approximation running in O(NlogN) time. method=’exact’ will run on the slower, but exact, algorithm in O(N^2) time. The exact algorithm should be used when nearest-neighbor errors need to be better than 3%. However, the exact method cannot scale to millions of examples.

Added in version 0.17: Approximate optimization _method_ via the Barnes-Hut.

**angle**float, default=0.5

Only used if method=’barnes\_hut’ This is the trade-off between speed and accuracy for Barnes-Hut T-SNE. ‘angle’ is the angular size (referred to as theta in \[3\]) of a distant node as measured from a point. If this size is below ‘angle’ then it is used as a summary node of all points contained within it. This method is not very sensitive to changes in this parameter in the range of 0.2 - 0.8. Angle less than 0.2 has quickly increasing computation time and angle greater 0.8 has quickly increasing error.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. This parameter has no impact when `metric="precomputed"` or (`metric="euclidean"` and `method="exact"`). `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 0.22.

Attributes:

**embedding\_**array-like of shape (n\_samples, n\_components)

Stores the embedding vectors.

**kl\_divergence\_**float

Kullback-Leibler divergence after optimization.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**learning\_rate\_**float

Effective learning rate.

Added in version 1.2.

**n\_iter\_**int

Number of iterations run.

See also

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis that is a linear dimensionality reduction method.

[`sklearn.decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Non-linear dimensionality reduction using kernels and PCA.

[`MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")

Manifold learning using multidimensional scaling.

[`Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")

Manifold learning based on Isometric Mapping.

[`LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")

Manifold learning using Locally Linear Embedding.

[`SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")

Spectral embedding for non-linear dimensionality.

Notes

For an example of using [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 in combination with [`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
 see [Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html#sphx-glr-auto-examples-neighbors-approximate-nearest-neighbors-py)
.

References

\[1\] van der Maaten, L.J.P.; Hinton, G.E. Visualizing High-Dimensional Data

Using t-SNE. Journal of Machine Learning Research 9:2579-2605, 2008.

\[2\] van der Maaten, L.J.P. t-Distributed Stochastic Neighbor Embedding

[https://lvdmaaten.github.io/tsne/](https://lvdmaaten.github.io/tsne/)

\[3\] L.J.P. van der Maaten. Accelerating t-SNE using Tree-Based Algorithms.

Journal of Machine Learning Research 15(Oct):3221-3245, 2014. [https://lvdmaaten.github.io/publications/papers/JMLR\_2014.pdf](https://lvdmaaten.github.io/publications/papers/JMLR_2014.pdf)

\[4\] Belkina, A. C., Ciccolella, C. O., Anno, R., Halpert, R., Spidlen, J.,

& Snyder-Cappione, J. E. (2019). Automated optimized parameters for T-distributed stochastic neighbor embedding improve visualization and analysis of large datasets. Nature Communications, 10(1), 1-12.

\[5\] Kobak, D., & Berens, P. (2019). The art of using t-SNE for single-cell

transcriptomics. Nature Communications, 10(1), 1-14.

Examples

\>>> import numpy as np
\>>> from sklearn.manifold import TSNE
\>>> X \= np.array(\[\[0, 0, 0\], \[0, 1, 1\], \[1, 0, 1\], \[1, 1, 1\]\])
\>>> X\_embedded \= TSNE(n\_components\=2, learning\_rate\='auto',
...                   init\='random', perplexity\=3).fit\_transform(X)
\>>> X\_embedded.shape
(4, 2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_t_sne.py#L1137)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.fit "Link to this definition")

Fit X into an embedded space.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

If the metric is ‘precomputed’ X must be a square distance matrix. Otherwise it contains a sample per row. If the method is ‘exact’, X may be a sparse matrix of type ‘csr’, ‘csc’ or ‘coo’. If the method is ‘barnes\_hut’ and the metric is ‘precomputed’, X may be a precomputed sparse graph.

**y**None

Ignored.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_t_sne.py#L1107)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.fit_transform "Link to this definition")

Fit X into an embedded space and return that transformed output.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

If the metric is ‘precomputed’ X must be a square distance matrix. Otherwise it contains a sample per row. If the method is ‘exact’, X may be a sparse matrix of type ‘csr’, ‘csc’ or ‘coo’. If the method is ‘barnes\_hut’ and the metric is ‘precomputed’, X may be a precomputed sparse graph.

**y**None

Ignored.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Embedding of the training data in low-dimensional space.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_thumb.png)

[Swiss Roll And Swiss-Hole Reduction](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)

Swiss Roll And Swiss-Hole Reduction

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_t_sne_perplexity_thumb.png)

[t-SNE: The effect of various perplexity values on the shape](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html)

t-SNE: The effect of various perplexity values on the shape

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)