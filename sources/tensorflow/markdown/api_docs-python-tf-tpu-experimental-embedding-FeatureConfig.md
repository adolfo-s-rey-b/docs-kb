[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.FeatureConfig Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1537-L1652)

Configuration data for one embedding feature.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)

tf.tpu.experimental.embedding.FeatureConfig(
        table: tf.tpu.experimental.embedding.TableConfig,
        max_sequence_length: int = 0,
        validate_weights_and_indices: bool = True,
        output_shape: Optional[Union[List[int], tf.TensorShape]] = None,
        name: Optional[Text] = None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer) |

This class holds the configuration data for a single embedding feature. The main use is to assign features to [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
s via the table parameter:

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

You can also specify the output shape for each feature. The output shape should be the expected activation shape excluding the table dimension. For dense and sparse tensor, the output shape should be the same as the input shape excluding the last dimension. For ragged tensor, the output shape can mismatch the input shape.

When feeding features into `embedding.enqueue` they can be [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
s or [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s. When the argument `max_sequence_length` is 0, the default, you should expect a output of `embedding.dequeue` for this feature of shape `(batch_size, dim)`. If `max_sequence_length` is greater than 0, the feature is embedded as a sequence and padded up to the given length. The shape of the output for this feature will be `(batch_size, max_sequence_length, dim)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `table` | An instance of [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)<br>, describing the table in which this feature should be looked up. |
| `max_sequence_length` | If positive, the feature is a sequence feature with the corresponding maximum sequence length. If the sequence is longer than this, it will be truncated. If 0, the feature is not a sequence feature. |
| `validate_weights_and_indices` | If true, uses safe\_embedding\_lookup during serving which ensures there are no empty rows and all weights and ids are positive at the expense of extra compute cost. |
| `output_shape` | Optional argument to config the output shape of the feature activation. If provided, the feature feeding to the `embedding.enqueue` has to match the shape (for ragged tensor, the input shape and output shape can mismatch). If not provided, the shape can be either provided to the `embedding.build` or auto detected at the runtime. |
| `name` | An optional string used to name the table. Must be defined if running on SparseCore. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `table` is not an instance of [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)<br>. |
| `ValueError` | if `max_sequence_length` not an integer or is negative. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.