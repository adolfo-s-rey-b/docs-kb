[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.ClassicalMDS.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.ClassicalMDS.html)

Collapse Sidebar Expand Sidebar

ClassicalMDS[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#classicalmds "Link to this heading")

==========================================================================================================================================

class sklearn.manifold.ClassicalMDS(_n\_components\=2_, _\*_, _metric\='euclidean'_, _metric\_params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_classical_mds.py#L21)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "Link to this definition")

Classical multidimensional scaling (MDS).

This is also known as principal coordinates analysis (PCoA) or Torgerson’s scaling. It is a version of MDS that has exact solution in terms of eigendecomposition. If the input dissimilarity matrix consists of the pairwise Euclidean distances between some vectors, then classical MDS is equivalent to PCA applied to this set of vectors.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling)
.

Parameters:

**n\_components**int, default=2

Number of embedding dimensions.

**metric**str or callable, default=’euclidean’

Metric to use for dissimilarity computation. Default is “euclidean”.

If metric is a string, it must be one of the options allowed by `scipy.spatial.distance.pdist` for its metric parameter, or a metric listed in [`sklearn.metrics.pairwise.distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")

If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

**metric\_params**dict, default=None

Additional keyword arguments for the dissimilarity computation.

Attributes:

**embedding\_**ndarray of shape (n\_samples, n\_components)

Stores the position of the dataset in the embedding space.

**dissimilarity\_matrix\_**ndarray of shape (n\_samples, n\_samples)

Pairwise dissimilarities between the points.

**eigenvalues\_**ndarray of shape (n\_components,)

Eigenvalues of the double-centered dissimilarity matrix, corresponding to each of the selected components. They are equal to the squared 2-norms of the `n_components` variables in the embedding space.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

See also

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis.

[`MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")

Metric and non-metric MDS.

References

\[1\]

“Modern Multidimensional Scaling - Theory and Applications” Borg, I.; Groenen P. Springer Series in Statistics (1997)

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import ClassicalMDS
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> cmds \= ClassicalMDS(n\_components\=2)
\>>> X\_emb \= cmds.fit\_transform(X\[:100\])
\>>> X\_emb.shape
(100, 2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_classical_mds.py#L120)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS.fit "Link to this definition")

Compute the embedding positions.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Input data. If `metric=='precomputed'`, the input should be the dissimilarity matrix.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_classical_mds.py#L142)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS.fit_transform "Link to this definition")

Compute and return the embedding positions.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Input data. If `metric=='precomputed'`, the input should be the dissimilarity matrix.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

The embedding coordinates.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

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

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)