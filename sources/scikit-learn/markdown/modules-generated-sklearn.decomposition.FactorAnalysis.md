[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.FactorAnalysis.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.FactorAnalysis.html)

Collapse Sidebar Expand Sidebar

FactorAnalysis[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#factoranalysis "Link to this heading")

=====================================================================================================================================================

class sklearn.decomposition.FactorAnalysis(_n\_components\=None_, _\*_, _tol\=0.01_, _copy\=True_, _max\_iter\=1000_, _noise\_variance\_init\=None_, _svd\_method\='randomized'_, _iterated\_power\=3_, _rotation\=None_, _random\_state\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L39)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "Link to this definition")

Factor Analysis (FA).

A simple linear generative model with Gaussian latent variables.

The observations are assumed to be caused by a linear transformation of lower dimensional latent factors and added Gaussian noise. Without loss of generality the factors are distributed according to a Gaussian with zero mean and unit covariance. The noise is also zero mean and has an arbitrary diagonal covariance matrix.

If we would restrict the model further, by assuming that the Gaussian noise is even isotropic (all diagonal entries are the same) we would obtain [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
.

FactorAnalysis performs a maximum likelihood estimate of the so-called `loading` matrix, the transformation of the latent variables to the observed ones, using SVD based approach.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#fa)
.

Added in version 0.13.

Parameters:

**n\_components**int, default=None

Dimensionality of latent space, the number of components of `X` that are obtained after `transform`. If None, n\_components is set to the number of features.

**tol**float, default=1e-2

Stopping tolerance for log-likelihood increase.

**copy**bool, default=True

Whether to make a copy of X. If `False`, the input X gets overwritten during fitting.

**max\_iter**int, default=1000

Maximum number of iterations.

**noise\_variance\_init**array-like of shape (n\_features,), default=None

The initial guess of the noise variance for each feature. If None, it defaults to np.ones(n\_features).

**svd\_method**{‘lapack’, ‘randomized’}, default=’randomized’

Which SVD method to use. If ‘lapack’ use standard SVD from scipy.linalg, if ‘randomized’ use fast `randomized_svd` function. Defaults to ‘randomized’. For most applications ‘randomized’ will be sufficiently precise while providing significant speed gains. Accuracy can also be improved by setting higher values for `iterated_power`. If this is not sufficient, for maximum precision you should choose ‘lapack’.

**iterated\_power**int, default=3

Number of iterations for the power method. 3 by default. Only used if `svd_method` equals ‘randomized’.

**rotation**{‘varimax’, ‘quartimax’}, default=None

If not None, apply the indicated rotation. Currently, varimax and quartimax are implemented. See [“The varimax criterion for analytic rotation in factor analysis”](https://link.springer.com/article/10.1007%2FBF02289233)
 H. F. Kaiser, 1958.

Added in version 0.24.

**random\_state**int or RandomState instance, default=0

Only used when `svd_method` equals ‘randomized’. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Components with maximum variance.

**loglike\_**list of shape (n\_iterations,)

The log likelihood at each iteration.

**noise\_variance\_**ndarray of shape (n\_features,)

The estimated noise variance for each feature.

**n\_iter\_**int

Number of iterations run.

**mean\_**ndarray of shape (n\_features,)

Per-feature empirical mean, estimated from the training set.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis is also a latent linear variable model which however assumes equal noise variance for each feature. This extra assumption makes probabilistic PCA faster as it can be computed in closed form.

[`FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")

Independent component analysis, a latent variable model with non-Gaussian latent variables.

References

*   David Barber, Bayesian Reasoning and Machine Learning, Algorithm 21.1.
    
*   Christopher M. Bishop: Pattern Recognition and Machine Learning, Chapter 12.2.4.
    

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.decomposition import FactorAnalysis
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> transformer \= FactorAnalysis(n\_components\=7, random\_state\=0)
\>>> X\_transformed \= transformer.fit\_transform(X)
\>>> X\_transformed.shape
(1797, 7)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L202)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.fit "Link to this definition")

Fit the FactorAnalysis model to X using SVD based approach.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**Ignored

Ignored parameter.

Returns:

**self**object

FactorAnalysis class instance.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.fit_transform "Link to this definition")

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

get\_covariance()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.get_covariance "Link to this definition")

Compute data covariance with the FactorAnalysis model.

`cov = components_.T * components_ + diag(noise_variance)`

Returns:

**cov**ndarray of shape (n\_features, n\_features)

Estimated covariance of data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L357)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.get_precision "Link to this definition")

Compute data precision matrix with the FactorAnalysis model.

Returns:

**precision**ndarray of shape (n\_features, n\_features)

Estimated precision of data.

score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L407)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.score "Link to this definition")

Compute the average log-likelihood of the samples.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

The data.

**y**Ignored

Ignored parameter.

Returns:

**ll**float

Average log-likelihood of the samples under the current model.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L385)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.score_samples "Link to this definition")

Compute the log-likelihood of each sample.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

The data.

Returns:

**ll**ndarray of shape (n\_samples,)

Log-likelihood of each sample under the current model.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_factor_analysis.py#L311)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis.transform "Link to this definition")

Apply dimensionality reduction to X using the model.

Compute the expected mean of the latent variables. See Barber, 21.2.33 (or Bishop, 12.66).

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

The latent variables of X.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_thumb.png)

[Model selection with Probabilistic PCA and Factor Analysis (FA)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)

Model selection with Probabilistic PCA and Factor Analysis (FA)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_thumb.png)

[Factor Analysis (with rotation) to visualize patterns](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)

Factor Analysis (with rotation) to visualize patterns

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)