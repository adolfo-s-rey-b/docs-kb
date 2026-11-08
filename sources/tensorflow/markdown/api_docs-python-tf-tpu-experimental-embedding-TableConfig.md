[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.TableConfig Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1318-L1519)

Configuration data for one embedding table.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)

tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size: int,
        dim: int,
        initializer: Optional[Callable[[Any], None]] = None,
        optimizer: Optional[_Optimizer] = None,
        combiner: Union[Text, tf.tpu.experimental.embedding.CustomCombiner] = 'mean',
        name: Optional[Text] = None,
        quantization_config: tf.tpu.experimental.embedding.QuantizationConfig = None,
        layout: Optional[Any] = None,
        dtype: tf.dtypes.DType = tf.dtypes.float32
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer) |

This class holds the configuration data for a single embedding table. It is used as the `table` parameter of a [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)
. Multiple [`tf.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)
 objects can use the same [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 object. In this case a shared table will be created for those feature lookups.

table_config_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...)
    table_config_two = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...)
    feature_config = {
        'feature_one': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_one),
        'feature_two': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_one),
        'feature_three': tf.tpu.experimental.embedding.FeatureConfig(
            table=table_config_two)}
    embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config=feature_config,
        batch_size=...
        optimizer=tf.tpu.experimental.embedding.Adam(0.1))

The above configuration has 2 tables, and three features. The first two features will be looked up in the first table and the third feature will be looked up in the second table.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocabulary_size` | Size of the table's vocabulary (number of rows). |
| `dim` | The embedding dimension (width) of the table. |
| `initializer` | A callable initializer taking one parameter, the shape of the variable that will be initialized. Will be called once per task, to initialize that task's shard of the embedding table. If not specified, defaults to `truncated_normal_initializer` with mean `0.0` and standard deviation `1/sqrt(dim)`. |
| `optimizer` | An optional instance of an optimizer parameters class, instance of one of [`tf.tpu.experimental.embedding.SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)<br>, [`tf.tpu.experimental.embedding.Adagrad`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adagrad)<br> or [`tf.tpu.experimental.embedding.Adam`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adam)<br>. If set will override the global optimizer passed to [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)<br>. |
| `combiner` | A string or instance of a combiner class specifying how to reduce if there are multiple entries in a single row. Currently 'mean', 'sqrtn', 'sum', and custom combiners are supported, with 'mean' the default. 'sqrtn' often achieves good accuracy, in particular with bag-of-words columns. For more information, see [`tf.nn.embedding_lookup_sparse`](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup_sparse)<br>. |
| `name` | An optional string used to name the table. Must be defined if running on SparseCore. |
| `quantization_config` | The simulated quantization config. An instance of [`tf.tpu.experimental.embedding.QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig)<br>. See the class for more documentation. |
| `layout` | If the table already has its layout computed, you can pass it in here. Otherwise, we will compute it for you. Most users should leave this as None. |
| `dtype` | The data type of the embedding table. Currently only int32 or float32 is supported. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `vocabulary_size` is not a positive integer. |
| `ValueError` | if `dim` is not a positive integer. |
| `ValueError` | if `initializer` is specified and is not callable. |
| `ValueError` | if `combiner` is not supported. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.