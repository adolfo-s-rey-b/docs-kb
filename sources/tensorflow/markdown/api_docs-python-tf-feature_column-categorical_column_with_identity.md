[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.categorical\_column\_with\_identity Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1441-L1516)

A `CategoricalColumn` that returns identity values. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.categorical_column_with_identity`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity)

tf.feature_column.categorical_column_with_identity(
        key, num_buckets, default_value=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [TFX Estimator Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components)<br>    <br>*   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census) |

Use this when your inputs are integers in the range `[0, num_buckets)`, and you want to use the input value itself as the categorical ID. Values outside this range will result in `default_value` if specified, otherwise it will fail.\
\
Typically, this is used for contiguous ranges of integer indexes, but it doesn't have to be. This might be inefficient, however, if many of IDs are unused. Consider `categorical_column_with_hash_bucket` in that case.\
\
For input dictionary `features`, `features[key]` is either `Tensor` or `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int and `''` for string, which will be dropped by this feature column.\
\
In the following examples, each input in the range `[0, 1000000)` is assigned the same value. All other inputs are assigned `default_value` 0. Note that a literal 0 in inputs will result in the same default ID.\
\
#### Linear model:\
\
import tensorflow as tf\
    video_id = tf.feature_column.categorical_column_with_identity(\
        key='video_id', num_buckets=1000000, default_value=0)\
    columns = [video_id]\
    features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],\
    [33,78, 2, 73, 1]])}\
    linear_prediction = tf.compat.v1.feature_column.linear_model(features,\
    columns)\
\
Embedding for a DNN model:\
\
import tensorflow as tf\
    video_id = tf.feature_column.categorical_column_with_identity(\
        key='video_id', num_buckets=1000000, default_value=0)\
    columns = [tf.feature_column.embedding_column(video_id, 9)]\
    features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],\
    [33,78, 2, 73, 1]])}\
    input_layer = tf.keras.layers.DenseFeatures(columns)\
    dense_tensor = input_layer(features)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `key` | A unique string identifying the input feature. It is used as the column name and the dictionary key for feature parsing configs, feature `Tensor` objects, and feature columns. |\
| `num_buckets` | Range of inputs and outputs is `[0, num_buckets)`. |\
| `default_value` | If set, values outside of range `[0, num_buckets)` will be replaced with this value. If not set, values >= num\_buckets will cause a failure while values < 0 will be dropped. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `CategoricalColumn` that returns identity values. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if `num_buckets` is less than one. |\
| `ValueError` | if `default_value` is not in range `[0, num_buckets)`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.