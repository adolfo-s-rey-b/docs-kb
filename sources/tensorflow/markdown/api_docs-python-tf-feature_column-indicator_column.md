[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.indicator\_column Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1519-L1561)

Represents multi-hot representation of given categorical column. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.indicator_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column)

tf.feature_column.indicator_column(
        categorical_column
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns) | *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)<br>    <br>*   [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery)<br>    <br>*   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census) |

*   For DNN model, `indicator_column` can be used to wrap any `categorical_column_*` (e.g., to feed to DNN). Consider to Use `embedding_column` if the number of buckets/unique(values) are large.
    
*   For Wide (aka linear) model, `indicator_column` is the internal representation for categorical column when passing categorical column directly (as any element in feature\_columns) to `linear_model`. See `linear_model` for details.
    

name = indicator_column(categorical_column_with_vocabulary_list(
        'name', ['bob', 'george', 'wanda']))
    columns = [name, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)
    
    dense_tensor == [[1, 0, 0]]  # If "name" bytes_list is ["bob"]
    dense_tensor == [[1, 0, 1]]  # If "name" bytes_list is ["bob", "wanda"]
    dense_tensor == [[2, 0, 0]]  # If "name" bytes_list is ["bob", "bob"]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `categorical_column` | A `CategoricalColumn` which is created by `categorical_column_with_*` or `crossed_column` functions. |

|     |
| --- |
| Returns<br>------- |     |
| An `IndicatorColumn`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `categorical_column` is not CategoricalColumn type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.