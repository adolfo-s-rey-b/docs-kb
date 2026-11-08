[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.sequence\_categorical\_column\_with\_vocabulary\_file Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/sequence_feature_column.py#L199-L266)

A sequence of categorical terms where ids use a vocabulary file. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.sequence_categorical_column_with_vocabulary_file`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file)

tf.feature_column.sequence_categorical_column_with_vocabulary_file(
        key,
        vocabulary_file,
        vocabulary_size=None,
        num_oov_buckets=0,
        default_value=None,
        dtype=tf.dtypes.string
    )

Pass this to `embedding_column` or `indicator_column` to convert sequence categorical data into dense representation for input to sequence NN, such as RNN.

#### Example:

states = sequence_categorical_column_with_vocabulary_file(
        key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
        num_oov_buckets=5)
    states_embedding = embedding_column(states, dimension=10)
    columns = [states_embedding]
    
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
| `vocabulary_file` | The vocabulary file name. |
| `vocabulary_size` | Number of the elements in the vocabulary. This must be no greater than length of `vocabulary_file`, if less than length, later values are ignored. If None, it is set to the length of `vocabulary_file`. |
| `num_oov_buckets` | Non-negative integer, the number of out-of-vocabulary buckets. All out-of-vocabulary inputs will be assigned IDs in the range `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of the input value. A positive `num_oov_buckets` can not be specified with `default_value`. |\
| `default_value` | The integer ID value to return for out-of-vocabulary feature values, defaults to `-1`. This can not be specified with a positive `num_oov_buckets`. |\
| `dtype` | The type of features. Only string and integer types are supported. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `SequenceCategoricalColumn`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | `vocabulary_file` is missing or cannot be opened. |\
| `ValueError` | `vocabulary_size` is missing or < 1. |\
| `ValueError` | `num_oov_buckets` is a negative integer. |\
| `ValueError` | `num_oov_buckets` and `default_value` are both specified. |\
| `ValueError` | `dtype` is neither string nor integer. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.