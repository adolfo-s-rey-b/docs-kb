[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html)

Collapse Sidebar Expand Sidebar

MiniBatchSparsePCA[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#minibatchsparsepca "Link to this heading")

=================================================================================================================================================================

class sklearn.decomposition.MiniBatchSparsePCA(_n\_components\=None_, _\*_, _alpha\=1_, _ridge\_alpha\=0.01_, _max\_iter\=1000_, _callback\=None_, _batch\_size\=3_, _verbose\=False_, _shuffle\=True_, _n\_jobs\=None_, _method\='lars'_, _random\_state\=None_, _tol\=0.001_, _max\_no\_improvement\=10_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_sparse_pca.py#L342)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "Link to this definition")

Mini-batch Sparse Principal Components Analysis.

Finds the set of sparse components that can optimally reconstruct the data. The amount of sparseness is controllable by the coefficient of the L1 penalty, given by the parameter alpha.

For an example comparing sparse PCA to PCA, see [Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-auto-examples-decomposition-plot-faces-decomposition-py)

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#sparsepca)
.

Parameters:

**n\_components**int, default=None

Number of sparse atoms to extract. If None, then `n_components` is set to `n_features`.

**alpha**int, default=1

Sparsity controlling parameter. Higher values lead to sparser components.

**ridge\_alpha**float, default=0.01

Amount of ridge shrinkage to apply in order to improve conditioning when calling the transform method.

**max\_iter**int, default=1\_000

Maximum number of iterations over the complete dataset before stopping independently of any early stopping criterion heuristics.

Added in version 1.2.

**callback**callable, default=None

Callable that gets invoked every five iterations.

**batch\_size**int, default=3

The number of features to take in each mini batch.

**verbose**int or bool, default=False

Controls the verbosity; the higher, the more messages. Defaults to 0.

**shuffle**bool, default=True

Whether to shuffle the data before splitting it in batches.

**n\_jobs**int, default=None

Number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**method**{‘lars’, ‘cd’}, default=’lars’

Method to be used for optimization. lars: uses the least angle regression method to solve the lasso problem (linear\_model.lars\_path) cd: uses the coordinate descent method to compute the Lasso solution (linear\_model.Lasso). Lars will be faster if the estimated components are sparse.

**random\_state**int, RandomState instance or None, default=None

Used for random shuffling when `shuffle` is set to `True`, during online dictionary learning. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**tol**float, default=1e-3

Control early stopping based on the norm of the differences in the dictionary between 2 steps.

To disable early stopping based on changes in the dictionary, set `tol` to 0.0.

Added in version 1.1.

**max\_no\_improvement**int or None, default=10

Control early stopping based on the consecutive number of mini batches that does not yield an improvement on the smoothed cost function.

To disable convergence detection based on cost function, set `max_no_improvement` to `None`.

Added in version 1.1.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Sparse components extracted from the data.

**n\_components\_**int

Estimated number of components.

Added in version 0.23.

**n\_iter\_**int

Number of iterations run.

**mean\_**ndarray of shape (n\_features,)

Per-feature empirical mean, estimated from the training set. Equal to `X.mean(axis=0)`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")

Find a dictionary that sparsely encodes data.

[`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")

Incremental principal components analysis.

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis.

[`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")

Dimensionality reduction using truncated SVD.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.decomposition import MiniBatchSparsePCA
\>>> X, \_ \= make\_friedman1(n\_samples\=200, n\_features\=30, random\_state\=0)
\>>> transformer \= MiniBatchSparsePCA(n\_components\=5, batch\_size\=50,
...                                  max\_iter\=10, random\_state\=0)
\>>> transformer.fit(X)
MiniBatchSparsePCA(...)
\>>> X\_transformed \= transformer.transform(X)
\>>> X\_transformed.shape
(200, 5)
\>>> \# most values in the components\_ are zero (sparsity)
\>>> np.mean(transformer.components\_ \== 0)
np.float64(0.9)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_sparse_pca.py#L65)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.fit "Link to this definition")

Fit the model from data in X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_sparse_pca.py#L128)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.inverse_transform "Link to this definition")

Transform data from the latent space to the original space.

This inversion is an approximation due to the loss of information induced by the forward decomposition.

Added in version 1.2.

Parameters:

**X**ndarray of shape (n\_samples, n\_components)

Data in the latent space.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Reconstructed data in the original space.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_sparse_pca.py#L96)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA.transform "Link to this definition")

Least Squares projection of the data onto the sparse components.

To avoid instability issues in case the system is under-determined, regularization can be applied (Ridge regression) via the `ridge_alpha` parameter.

Note that Sparse PCA components orthogonality is not enforced as in PCA hence one cannot use a simple linear projection.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Test data to be transformed, must have the same number of features as the data used to train the model.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)