[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.categorical\_column\_with\_vocabulary\_list Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1322-L1438)

A `CategoricalColumn` with in-memory vocabulary. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.categorical_column_with_vocabulary_list`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list)

tf.feature_column.categorical_column_with_vocabulary_list(
        key, vocabulary_list, dtype=None, default_value=-1, num_oov_buckets=0
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator) | *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)<br>    <br>*   [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery) |

Use this when your inputs are in string or integer format, and you have an in-memory vocabulary mapping each value to an integer ID. By default, out-of-vocabulary values are ignored. Use either (but not both) of `num_oov_buckets` and `default_value` to specify how to include out-of-vocabulary values.

For input dictionary `features`, `features[key]` is either `Tensor` or `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int and `''` for string, which will be dropped by this feature column.

Example with `num_oov_buckets`: In the following example, each input in `vocabulary_list` is assigned an ID 0-3 corresponding to its index (e.g., input 'B' produces output 2). All other inputs are hashed and assigned an ID 4-5.

colors = categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
        num_oov_buckets=2)
    columns = [colors, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)

Example with `default_value`: In the following example, each input in `vocabulary_list` is assigned an ID 0-4 corresponding to its index (e.g., input 'B' produces output 3). All other inputs are assigned `default_value` 0.

colors = categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('X', 'R', 'G', 'B', 'Y'), default_value=0)
    columns = [colors, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)

And to make an embedding with either:

columns = [embedding_column(colors, 3),...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | A unique string identifying the input feature. It is used as the column name and the dictionary key for feature parsing configs, feature `Tensor` objects, and feature columns. |
| `vocabulary_list` | An ordered iterable defining the vocabulary. Each feature is mapped to the index of its value (if present) in `vocabulary_list`. Must be castable to `dtype`. |
| `dtype` | The type of features. Only string and integer types are supported. If `None`, it will be inferred from `vocabulary_list`. |
| `default_value` | The integer ID value to return for out-of-vocabulary feature values, defaults to `-1`. This can not be specified with a positive `num_oov_buckets`. |
| `num_oov_buckets` | Non-negative integer, the number of out-of-vocabulary buckets. All out-of-vocabulary inputs will be assigned IDs in the range `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a hash of the input value. A positive `num_oov_buckets` can not be specified with `default_value`. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `CategoricalColumn` with in-memory vocabulary. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if `vocabulary_list` is empty, or contains duplicate keys. |\
| `ValueError` | `num_oov_buckets` is a negative integer. |\
| `ValueError` | `num_oov_buckets` and `default_value` are both specified. |\
| `ValueError` | if `dtype` is not integer or string. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.