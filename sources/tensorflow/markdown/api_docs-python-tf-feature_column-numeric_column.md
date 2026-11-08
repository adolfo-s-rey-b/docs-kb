[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ffeature_column%2Fnumeric_column&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.numeric\_column Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L817-L914)

Represents real valued or numerical features. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.numeric_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column)

tf.feature_column.numeric_column(
        key,
        shape=(1,),
        default_value=None,
        dtype=tf.dtypes.float32,
        normalizer_fn=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Migration examples: Canned Estimators](https://www.tensorflow.org/guide/migrate/canned_estimators)<br>    <br>*   [Migrate checkpoint saving](https://www.tensorflow.org/guide/migrate/checkpoint_saver)<br>    <br>*   [Migrate evaluation](https://www.tensorflow.org/guide/migrate/evaluator) | *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)<br>    <br>*   [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear)<br>    <br>*   [Premade Estimators](https://www.tensorflow.org/tutorials/estimator/premade)<br>    <br>*   [Getting started](https://www.tensorflow.org/decision_forests/tutorials/beginner_colab)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery) |

#### Example:

Assume we have data with two features `a` and `b`.

    data = {'a': [15, 9, 17, 19, 21, 18, 25, 30],

Let us represent the features `a` and `b` as numerical features.

    a = tf.feature_column.numeric_column('a')

Feature column describe a set of transformations to the inputs.

For example, to "bucketize" feature `a`, wrap the `a` column in a [`feature_column.bucketized_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column)
. Providing `5` bucket boundaries, the bucketized\_column api will bucket this feature in total of `6` buckets.

    a_buckets = tf.feature_column.bucketized_column(a,

Create a `DenseFeatures` layer which will apply the transformations described by the set of [`tf.feature_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column)
 objects:

    feature_layer = tf.keras.layers.DenseFeatures([a_buckets, b])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | A unique string identifying the input feature. It is used as the column name and the dictionary key for feature parsing configs, feature `Tensor` objects, and feature columns. |
| `shape` | An iterable of integers specifies the shape of the `Tensor`. An integer can be given which means a single dimension `Tensor` with given width. The `Tensor` representing the column will have the shape of \[batch\_size\] + `shape`. |
| `default_value` | A single value compatible with `dtype` or an iterable of values compatible with `dtype` which the column takes on during `tf.Example` parsing if data is missing. A default value of `None` will cause [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)<br> to fail if an example does not contain this column. If a single value is provided, the same value will be applied as the default value for every item. If an iterable of values is provided, the shape of the `default_value` should be equal to the given `shape`. |
| `dtype` | defines the type of values. Default value is [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. Must be a non-quantized, real integer or floating point type. |
| `normalizer_fn` | If not `None`, a function that can be used to normalize the value of the tensor after `default_value` is applied for parsing. Normalizer function takes the input `Tensor` as its argument, and returns the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that even though the most common use case of this function is normalization, it can be used for any kind of Tensorflow transformations. |

|     |
| --- |
| Returns<br>------- |     |
| A `NumericColumn`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if any dimension in shape is not an int |
| `ValueError` | if any dimension in shape is not a positive integer |
| `TypeError` | if `default_value` is an iterable but not compatible with `shape` |
| `TypeError` | if `default_value` is not compatible with `dtype`. |
| `ValueError` | if `dtype` is not convertible to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.