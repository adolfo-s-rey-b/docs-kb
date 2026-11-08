[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.LabelEncoder.html)

Collapse Sidebar Expand Sidebar

LabelEncoder[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#labelencoder "Link to this heading")

===============================================================================================================================================

class sklearn.preprocessing.LabelEncoder[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L40)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "Link to this definition")

Encode target labels with value between 0 and n\_classes-1.

This transformer should be used to encode target values, _i.e._ `y`, and not the input `X`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
.

Added in version 0.12.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

Holds the label for each class.

See also

[`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

Encode categorical features using an ordinal encoding scheme.

[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Encode categorical features as a one-hot numeric array.

Examples

`LabelEncoder` can be used to normalize labels.

\>>> from sklearn.preprocessing import LabelEncoder
\>>> le \= LabelEncoder()
\>>> le.fit(\[1, 2, 2, 6\])
LabelEncoder()
\>>> le.classes\_
array(\[1, 2, 6\])
\>>> le.transform(\[1, 1, 2, 6\])
array(\[0, 0, 1, 2\]...)
\>>> le.inverse\_transform(\[0, 0, 1, 2\])
array(\[1, 1, 2, 6\])

Copy to clipboard

It can also be used to transform non-numerical labels (as long as they are hashable and comparable) to numerical labels.

\>>> le \= LabelEncoder()
\>>> le.fit(\["paris", "paris", "tokyo", "amsterdam"\])
LabelEncoder()
\>>> list(le.classes\_)
\[np.str\_('amsterdam'), np.str\_('paris'), np.str\_('tokyo')\]
\>>> le.transform(\["tokyo", "tokyo", "paris"\])
array(\[2, 2, 1\]...)
\>>> list(le.inverse\_transform(\[2, 2, 1\]))
\[np.str\_('tokyo'), np.str\_('tokyo'), np.str\_('paris')\]

Copy to clipboard

fit(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L90)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit "Link to this definition")

Fit label encoder.

Parameters:

**y**array-like of shape (n\_samples,)

Target values.

Returns:

**self**returns an instance of self.

Fitted label encoder.

fit\_transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L107)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit_transform "Link to this definition")

Fit label encoder and return encoded labels.

Parameters:

**y**array-like of shape (n\_samples,)

Target values.

Returns:

**y**array-like of shape (n\_samples,)

Encoded labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L146)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.inverse_transform "Link to this definition")

Transform labels back to original encoding.

Parameters:

**y**array-like of shape (n\_samples,)

Target values.

Returns:

**y\_original**ndarray of shape (n\_samples,)

Original encoding.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L124)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.transform "Link to this definition")

Transform labels to normalized encoding.

Parameters:

**y**array-like of shape (n\_samples,)

Target values.

Returns:

**y**array-like of shape (n\_samples,)

Labels as normalized encodings.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)