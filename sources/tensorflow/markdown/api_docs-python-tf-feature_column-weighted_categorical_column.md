[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.weighted\_categorical\_column Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1564-L1639)

Applies weight values to a `CategoricalColumn`. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.weighted_categorical_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column)

tf.feature_column.weighted_categorical_column(
        categorical_column,
        weight_feature_key,
        dtype=tf.dtypes.float32
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns) |

Use this when each of your sparse inputs has both an ID and a value. For example, if you're representing text documents as a collection of word frequencies, you can provide 2 parallel sparse input features ('terms' and 'frequencies' below).

#### Example:

Input `tf.Example` objects:

[\
      features {\
        feature {\
          key: "terms"\
          value {bytes_list {value: "very" value: "model"} }\
        }\
        feature {\
          key: "frequencies"\
          value {float_list {value: 0.3 value: 0.1} }\
        }\
      },\
      features {\
        feature {\
          key: "terms"\
          value {bytes_list {value: "when" value: "course" value: "human"} }\
        }\
        feature {\
          key: "frequencies"\
          value {float_list {value: 0.4 value: 0.1 value: 0.2} }\
        }\
      }\
    ]

categorical_column = categorical_column_with_hash_bucket(
        column_name='terms', hash_bucket_size=1000)
    weighted_column = weighted_categorical_column(
        categorical_column=categorical_column, weight_feature_key='frequencies')
    columns = [weighted_column, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction, _, _ = linear_model(features, columns)

This assumes the input dictionary contains a `SparseTensor` for key 'terms', and a `SparseTensor` for key 'frequencies'. These 2 tensors must have the same indices and dense shape.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `categorical_column` | A `CategoricalColumn` created by `categorical_column_with_*` functions. |
| `weight_feature_key` | String key for weight values. |
| `dtype` | Type of weights, such as [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. Only float and integer weights are supported. |

|     |
| --- |
| Returns<br>------- |     |
| A `CategoricalColumn` composed of two sparse features: one represents id, the other represents weight (value) of the id feature in that example. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `dtype` is not convertible to float. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.