[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.LabelBinarizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.LabelBinarizer.html)

Collapse Sidebar Expand Sidebar

LabelBinarizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#labelbinarizer "Link to this heading")

=====================================================================================================================================================

class sklearn.preprocessing.LabelBinarizer(_\*_, _neg\_label\=0_, _pos\_label\=1_, _sparse\_output\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L184)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "Link to this definition")

Binarize labels in a one-vs-all fashion.

Several regression and binary classification algorithms are available in scikit-learn. A simple way to extend these algorithms to the multi-class classification case is to use the so-called one-vs-all scheme.

At learning time, this simply consists in learning one regressor or binary classifier per class. In doing so, one needs to convert multi-class labels to binary labels (belong or does not belong to the class). `LabelBinarizer` makes this process easy with the transform method.

At prediction time, one assigns the class for which the corresponding model gave the greatest confidence. `LabelBinarizer` makes this easy with the [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.inverse_transform "sklearn.preprocessing.LabelBinarizer.inverse_transform")
 method.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
.

Parameters:

**neg\_label**int, default=0

Value with which negative labels must be encoded.

**pos\_label**int, default=1

Value with which positive labels must be encoded.

**sparse\_output**bool, default=False

True if the returned array from transform is desired to be in sparse CSR format.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

Holds the label for each class.

**y\_type\_**str

Represents the type of the target data as evaluated by [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
. Possible type are ‘continuous’, ‘continuous-multioutput’, ‘binary’, ‘multiclass’, ‘multiclass-multioutput’, ‘multilabel-indicator’, and ‘unknown’.

**sparse\_input\_**bool

`True` if the input data to transform is given as a sparse matrix,

`False` otherwise.

See also

[`label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")

Function to perform the transform operation of LabelBinarizer with fixed classes.

[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Encode categorical features using a one-hot aka one-of-K scheme.

Examples

\>>> from sklearn.preprocessing import LabelBinarizer
\>>> lb \= LabelBinarizer()
\>>> lb.fit(\[1, 2, 6, 4, 2\])
LabelBinarizer()
\>>> lb.classes\_
array(\[1, 2, 4, 6\])
\>>> lb.transform(\[1, 6\])
array(\[\[1, 0, 0, 0\],\
       \[0, 0, 0, 1\]\])

Copy to clipboard

Binary targets transform to a column vector

\>>> lb \= LabelBinarizer()
\>>> lb.fit\_transform(\['yes', 'no', 'no', 'yes'\])
array(\[\[1\],\
       \[0\],\
       \[0\],\
       \[1\]\])

Copy to clipboard

Passing a 2D matrix for multilabel classification

\>>> import numpy as np
\>>> lb.fit(np.array(\[\[0, 1, 1\], \[1, 0, 0\]\]))
LabelBinarizer()
\>>> lb.classes\_
array(\[0, 1, 2\])
\>>> lb.transform(\[0, 1, 2, 1\])
array(\[\[1, 0, 0\],\
       \[0, 1, 0\],\
       \[0, 0, 1\],\
       \[0, 1, 0\]\])

Copy to clipboard

fit(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L284)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.fit "Link to this definition")

Fit label binarizer.

Parameters:

**y**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Target values. The 2-d matrix should only contain 0 and 1, represents multilabel classification.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L334)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.fit_transform "Link to this definition")

Fit label binarizer/transform multi-class labels to binary labels.

The output of transform is sometimes referred to as the 1-of-K coding scheme.

Parameters:

**y**{ndarray, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_classes)

Target values. The 2-d matrix should only contain 0 and 1, represents multilabel classification. Sparse matrix can be CSR, CSC, COO, DOK, or LIL.

Returns:

**Y**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

Shape will be (n\_samples, 1) for binary problems. Sparse matrix will be of CSR format.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_Y_, _threshold\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L399)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.inverse_transform "Link to this definition")

Transform binary labels back to multi-class labels.

Parameters:

**Y**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

Target values. All sparse matrices are converted to CSR before inverse transformation.

**threshold**float, default=None

Threshold used in the binary and multi-label cases.

Use 0 when `Y` contains the output of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 (classifier). Use 0.5 when `Y` contains the output of [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
.

If None, the threshold is assumed to be half way between neg\_label and pos\_label.

Returns:

**y\_original**{ndarray, sparse matrix} of shape (n\_samples,)

Target values. Sparse matrix will be of CSR format.

Notes

In the case when the binary labels are fractional (probabilistic), [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.inverse_transform "sklearn.preprocessing.LabelBinarizer.inverse_transform")
 chooses the class with the greatest value. Typically, this allows to use the output of a linear model’s [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 method directly as the input of [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.inverse_transform "sklearn.preprocessing.LabelBinarizer.inverse_transform")
.

set\_inverse\_transform\_request(_\*_, _threshold: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing._label.LabelBinarizer")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.set_inverse_transform_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `inverse_transform` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `inverse_transform` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `inverse_transform`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**threshold**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `threshold` parameter in `inverse_transform`.

Returns:

**self**object

The updated object.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L356)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer.transform "Link to this definition")

Transform multi-class labels to binary labels.

The output of transform is sometimes referred to by some authors as the 1-of-K coding scheme.

Parameters:

**y**{array, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_classes)

Target values. The 2-d matrix should only contain 0 and 1, represents multilabel classification. Sparse matrix can be CSR, CSC, COO, DOK, or LIL.

Returns:

**Y**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

Shape will be (n\_samples, 1) for binary problems. Sparse matrix will be of CSR format.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)