[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.feature\_column.input\_layer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/input_layer#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column.py#L145-L214)

Returns a dense `Tensor` as input layer based on given `feature_columns`. (deprecated)

tf.compat.v1.feature_column.input_layer(
        features,
        feature_columns,
        weight_collections=None,
        trainable=True,
        cols_to_vars=None,
        cols_to_output_tensors=None
    )

Generally a single example in training data is described with FeatureColumns. At the first layer of the model, this column oriented data should be converted to a single `Tensor`.

#### Example:

price = numeric_column('price')
    keywords_embedded = embedding_column(
        categorical_column_with_hash_bucket("keywords", 10K), dimensions=16)
    columns = [price, keywords_embedded, ...]
    features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
    dense_tensor = input_layer(features, columns)
    for units in [128, 64, 32]:
      dense_tensor = tf.compat.v1.layers.dense(dense_tensor, units, tf.nn.relu)
    prediction = tf.compat.v1.layers.dense(dense_tensor, 1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A mapping from key to tensors. `_FeatureColumn`s look up via these keys. For example `numeric_column('price')` will look at 'price' key in this dict. Values can be a `SparseTensor` or a `Tensor` depends on corresponding `_FeatureColumn`. |
| `feature_columns` | An iterable containing the FeatureColumns to use as inputs to your model. All items should be instances of classes derived from `_DenseColumn` such as `numeric_column`, `embedding_column`, `bucketized_column`, `indicator_column`. If you have categorical features, you can wrap them with an `embedding_column` or `indicator_column`. |
| `weight_collections` | A list of collection names to which the Variable will be added. Note that variables will also be added to collections `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`. |
| `trainable` | If `True` also add the variable to the graph collection `GraphKeys.TRAINABLE_VARIABLES` (see [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>). |
| `cols_to_vars` | If not `None`, must be a dictionary that will be filled with a mapping from `_FeatureColumn` to list of `Variable`s. For example, after the call, we might have cols\_to\_vars = {\_EmbeddingColumn( categorical\_column=\_HashedCategoricalColumn( key='sparse\_feature', hash\_bucket\_size=5, dtype=tf.string), dimension=10): \[ |\
| `cols_to_output_tensors` | If not `None`, must be a dictionary that will be filled with a mapping from '\_FeatureColumn' to the associated output `Tensor`s. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` which represents input layer of a model. Its shape is (batch\_size, first\_layer\_dimension) and its dtype is `float32`. first\_layer\_dimension is determined based on given `feature_columns`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if an item in `feature_columns` is not a `_DenseColumn`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.