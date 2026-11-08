[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ffeature_column%2Fsequence_categorical_column_with_hash_bucket&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.sequence\_categorical\_column\_with\_hash\_bucket Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/sequence_feature_column.py#L152-L196)

A sequence of categorical terms where ids are set by hashing. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.sequence_categorical_column_with_hash_bucket`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket)

tf.feature_column.sequence_categorical_column_with_hash_bucket(
        key,
        hash_bucket_size,
        dtype=tf.dtypes.string
    )

Pass this to `embedding_column` or `indicator_column` to convert sequence categorical data into dense representation for input to sequence NN, such as RNN.

#### Example:

tokens = sequence_categorical_column_with_hash_bucket(
        'tokens', hash_bucket_size=1000)
    tokens_embedding = embedding_column(tokens, dimension=10)
    columns = [tokens_embedding]
    
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    sequence_feature_layer = SequenceFeatures(columns)
    sequence_input, sequence_length = sequence_feature_layer(features)
    sequence_length_mask = tf.sequence_mask(sequence_length)
    
    rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
    rnn_layer = tf.keras.layers.RNN(rnn_cell)
    outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key` | A unique string identifying the input feature. |
| `hash_bucket_size` | An int > 1. The number of buckets. |
| `dtype` | The type of features. Only string and integer types are supported. |

|     |
| --- |
| Returns<br>------- |     |
| A `SequenceCategoricalColumn`. |     |

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