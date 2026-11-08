[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ffeature_column%2Fcategorical_column_with_hash_bucket&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.categorical\_column\_with\_hash\_bucket Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1004-L1073)

Represents sparse feature where ids are set by hashing. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.categorical_column_with_hash_bucket`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket)

tf.feature_column.categorical_column_with_hash_bucket(
        key,
        hash_bucket_size,
        dtype=tf.dtypes.string
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Estimators](https://www.tensorflow.org/guide/estimator) | *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns) |

Use this when your sparse features are in string or integer format, and you want to distribute your inputs into a finite number of buckets by hashing. output\_id = Hash(input\_feature\_string) % bucket\_size for string type input. For int type input, the value is converted to its string representation first and then hashed by the same formula.

For input dictionary `features`, `features[key]` is either `Tensor` or `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int and `''` for string, which will be dropped by this feature column.

#### Example:

import tensorflow as tf
    keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
    10000)
    columns = [keywords]
    features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',\
    'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',\
    'LSTM', 'Keras', 'RNN']])}
    linear_prediction, _, _ = tf.compat.v1.feature_column.linear_model(features,
    columns)
    
    # or
    import tensorflow as tf
    keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
    10000)
    keywords_embedded = tf.feature_column.embedding_column(keywords, 16)
    columns = [keywords_embedded]
    features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',\
    'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',\
    'LSTM', 'Keras', 'RNN']])}
    input_layer = tf.keras.layers.DenseFeatures(columns)
    dense_tensor = input_layer(features)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | A unique string identifying the input feature. It is used as the column name and the dictionary key for feature parsing configs, feature `Tensor` objects, and feature columns. |
| `hash_bucket_size` | An int > 1. The number of buckets. |
| `dtype` | The type of features. Only string and integer types are supported. |

|     |
| --- |
| Returns<br>------- |     |
| A `HashedCategoricalColumn`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | `hash_bucket_size` is not greater than 1. |
| `ValueError` | `dtype` is neither string nor integer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.