[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.crossed\_column Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L1642-L1773)

Returns a column for performing crosses of categorical features. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.crossed_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column)

tf.feature_column.crossed_column(
        keys, hash_bucket_size, hash_key=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)<br>    <br>*   [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear) |

Crossed features will be hashed according to `hash_bucket_size`. Conceptually, the transformation can be thought of as: Hash(cartesian product of features) % `hash_bucket_size`

For example, if the input features are:

*   SparseTensor referred by first key:
    
    shape = [2, 2]
        {
            [0, 0]: "a"
            [1, 0]: "b"
            [1, 1]: "c"
        }
    
*   SparseTensor referred by second key:
    
    shape = [2, 1]
        {
            [0, 0]: "d"
            [1, 0]: "e"
        }
    

then crossed feature will look like:

 shape = [2, 2]
    {
        [0, 0]: Hash64("d", Hash64("a")) % hash_bucket_size
        [1, 0]: Hash64("e", Hash64("b")) % hash_bucket_size
        [1, 1]: Hash64("e", Hash64("c")) % hash_bucket_size
    }

Here is an example to create a linear model with crosses of string features:

keywords_x_doc_terms = crossed_column(['keywords', 'doc_terms'], 50K)
    columns = [keywords_x_doc_terms, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)

You could also use vocabulary lookup before crossing:

keywords = categorical_column_with_vocabulary_file(
        'keywords', '/path/to/vocabulary/file', vocabulary_size=1K)
    keywords_x_doc_terms = crossed_column([keywords, 'doc_terms'], 50K)
    columns = [keywords_x_doc_terms, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)

If an input feature is of numeric type, you can use `categorical_column_with_identity`, or `bucketized_column`, as in the example:

# vertical_id is an integer categorical feature.
    vertical_id = categorical_column_with_identity('vertical_id', 10K)
    price = numeric_column('price')
    # bucketized_column converts numerical feature to a categorical one.
    bucketized_price = bucketized_column(price, boundaries=[...])
    vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
    columns = [vertical_id_x_price, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    linear_prediction = linear_model(features, columns)

To use crossed column in DNN model, you need to add it in an embedding column as in this example:

vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
    vertical_id_x_price_embedded = embedding_column(vertical_id_x_price, 10)
    dense_tensor = input_layer(features, [vertical_id_x_price_embedded, ...])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `keys` | An iterable identifying the features to be crossed. Each element can be either:<br><br>*   string: Will use the corresponding feature which must be of string type.<br>*   `CategoricalColumn`: Will use the transformed tensor produced by this column. Does not support hashed categorical column. |
| `hash_bucket_size` | An int > 1. The number of buckets. |
| `hash_key` | Specify the hash\_key that will be used by the `FingerprintCat64` function to combine the crosses fingerprints on SparseCrossOp (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `CrossedColumn`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `len(keys) < 2`. |
| `ValueError` | If any of the keys is neither a string nor `CategoricalColumn`. |
| `ValueError` | If any of the keys is `HashedCategoricalColumn`. |
| `ValueError` | If `hash_bucket_size < 1`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.