[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_identity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.sequence\_categorical\_column\_with\_identity Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/sequence_feature_column.py#L102-L149)

Returns a feature column that represents sequences of integers. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.sequence_categorical_column_with_identity`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_identity)

tf.feature_column.sequence_categorical_column_with_identity(
        key, num_buckets, default_value=None
    )

Pass this to `embedding_column` or `indicator_column` to convert sequence categorical data into dense representation for input to sequence NN, such as RNN.

#### Example:

watches = sequence_categorical_column_with_identity(
        'watches', num_buckets=1000)
    watches_embedding = embedding_column(watches, dimension=10)
    columns = [watches_embedding]
    
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
| `num_buckets` | Range of inputs. Namely, inputs are expected to be in the range `[0, num_buckets)`. |\
| `default_value` | If `None`, this column's graph operations will fail for out-of-range inputs. Otherwise, this value must be in the range `[0, num_buckets)`, and will replace out-of-range inputs. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `SequenceCategoricalColumn`. |     |\
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