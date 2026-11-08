[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.random_projection.SparseRandomProjection.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.random_projection.SparseRandomProjection.html)

Collapse Sidebar Expand Sidebar

SparseRandomProjection[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sparserandomprojection "Link to this heading")

=================================================================================================================================================================================

class sklearn.random\_projection.SparseRandomProjection(_n\_components\='auto'_, _\*_, _density\='auto'_, _eps\=0.1_, _dense\_output\=False_, _compute\_inverse\_components\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L616)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "Link to this definition")

Reduce dimensionality through sparse random projection.

Sparse random matrix is an alternative to dense random projection matrix that guarantees similar embedding quality while being much more memory efficient and allowing faster computation of the projected data.

If we note `s = 1 / density` the components of the random matrix are drawn from:

\-sqrt(s) / sqrt(n\_components)   with probability 1 / 2s
 0                              with probability 1 - 1 / s
+sqrt(s) / sqrt(n\_components)   with probability 1 / 2s

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/random_projection.html#sparse-random-matrix)
.

Added in version 0.13.

Parameters:

**n\_components**int or ‘auto’, default=’auto’

Dimensionality of the target projection space.

n\_components can be automatically adjusted according to the number of samples in the dataset and the bound given by the Johnson-Lindenstrauss lemma. In that case the quality of the embedding is controlled by the `eps` parameter.

It should be noted that Johnson-Lindenstrauss lemma can yield very conservative estimated of the required number of components as it makes no assumption on the structure of the dataset.

**density**float or ‘auto’, default=’auto’

Ratio in the range (0, 1\] of non-zero component in the random projection matrix.

If density = ‘auto’, the value is set to the minimum density as recommended by Ping Li et al.: 1 / sqrt(n\_features).

Use density = 1 / 3.0 if you want to reproduce the results from Achlioptas, 2001.

**eps**float, default=0.1

Parameter to control the quality of the embedding according to the Johnson-Lindenstrauss lemma when n\_components is set to ‘auto’. This value should be strictly positive.

Smaller values lead to better embedding and higher number of dimensions (n\_components) in the target projection space.

**dense\_output**bool, default=False

If True, ensure that the output of the random projection is a dense numpy array even if the input and random projection matrix are both sparse. In practice, if the number of components is small the number of zero components in the projected data will be very small and it will be more CPU and memory efficient to use a dense representation.

If False, the projected data uses a sparse representation if the input is sparse.

**compute\_inverse\_components**bool, default=False

Learn the inverse transform by computing the pseudo-inverse of the components during fit. Note that the pseudo-inverse is always a dense array, even if the training data was sparse. This means that it might be necessary to call `inverse_transform` on a small batch of samples at a time to avoid exhausting the available memory on the host. Moreover, computing the pseudo-inverse does not scale well to large matrices.

**random\_state**int, RandomState instance or None, default=None

Controls the pseudo random number generator used to generate the projection matrix at fit time. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**n\_components\_**int

Concrete number of components computed when n\_components=”auto”.

**components\_**sparse matrix of shape (n\_components, n\_features)

Random matrix used for the projection. Sparse matrix will be of CSR format.

**inverse\_components\_**ndarray of shape (n\_features, n\_components)

Pseudo-inverse of the components, only computed if `compute_inverse_components` is True.

Added in version 1.1.

**density\_**float in range 0.0 - 1.0

Concrete density computed from when density = “auto”.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")

Reduce dimensionality through Gaussian random projection.

References

\[1\]

Ping Li, T. Hastie and K. W. Church, 2006, “Very Sparse Random Projections”. [https://web.stanford.edu/~hastie/Papers/Ping/KDD06\_rp.pdf](https://web.stanford.edu/~hastie/Papers/Ping/KDD06_rp.pdf)

\[2\]

D. Achlioptas, 2001, “Database-friendly random projections”, [https://cgi.di.uoa.gr/~optas/papers/jl.pdf](https://cgi.di.uoa.gr/~optas/papers/jl.pdf)

Examples

\>>> import numpy as np
\>>> from sklearn.random\_projection import SparseRandomProjection
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.rand(25, 3000)
\>>> transformer \= SparseRandomProjection(random\_state\=rng)
\>>> X\_new \= transformer.fit\_transform(X)
\>>> X\_new.shape
(25, 2759)
\>>> \# very few components are non-zero
\>>> np.mean(transformer.components\_ != 0)
np.float64(0.0182)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L367)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.fit "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L435)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.inverse_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L802)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection.transform "Link to this definition")

Project the data by using matrix product with the random matrix.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The input data to project into a smaller dimensional space.

Returns:

**X\_new**{ndarray, sparse matrix} of shape (n\_samples, n\_components)

Projected array. It is a sparse matrix only when the input is sparse and `dense_output = False`.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)

[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

The Johnson-Lindenstrauss bound for embedding with random projections

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)