[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.DictVectorizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.DictVectorizer.html)

Collapse Sidebar Expand Sidebar

DictVectorizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#dictvectorizer "Link to this heading")

==========================================================================================================================================================

class sklearn.feature\_extraction.DictVectorizer(_\*_, _dtype\=<class 'numpy.float64'>_, _separator\='='_, _sparse\=True_, _sort\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L17)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "Link to this definition")

Transforms lists of feature-value mappings to vectors.

This transformer turns lists of mappings (dict-like objects) of feature names to feature values into Numpy arrays or scipy.sparse matrices for use with scikit-learn estimators.

When feature values are strings, this transformer will do a binary one-hot (aka one-of-K) coding: one boolean-valued feature is constructed for each of the possible string values that the feature can take on. For instance, a feature “f” that can take on the values “ham” and “spam” will become two features in the output, one signifying “f=ham”, the other “f=spam”.

If a feature value is a sequence or set of strings, this transformer will iterate over the values and will count the occurrences of each string value.

However, note that this transformer will only do a binary one-hot encoding when feature values are of type string. If categorical features are represented as numeric values such as int or iterables of strings, the DictVectorizer can be followed by [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 to complete binary one-hot encoding.

Features that do not occur in a sample (mapping) will have a zero value in the resulting array/matrix.

For an efficiency comparison of the different feature extractors, see [FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#dict-feature-extraction)
.

Parameters:

**dtype**dtype, default=np.float64

The type of feature values. Passed to Numpy array/scipy.sparse matrix constructors as the dtype argument.

**separator**str, default=”=”

Separator string used when constructing new features for one-hot coding.

**sparse**bool, default=True

Whether transform should produce scipy.sparse matrices.

**sort**bool, default=True

Whether `feature_names_` and `vocabulary_` should be sorted when fitting.

Attributes:

**vocabulary\_**dict

A dictionary mapping feature names to feature indices.

**feature\_names\_**list

A list of length n\_features containing the feature names (e.g., “f=ham” and “f=spam”).

See also

[`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")

Performs vectorization using only a hash function.

[`sklearn.preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

Handles nominal/categorical features encoded as columns of arbitrary data types.

Examples

\>>> from sklearn.feature\_extraction import DictVectorizer
\>>> v \= DictVectorizer(sparse\=False)
\>>> D \= \[{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}\]
\>>> X \= v.fit\_transform(D)
\>>> X
array(\[\[2., 0., 1.\],\
       \[0., 1., 3.\]\])
\>>> v.inverse\_transform(X) \== \[{'bar': 2.0, 'foo': 1.0},\
...                            {'baz': 1.0, 'foo': 3.0}\]
True
\>>> v.transform({'foo': 4, 'unseen\_feature': 3})
array(\[\[0., 0., 4.\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L141)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.fit "Link to this definition")

Learn a list of feature name -> indices mappings.

Parameters:

**X**Mapping or iterable over Mappings

Dict(s) or Mapping(s) from feature names (arbitrary Python objects) to feature values (strings or convertible to dtype).

Changed in version 0.24: Accepts multiple string values for one categorical feature.

**y**(ignored)

Ignored parameter.

Returns:

**self**object

DictVectorizer class instance.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L294)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.fit_transform "Link to this definition")

Learn a list of feature name -> indices mappings and transform X.

Like fit(X) followed by transform(X), but does not require materializing X in memory.

Parameters:

**X**Mapping or iterable over Mappings

Dict(s) or Mapping(s) from feature names (arbitrary Python objects) to feature values (strings or convertible to dtype).

Changed in version 0.24: Accepts multiple string values for one categorical feature.

**y**(ignored)

Ignored parameter.

Returns:

**Xa**{array, sparse matrix}

Feature vectors; always 2-d.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L383)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Not used, present here for API consistency by convention.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_, _dict\_type\=<class 'dict'>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L320)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.inverse_transform "Link to this definition")

Transform array or sparse matrix X back to feature mappings.

X must have been produced by this DictVectorizer’s transform or fit\_transform method; it may only have passed through transformers that preserve the number of features and their order.

In the case of one-hot/one-of-K coding, the constructed feature names and values are returned rather than the original ones.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Sample matrix.

**dict\_type**type, default=dict

Constructor for feature mappings. Must conform to the collections.Mapping API.

Returns:

**X\_original**list of dict\_type objects of shape (n\_samples,)

Feature mappings for the samples in X.

restrict(_support_, _indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L403)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.restrict "Link to this definition")

Restrict the features to those in support using feature selection.

This function modifies the estimator in-place.

Parameters:

**support**array-like

Boolean mask or list of indices (as returned by the get\_support member of feature selectors).

**indices**bool, default=False

Whether support is a list of indices.

Returns:

**self**object

DictVectorizer class instance.

Examples

\>>> from sklearn.feature\_extraction import DictVectorizer
\>>> from sklearn.feature\_selection import SelectKBest, chi2
\>>> v \= DictVectorizer()
\>>> D \= \[{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}\]
\>>> X \= v.fit\_transform(D)
\>>> support \= SelectKBest(chi2, k\=2).fit(X, \[0, 1\])
\>>> v.get\_feature\_names\_out()
array(\['bar', 'baz', 'foo'\], ...)
\>>> v.restrict(support.get\_support())
DictVectorizer()
\>>> v.get\_feature\_names\_out()
array(\['bar', 'foo'\], ...)

Copy to clipboard

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/_dict_vectorizer.py#L363)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.transform "Link to this definition")

Transform feature->value dicts to array or sparse matrix.

Named features not encountered during fit or fit\_transform will be silently ignored.

Parameters:

**X**Mapping or iterable over Mappings of shape (n\_samples,)

Dict(s) or Mapping(s) from feature names (arbitrary Python objects) to feature values (strings or convertible to dtype).

Returns:

**Xa**{array, sparse matrix}

Feature vectors; always 2-d.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

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