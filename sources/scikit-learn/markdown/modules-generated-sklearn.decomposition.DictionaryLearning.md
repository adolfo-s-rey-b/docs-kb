[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.DictionaryLearning.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.DictionaryLearning.html)

Collapse Sidebar Expand Sidebar

DictionaryLearning[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#dictionarylearning "Link to this heading")

=================================================================================================================================================================

class sklearn.decomposition.DictionaryLearning(_n\_components\=None_, _\*_, _alpha\=1_, _max\_iter\=1000_, _tol\=1e-08_, _fit\_algorithm\='lars'_, _transform\_algorithm\='omp'_, _transform\_n\_nonzero\_coefs\=None_, _transform\_alpha\=None_, _n\_jobs\=None_, _code\_init\=None_, _dict\_init\=None_, _callback\=None_, _verbose\=False_, _split\_sign\=False_, _random\_state\=None_, _positive\_code\=False_, _positive\_dict\=False_, _transform\_max\_iter\=1000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1417)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "Link to this definition")

Dictionary learning.

Finds a dictionary (a set of atoms) that performs well at sparsely encoding the fitted data.

Solves the optimization problem:

(U^\*,V^\*) \= argmin 0.5 || X \- U V ||\_Fro^2 + alpha \* || U ||\_1,1
            (U,V)
            with || V\_k ||\_2 <= 1 for all  0 <= k < n\_components

Copy to clipboard

||.||\_Fro stands for the Frobenius norm and ||.||\_1,1 stands for the entry-wise matrix norm which is the sum of the absolute values of all the entries in the matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#dictionarylearning)
.

Parameters:

**n\_components**int, default=None

Number of dictionary elements to extract. If None, then `n_components` is set to `n_features`.

**alpha**float, default=1.0

Sparsity controlling parameter.

**max\_iter**int, default=1000

Maximum number of iterations to perform.

**tol**float, default=1e-8

Tolerance for numerical error.

**fit\_algorithm**{‘lars’, ‘cd’}, default=’lars’

*   `'lars'`: uses the least angle regression method to solve the lasso problem ([`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
    );
    
*   `'cd'`: uses the coordinate descent method to compute the Lasso solution ([`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    ). Lars will be faster if the estimated components are sparse.
    

Added in version 0.17: _cd_ coordinate descent method to improve speed.

**transform\_algorithm**{‘lasso\_lars’, ‘lasso\_cd’, ‘lars’, ‘omp’, ‘threshold’}, default=’omp’

Algorithm used to transform the data:

*   `'lars'`: uses the least angle regression method ([`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
    );
    
*   `'lasso_lars'`: uses Lars to compute the Lasso solution.
    
*   `'lasso_cd'`: uses the coordinate descent method to compute the Lasso solution ([`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    ). `'lasso_lars'` will be faster if the estimated components are sparse.
    
*   `'omp'`: uses orthogonal matching pursuit to estimate the sparse solution.
    
*   `'threshold'`: squashes to zero all coefficients less than alpha from the projection `dictionary * X'`.
    

Added in version 0.17: _lasso\_cd_ coordinate descent method to improve speed.

**transform\_n\_nonzero\_coefs**int, default=None

Number of nonzero coefficients to target in each column of the solution. This is only used by `algorithm='lars'` and `algorithm='omp'`. If `None`, then `transform_n_nonzero_coefs=int(n_features / 10)`.

**transform\_alpha**float, default=None

If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the penalty applied to the L1 norm. If `algorithm='threshold'`, `alpha` is the absolute value of the threshold below which coefficients will be squashed to zero. If `None`, defaults to `alpha`.

Changed in version 1.2: When None, default value changed from 1.0 to `alpha`.

**n\_jobs**int or None, default=None

Number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**code\_init**ndarray of shape (n\_samples, n\_components), default=None

Initial value for the code, for warm restart. Only used if `code_init` and `dict_init` are not None.

**dict\_init**ndarray of shape (n\_components, n\_features), default=None

Initial values for the dictionary, for warm restart. Only used if `code_init` and `dict_init` are not None.

**callback**callable, default=None

Callable that gets invoked every five iterations.

Added in version 1.3.

**verbose**bool, default=False

To control the verbosity of the procedure.

**split\_sign**bool, default=False

Whether to split the sparse feature vector into the concatenation of its negative part and its positive part. This can improve the performance of downstream classifiers.

**random\_state**int, RandomState instance or None, default=None

Used for initializing the dictionary when `dict_init` is not specified, randomly shuffling the data when `shuffle` is set to `True`, and updating the dictionary. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**positive\_code**bool, default=False

Whether to enforce positivity when finding the code.

Added in version 0.20.

**positive\_dict**bool, default=False

Whether to enforce positivity when finding the dictionary.

Added in version 0.20.

**transform\_max\_iter**int, default=1000

Maximum number of iterations to perform if `algorithm='lasso_cd'` or `'lasso_lars'`.

Added in version 0.22.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

dictionary atoms extracted from the data

**error\_**array

vector of errors at each iteration

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

Number of iterations run.

See also

[`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")

A faster, less accurate, version of the dictionary learning algorithm.

[`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")

Mini-batch Sparse Principal Components Analysis.

[`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")

Find a sparse representation of data from a fixed, precomputed dictionary.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis.

References

J. Mairal, F. Bach, J. Ponce, G. Sapiro, 2009: Online dictionary learning for sparse coding ([https://www.di.ens.fr/~fbach/mairal\_icml09.pdf](https://www.di.ens.fr/~fbach/mairal_icml09.pdf)
)

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_sparse\_coded\_signal
\>>> from sklearn.decomposition import DictionaryLearning
\>>> X, dictionary, code \= make\_sparse\_coded\_signal(
...     n\_samples\=30, n\_components\=15, n\_features\=20, n\_nonzero\_coefs\=10,
...     random\_state\=42,
... )
\>>> dict\_learner \= DictionaryLearning(
...     n\_components\=15, transform\_algorithm\='lasso\_lars', transform\_alpha\=0.1,
...     random\_state\=42,
... )
\>>> X\_transformed \= dict\_learner.fit(X).transform(X)

Copy to clipboard

We can check the level of sparsity of `X_transformed`:

\>>> np.mean(X\_transformed \== 0)
np.float64(0.527)

Copy to clipboard

We can compare the average squared euclidean norm of the reconstruction error of the sparse coded signal relative to the squared euclidean norm of the original signal:

\>>> X\_hat \= X\_transformed @ dict\_learner.components\_
\>>> np.mean(np.sum((X\_hat \- X) \*\* 2, axis\=1) / np.sum(X \*\* 2, axis\=1))
np.float64(0.056)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1676)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.fit "Link to this definition")

Fit the model from data in X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1696)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.fit_transform "Link to this definition")

Fit the model from data in X and return the transformed data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**V**ndarray of shape (n\_samples, n\_components)

Transformed data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1164)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.inverse_transform "Link to this definition")

Transform data back to its original space.

Parameters:

**X**array-like of shape (n\_samples, n\_components)

Data to be transformed back. Must have the same number of components as the data used to train the model.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Transformed data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L1123)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning.transform "Link to this definition")

Encode the data as a sparse combination of the dictionary atoms.

Coding method is determined by the object parameter `transform_algorithm`.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Test data to be transformed, must have the same number of features as the data used to train the model.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Transformed data.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)