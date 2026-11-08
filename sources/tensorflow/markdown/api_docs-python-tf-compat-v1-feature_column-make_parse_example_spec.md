[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.feature\_column.make\_parse\_example\_spec Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/make_parse_example_spec#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column.py#L671-L730)

Creates parsing spec dictionary from input feature\_columns. (deprecated)

tf.compat.v1.feature_column.make_parse_example_spec(
        feature_columns
    )

The returned dictionary can be used as arg 'features' in [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
.

#### Typical usage example:

# Define features and transformations
    feature_a = categorical_column_with_vocabulary_file(...)
    feature_b = numeric_column(...)
    feature_c_bucketized = bucketized_column(numeric_column("feature_c"), ...)
    feature_a_x_feature_c = crossed_column(
        columns=["feature_a", feature_c_bucketized], ...)
    
    feature_columns = set(
        [feature_b, feature_c_bucketized, feature_a_x_feature_c])
    features = tf.io.parse_example(
        serialized=serialized_examples,
        features=make_parse_example_spec(feature_columns))

For the above example, make\_parse\_example\_spec would return the dict:

{
        "feature_a": parsing_ops.VarLenFeature(tf.string),
        "feature_b": parsing_ops.FixedLenFeature([1], dtype=tf.float32),
        "feature_c": parsing_ops.FixedLenFeature([1], dtype=tf.float32)
    }

|     |     |
| --- | --- |
| Args<br>---- |     |
| `feature_columns` | An iterable containing all feature columns. All items should be instances of classes derived from `_FeatureColumn`. |

|     |
| --- |
| Returns<br>------- |     |
| A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature` value. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If any of the given `feature_columns` is not a `_FeatureColumn` instance. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.