[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.SparseCoder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.SparseCoder.html)

Collapse Sidebar Expand Sidebar

SparseCoder[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sparsecoder "Link to this heading")

============================================================================================================================================

class sklearn.decomposition.SparseCoder(_dictionary_, _\*_, _transform\_algorithm\='omp'_, _transform\_n\_nonzero\_coefs\=None_, _transform\_alpha\=None_, _split\_sign\=False_, _n\_jobs\=None_, _positive\_code\=False_, _transform\_max\_iter\=1000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1182)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "Link to this definition")

Sparse coding.

Finds a sparse representation of data against a fixed, precomputed dictionary.

Each row of the result is the solution to a sparse coding problem. The goal is to find a sparse array `code` such that:

X ~= code \* dictionary

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#sparsecoder)
.

Parameters:

**dictionary**ndarray of shape (n\_components, n\_features)

The dictionary atoms used for sparse coding. Lines are assumed to be normalized to unit norm.

**transform\_algorithm**{‘lasso\_lars’, ‘lasso\_cd’, ‘lars’, ‘omp’, ‘threshold’}, default=’omp’

Algorithm used to transform the data:

*   `'lars'`: uses the least angle regression method (`linear_model.lars_path`);
    
*   `'lasso_lars'`: uses Lars to compute the Lasso solution;
    
*   `'lasso_cd'`: uses the coordinate descent method to compute the Lasso solution (linear\_model.Lasso). `'lasso_lars'` will be faster if the estimated components are sparse;
    
*   `'omp'`: uses orthogonal matching pursuit to estimate the sparse solution;
    
*   `'threshold'`: squashes to zero all coefficients less than alpha from the projection `dictionary * X'`.
    

**transform\_n\_nonzero\_coefs**int, default=None

Number of nonzero coefficients to target in each column of the solution. This is only used by `algorithm='lars'` and `algorithm='omp'` and is overridden by `alpha` in the `omp` case. If `None`, then `transform_n_nonzero_coefs=int(n_features / 10)`.

**transform\_alpha**float, default=None

If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the penalty applied to the L1 norm. If `algorithm='threshold'`, `alpha` is the absolute value of the threshold below which coefficients will be squashed to zero. If `algorithm='omp'`, `alpha` is the tolerance parameter: the value of the reconstruction error targeted. In this case, it overrides `n_nonzero_coefs`. If `None`, default to 1.

**split\_sign**bool, default=False

Whether to split the sparse feature vector into the concatenation of its negative part and its positive part. This can improve the performance of downstream classifiers.

**n\_jobs**int, default=None

Number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**positive\_code**bool, default=False

Whether to enforce positivity when finding the code.

Added in version 0.20.

**transform\_max\_iter**int, default=1000

Maximum number of iterations to perform if `algorithm='lasso_cd'` or `lasso_lars`.

Added in version 0.22.

Attributes:

**n\_components\_**int

Number of atoms.

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

[`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")

A faster, less accurate, version of the dictionary learning algorithm.

[`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")

Mini-batch Sparse Principal Components Analysis.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis.

[`sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Sparse coding where each row of the result is the solution to a sparse coding problem.

Examples

\>>> import numpy as np
\>>> from sklearn.decomposition import SparseCoder
\>>> X \= np.array(\[\[\-1, \-1, \-1\], \[0, 0, 3\]\])
\>>> dictionary \= np.array(
...     \[\[0, 1, 0\],\
...      \[\-1, \-1, 2\],\
...      \[1, 1, 1\],\
...      \[0, 1, 1\],\
...      \[0, 2, 1\]\],
...    dtype\=np.float64
... )
\>>> coder \= SparseCoder(
...     dictionary\=dictionary, transform\_algorithm\='lasso\_lars',
...     transform\_alpha\=1e-10,
... )
\>>> coder.transform(X)
array(\[\[ 0.,  0., -1.,  0.,  0.\],\
       \[ 0.,  1.,  1.,  0.,  0.\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1338)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.fit "Link to this definition")

Only validate the parameters of the estimator.

This method allows to: (i) validate the parameters of the estimator and (ii) be consistent with the scikit-learn transformer API.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data. Only used for input validation.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1389)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.inverse_transform "Link to this definition")

Transform data back to its original space.

Parameters:

**X**array-like of shape (n\_samples, n\_components)

Data to be transformed back. Must have the same number of components as the data used to train the model.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Transformed data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1367)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder.transform "Link to this definition")

Encode the data as a sparse combination of the dictionary atoms.

Coding method is determined by the object parameter `transform_algorithm`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_coding_thumb.png)

[Sparse coding with a precomputed dictionary](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html)

Sparse coding with a precomputed dictionary

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)