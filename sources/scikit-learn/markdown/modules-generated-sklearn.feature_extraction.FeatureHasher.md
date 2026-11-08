[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.FeatureHasher.html)

Collapse Sidebar Expand Sidebar

FeatureHasher[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#featurehasher "Link to this heading")

=======================================================================================================================================================

class sklearn.feature\_extraction.FeatureHasher(_n\_features\=1048576_, _\*_, _input\_type\='dict'_, _dtype\=<class 'numpy.float64'>_, _alternate\_sign\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_hash.py#L21)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "Link to this definition")

Implements feature hashing, aka the hashing trick.

This class turns sequences of symbolic feature names (strings) into scipy.sparse matrices, using a hash function to compute the matrix column corresponding to a name. The hash function employed is the signed 32-bit version of Murmurhash3.

Feature names of type byte string are used as-is. Unicode strings are converted to UTF-8 first, but no Unicode normalization is done. Feature values must be (finite) numbers.

This class is a low-memory alternative to DictVectorizer and CountVectorizer, intended for large-scale (online) learning and situations where memory is tight, e.g. when running prediction code on embedded devices.

For an efficiency comparison of the different feature extractors, see [FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-hashing)
.

Added in version 0.13.

Parameters:

**n\_features**int, default=2\*\*20

The number of features (columns) in the output matrices. Small numbers of features are likely to cause hash collisions, but large numbers will cause larger coefficient dimensions in linear learners.

**input\_type**str, default=’dict’

Choose a string from {‘dict’, ‘pair’, ‘string’}. Either “dict” (the default) to accept dictionaries over (feature\_name, value); “pair” to accept pairs of (feature\_name, value); or “string” to accept single strings. feature\_name should be a string, while value should be a number. In the case of “string”, a value of 1 is implied. The feature\_name is hashed to find the appropriate column for the feature. The value’s sign might be flipped in the output (but see non\_negative, below).

**dtype**numpy dtype, default=np.float64

The type of feature values. Passed to scipy.sparse matrix constructors as the dtype argument. Do not set this to bool, np.boolean or any unsigned integer type.

**alternate\_sign**bool, default=True

When True, an alternating sign is added to the features as to approximately conserve the inner product in the hashed space even for small n\_features. This approach is similar to sparse random projection.

Changed in version 0.19: `alternate_sign` replaces the now deprecated `non_negative` parameter.

See also

[`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")

Vectorizes string-valued features using a hash table.

[`sklearn.preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Handles nominal/categorical features.

Notes

This estimator is [stateless](https://scikit-learn.org/stable/glossary.html#term-stateless)
 and does not need to be fitted. However, we recommend to call [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.fit_transform "sklearn.feature_extraction.FeatureHasher.fit_transform")
 instead of [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.transform "sklearn.feature_extraction.FeatureHasher.transform")
, as parameter validation is only performed in [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.fit "sklearn.feature_extraction.FeatureHasher.fit")
.

Examples

\>>> from sklearn.feature\_extraction import FeatureHasher
\>>> h \= FeatureHasher(n\_features\=10)
\>>> D \= \[{'dog': 1, 'cat':2, 'elephant':4},{'dog': 2, 'run': 5}\]
\>>> f \= h.transform(D)
\>>> f.toarray()
array(\[\[ 0.,  0., -4., -1.,  0.,  0.,  0.,  0.,  0.,  2.\],\
       \[ 0.,  0.,  0., -2., -5.,  0.,  0.,  0.,  0.,  0.\]\])

Copy to clipboard

With `input_type="string"`, the input must be an iterable over iterables of strings:

\>>> h \= FeatureHasher(n\_features\=8, input\_type\="string")
\>>> raw\_X \= \[\["dog", "cat", "snake"\], \["snake", "dog"\], \["cat", "bird"\]\]
\>>> f \= h.transform(raw\_X)
\>>> f.toarray()
array(\[\[ 0.,  0.,  0., -1.,  0., -1.,  0.,  1.\],\
       \[ 0.,  0.,  0., -1.,  0., -1.,  0.,  0.\],\
       \[ 0., -1.,  0.,  0.,  0.,  0.,  0.,  1.\]\])

Copy to clipboard

fit(_X\=None_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_hash.py#L131)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.fit "Link to this definition")

Only validates estimator’s parameters.

This method allows to: (i) validate the estimator’s parameters and (ii) be consistent with the scikit-learn transformer API.

Parameters:

**X**Ignored

Not used, present here for API consistency by convention.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

FeatureHasher class instance.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.fit_transform "Link to this definition")

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

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_raw\_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_hash.py#L153)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher.transform "Link to this definition")

Transform a sequence of instances to a scipy.sparse matrix.

Parameters:

**raw\_X**iterable over iterable over raw features, length = n\_samples

Samples. Each sample must be iterable an (e.g., a list or tuple) containing/generating feature names (and optionally values, see the input\_type constructor argument) which will be hashed. raw\_X need not support the len function, so it can be the result of a generator; n\_samples is determined on the fly.

Returns:

**X**sparse matrix of shape (n\_samples, n\_features)

Feature matrix, for use with estimators or further transformers.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)