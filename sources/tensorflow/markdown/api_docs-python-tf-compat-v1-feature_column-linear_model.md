[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.feature\_column.linear\_model Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/linear_model#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column.py#L280-L416)

Returns a linear prediction `Tensor` based on given `feature_columns`. (deprecated)

tf.compat.v1.feature_column.linear_model(
        features,
        feature_columns,
        units=1,
        sparse_combiner='sum',
        weight_collections=None,
        trainable=True,
        cols_to_vars=None
    )

This function generates a weighted sum based on output dimension `units`. Weighted sum refers to logits in classification problems. It refers to the prediction itself for linear regression problems.

Note on supported columns: `linear_model` treats categorical columns as `indicator_column`s. To be specific, assume the input as `SparseTensor` looks like:

  shape = [2, 2]
      {
          [0, 0]: "a"
          [1, 0]: "b"
          [1, 1]: "c"
      }

`linear_model` assigns weights for the presence of "a", "b", "c' implicitly, just like `indicator_column`, while `input_layer` explicitly requires wrapping each of categorical columns with an `embedding_column` or an `indicator_column`.

#### Example of usage:

price = numeric_column('price')
    price_buckets = bucketized_column(price, boundaries=[0., 10., 100., 1000.])
    keywords = categorical_column_with_hash_bucket("keywords", 10K)
    keywords_price = crossed_column('keywords', price_buckets, ...)
    columns = [price_buckets, keywords, keywords_price ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    prediction = linear_model(features, columns)

The `sparse_combiner` argument works as follows For example, for two features represented as the categorical columns:

  # Feature 1
    
      shape = [2, 2]
      {
          [0, 0]: "a"
          [0, 1]: "b"
          [1, 0]: "c"
      }
    
      # Feature 2
    
      shape = [2, 3]
      {
          [0, 0]: "d"
          [1, 0]: "e"
          [1, 1]: "f"
          [1, 2]: "f"
      }

with `sparse_combiner` as "mean", the linear model outputs consequently are:

  y_0 = 1.0 / 2.0 * ( w_a + w_b ) + w_d + b
      y_1 = w_c + 1.0 / 3.0 * ( w_e + 2.0 * w_f ) + b

where `y_i` is the output, `b` is the bias, and `w_x` is the weight assigned to the presence of `x` in the input features.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A mapping from key to tensors. `_FeatureColumn`s look up via these keys. For example `numeric_column('price')` will look at 'price' key in this dict. Values are `Tensor` or `SparseTensor` depending on corresponding `_FeatureColumn`. |
| `feature_columns` | An iterable containing the FeatureColumns to use as inputs to your model. All items should be instances of classes derived from `_FeatureColumn`s. |
| `units` | An integer, dimensionality of the output space. Default value is 1. |
| `sparse_combiner` | A string specifying how to reduce if a categorical column is multivalent. Except `numeric_column`, almost all columns passed to `linear_model` are considered as categorical columns. It combines each categorical column independently. Currently "mean", "sqrtn" and "sum" are supported, with "sum" the default for linear model. "sqrtn" often achieves good accuracy, in particular with bag-of-words columns.<br><br>*   "sum": do not normalize features in the column<br>*   "mean": do l1 normalization on features in the column<br>*   "sqrtn": do l2 normalization on features in the column |
| `weight_collections` | A list of collection names to which the Variable will be added. Note that, variables will also be added to collections `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`. |
| `trainable` | If `True` also add the variable to the graph collection `GraphKeys.TRAINABLE_VARIABLES` (see [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>). |
| `cols_to_vars` | If not `None`, must be a dictionary that will be filled with a mapping from `_FeatureColumn` to associated list of `Variable`s. For example, after the call, we might have cols\_to\_vars = { \_NumericColumn( key='numeric\_feature1', shape=(1,): \[\], 'bias': \[\], \_NumericColumn( key='numeric\_feature2', shape=(2,)): \[\]} If a column creates no variables, its value will be an empty list. Note that cols\_to\_vars will also contain a string key 'bias' that maps to a list of Variables. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` which represents predictions/logits of a linear model. Its shape is (batch\_size, units) and its dtype is `float32`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if an item in `feature_columns` is neither a `_DenseColumn` nor `_CategoricalColumn`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.