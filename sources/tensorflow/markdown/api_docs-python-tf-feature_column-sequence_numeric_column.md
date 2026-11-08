[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.sequence\_numeric\_column Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/sequence_feature_column.py#L336-L397)

Returns a feature column that represents sequences of numeric data. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.sequence_numeric_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column)

tf.feature_column.sequence_numeric_column(
        key,
        shape=(1,),
        default_value=0.0,
        dtype=tf.dtypes.float32,
        normalizer_fn=None
    )

#### Example:

temperature = sequence_numeric_column('temperature')
    columns = [temperature]
    
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
| `key` | A unique string identifying the input features. |
| `shape` | The shape of the input data per sequence id. E.g. if `shape=(2,)`, each example must contain `2 * sequence_length` values. |
| `default_value` | A single value compatible with `dtype` that is used for padding the sparse data into a dense `Tensor`. |
| `dtype` | The type of values. |
| `normalizer_fn` | If not `None`, a function that can be used to normalize the value of the tensor after `default_value` is applied for parsing. Normalizer function takes the input `Tensor` as its argument, and returns the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that even though the most common use case of this function is normalization, it can be used for any kind of Tensorflow transformations. |

|     |
| --- |
| Returns<br>------- |     |
| A `SequenceNumericColumn`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if any dimension in shape is not an int. |
| `ValueError` | if any dimension in shape is not a positive integer. |
| `ValueError` | if `dtype` is not convertible to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.