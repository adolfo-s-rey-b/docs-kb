[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)

Collapse Sidebar Expand Sidebar

MultiLabelBinarizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#multilabelbinarizer "Link to this heading")

====================================================================================================================================================================

class sklearn.preprocessing.MultiLabelBinarizer(_\*_, _classes\=None_, _sparse\_output\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L802)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "Link to this definition")

Transform between iterable of iterables and a multilabel format.

Although a list of sets or tuples is a very intuitive format for multilabel data, it is unwieldy to process. This transformer converts between this intuitive format and the supported multilabel format: a (samples x classes) binary matrix indicating the presence of a class label.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing_targets.html#multilabelbinarizer)
.

Parameters:

**classes**array-like of shape (n\_classes,), default=None

Indicates an ordering for the class labels. All entries should be unique (cannot contain duplicate classes).

**sparse\_output**bool, default=False

Set to True if output binary array is desired in CSR sparse format.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

A copy of the `classes` parameter when provided. Otherwise it corresponds to the sorted set of classes found when fitting.

See also

[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Encode categorical features using a one-hot aka one-of-K scheme.

Examples

\>>> from sklearn.preprocessing import MultiLabelBinarizer
\>>> mlb \= MultiLabelBinarizer()
\>>> mlb.fit\_transform(\[(1, 2), (3,)\])
array(\[\[1, 1, 0\],\
       \[0, 0, 1\]\])
\>>> mlb.classes\_
array(\[1, 2, 3\])

Copy to clipboard

\>>> mlb.fit\_transform(\[{'sci-fi', 'thriller'}, {'comedy'}\])
array(\[\[0, 1, 1\],\
       \[1, 0, 0\]\])
\>>> list(mlb.classes\_)
\['comedy', 'sci-fi', 'thriller'\]

Copy to clipboard

A common mistake is to pass in a list, which leads to the following issue:

\>>> mlb \= MultiLabelBinarizer()
\>>> mlb.fit(\['sci-fi', 'thriller', 'comedy'\])
MultiLabelBinarizer()
\>>> mlb.classes\_
array(\['-', 'c', 'd', 'e', 'f', 'h', 'i', 'l', 'm', 'o', 'r', 's', 't',\
    'y'\], dtype=object)

Copy to clipboard

To correct this, the list of labels should be passed in as:

\>>> mlb \= MultiLabelBinarizer()
\>>> mlb.fit(\[\['sci-fi', 'thriller', 'comedy'\]\])
MultiLabelBinarizer()
\>>> mlb.classes\_
array(\['comedy', 'sci-fi', 'thriller'\], dtype=object)

Copy to clipboard

fit(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L876)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.fit "Link to this definition")

Fit the label sets binarizer, storing [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

Parameters:

**y**iterable of iterables

A set of labels (any orderable and hashable object) for each sample. If the `classes` parameter is set, `y` will not be iterated.

Returns:

**self**object

Fitted estimator.

fit\_transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L909)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.fit_transform "Link to this definition")

Fit the label sets binarizer and transform the given label sets.

Parameters:

**y**iterable of iterables

A set of labels (any orderable and hashable object) for each sample. If the `classes` parameter is set, `y` will not be iterated.

Returns:

**y\_indicator**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

A matrix such that `y_indicator[i, j] = 1` iff `classes_[j]` is in `y[i]`, and 0 otherwise. Sparse matrix will be of CSR format.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_yt_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L1027)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.inverse_transform "Link to this definition")

Transform the given indicator matrix into label sets.

Parameters:

**yt**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

A matrix containing only 1s and 0s.

Returns:

**y\_original**list of tuples

The set of labels for each sample such that `y[i]` consists of `classes_[j]` for each `yt[i, j] == 1`.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L953)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.transform "Link to this definition")

Transform the given label sets.

Parameters:

**y**iterable of iterables

A set of labels (any orderable and hashable object) for each sample. If the `classes` parameter is set, `y` will not be iterated.

Returns:

**y\_indicator**array or CSR matrix, shape (n\_samples, n\_classes)

A matrix such that `y_indicator[i, j] = 1` iff `classes_[j]` is in `y[i]`, and 0 otherwise.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)