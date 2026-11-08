[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.sequence\_categorical\_column\_with\_vocabulary\_list Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/sequence_feature_column.py#L269-L333)

A sequence of categorical terms where ids use an in-memory list. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.sequence_categorical_column_with_vocabulary_list`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list)

tf.feature_column.sequence_categorical_column_with_vocabulary_list(
        key, vocabulary_list, dtype=None, default_value=-1, num_oov_buckets=0
    )

Pass this to `embedding_column` or `indicator_column` to convert sequence categorical data into dense representation for input to sequence NN, such as RNN.

#### Example:

colors = sequence_categorical_column_with_vocabulary_list(
        key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
        num_oov_buckets=2)
    colors_embedding = embedding_column(colors, dimension=3)
    columns = [colors_embedding]
    
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
| `vocabulary_list` | An ordered iterable defining the vocabulary. Each feature is mapped to the index of its value (if present) in `vocabulary_list`. Must be castable to `dtype`. |
| `dtype` | The type of features. Only string and integer types are supported. If `None`, it will be inferred from `vocabulary_list`. |
| `default_value` | The integer ID value to return for out-of-vocabulary feature values, defaults to `-1`. This can not be specified with a positive `num_oov_buckets`. |
| `num_oov_buckets` | Non-negative integer, the number of out-of-vocabulary buckets. All out-of-vocabulary inputs will be assigned IDs in the range `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a hash of the input value. A positive `num_oov_buckets` can not be specified with `default_value`. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `SequenceCategoricalColumn`. |     |\
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