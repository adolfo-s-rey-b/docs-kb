[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.random_projection.GaussianRandomProjection.html)

Collapse Sidebar Expand Sidebar

GaussianRandomProjection[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#gaussianrandomprojection "Link to this heading")

=======================================================================================================================================================================================

class sklearn.random\_projection.GaussianRandomProjection(_n\_components\='auto'_, _\*_, _eps\=0.1_, _compute\_inverse\_components\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L471)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "Link to this definition")

Reduce dimensionality through Gaussian random projection.

The components of the random matrix are drawn from N(0, 1 / n\_components).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/random_projection.html#gaussian-random-matrix)
.

Added in version 0.13.

Parameters:

**n\_components**int or ‘auto’, default=’auto’

Dimensionality of the target projection space.

n\_components can be automatically adjusted according to the number of samples in the dataset and the bound given by the Johnson-Lindenstrauss lemma. In that case the quality of the embedding is controlled by the `eps` parameter.

It should be noted that Johnson-Lindenstrauss lemma can yield very conservative estimated of the required number of components as it makes no assumption on the structure of the dataset.

**eps**float, default=0.1

Parameter to control the quality of the embedding according to the Johnson-Lindenstrauss lemma when `n_components` is set to ‘auto’. The value should be strictly positive.

Smaller values lead to better embedding and higher number of dimensions (n\_components) in the target projection space.

**compute\_inverse\_components**bool, default=False

Learn the inverse transform by computing the pseudo-inverse of the components during fit. Note that computing the pseudo-inverse does not scale well to large matrices.

**random\_state**int, RandomState instance or None, default=None

Controls the pseudo random number generator used to generate the projection matrix at fit time. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**n\_components\_**int

Concrete number of components computed when n\_components=”auto”.

**components\_**ndarray of shape (n\_components, n\_features)

Random matrix used for the projection.

**inverse\_components\_**ndarray of shape (n\_features, n\_components)

Pseudo-inverse of the components, only computed if `compute_inverse_components` is True.

Added in version 1.1.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")

Reduce dimensionality through sparse random projection.

Examples

\>>> import numpy as np
\>>> from sklearn.random\_projection import GaussianRandomProjection
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.rand(25, 3000)
\>>> transformer \= GaussianRandomProjection(random\_state\=rng)
\>>> X\_new \= transformer.fit\_transform(X)
\>>> X\_new.shape
(25, 2759)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L367)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.fit "Link to this definition")

Generate a sparse random projection matrix.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Training set: only the shape is used to find optimal random matrix dimensions based on the theory referenced in the afore mentioned papers.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

BaseRandomProjection class instance.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L435)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.inverse_transform "Link to this definition")

Project data back to its original space.

Returns an array X\_original whose transform would be X. Note that even if X is sparse, X\_original is dense: this may use a lot of RAM.

If `compute_inverse_components` is False, the inverse of the components is computed during each call to `inverse_transform` which can be costly.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_components)

Data to be transformed back.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Reconstructed data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L591)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection.transform "Link to this definition")

Project the data by using matrix product with the random matrix.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The input data to project into a smaller dimensional space.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Projected array.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)