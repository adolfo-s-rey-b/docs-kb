[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.feature\_column.bucketized\_column Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L917-L1001)

Represents discretized dense input bucketed by `boundaries`. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.feature_column.bucketized_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column)

tf.feature_column.bucketized_column(
        source_column, boundaries
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns) | *   [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery) |

Buckets include the left boundary, and exclude the right boundary. Namely, `boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`.\
\
For example, if the inputs are\
\
boundaries = [0, 10, 100]\
    input tensor = [[-5, 10000]\
                    [150,   10]\
                    [5,    100]]\
\
then the output will be\
\
output = [[0, 3]\
              [3, 2]\
              [1, 3]]\
\
#### Example:\
\
price = tf.feature_column.numeric_column('price')\
    bucketized_price = tf.feature_column.bucketized_column(\
        price, boundaries=[...])\
    columns = [bucketized_price, ...]\
    features = tf.io.parse_example(\
        ..., features=tf.feature_column.make_parse_example_spec(columns))\
    dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)\
\
A `bucketized_column` can also be crossed with another categorical column using `crossed_column`:\
\
price = tf.feature_column.numeric_column('price')\
    # bucketized_column converts numerical feature to a categorical one.\
    bucketized_price = tf.feature_column.bucketized_column(\
        price, boundaries=[...])\
    # 'keywords' is a string feature.\
    price_x_keywords = tf.feature_column.crossed_column(\
        [bucketized_price, 'keywords'], 50K)\
    columns = [price_x_keywords, ...]\
    features = tf.io.parse_example(\
        ..., features=tf.feature_column.make_parse_example_spec(columns))\
    dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)\
    linear_model = tf.keras.experimental.LinearModel(units=...)(dense_tensor)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `source_column` | A one-dimensional dense column which is generated with `numeric_column`. |\
| `boundaries` | A sorted list or tuple of floats specifying the boundaries. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `BucketizedColumn`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `source_column` is not a numeric column, or if it is not one-dimensional. |\
| `ValueError` | If `boundaries` is not a sorted list or tuple. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.