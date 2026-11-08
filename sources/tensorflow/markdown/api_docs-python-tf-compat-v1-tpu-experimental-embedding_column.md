[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tpu.experimental.embedding\_column Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding_column#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/feature_column_v2.py#L49-L202)

TPU version of [`tf.compat.v1.feature_column.embedding_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)
.

tf.compat.v1.tpu.experimental.embedding_column(
        categorical_column,
        dimension,
        combiner='mean',
        initializer=None,
        max_sequence_length=0,
        learning_rate_fn=None,
        embedding_lookup_device=None,
        tensor_core_shape=None,
        use_safe_embedding_lookup=True
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) |

Note that the interface for `tf.tpu.experimental.embedding_column` is different from that of [`tf.compat.v1.feature_column.embedding_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)
: The following arguments are NOT supported: `ckpt_to_load_from`, `tensor_name_in_ckpt`, `max_norm` and `trainable`.

Use this function in place of [`tf.compat.v1.feature_column.embedding_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)
 when you want to use the TPU to accelerate your embedding lookups via TPU embeddings.

column = tf.feature_column.categorical_column_with_identity(...)
    tpu_column = tf.tpu.experimental.embedding_column(column, 10)
    ...
    def model_fn(features):
      dense_feature = tf.keras.layers.DenseFeature(tpu_column)
      embedded_feature = dense_feature(features)
      ...
    
    estimator = tf.estimator.tpu.TPUEstimator(
        model_fn=model_fn,
        ...
        embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          column=[tpu_column],
          ...))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `categorical_column` | A categorical column returned from `categorical_column_with_identity`, `weighted_categorical_column`, `categorical_column_with_vocabulary_file`, `categorical_column_with_vocabulary_list`, `sequence_categorical_column_with_identity`, `sequence_categorical_column_with_vocabulary_file`, `sequence_categorical_column_with_vocabulary_list` |
| `dimension` | An integer specifying dimension of the embedding, must be > 0. |
| `combiner` | A string specifying how to reduce if there are multiple entries in a single row for a non-sequence column. For more information, see [`tf.feature_column.embedding_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)<br>. |
| `initializer` | A variable initializer function to be used in embedding variable initialization. If not specified, defaults to [`tf.compat.v1.truncated_normal_initializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/truncated_normal_initializer)<br> with mean `0.0` and standard deviation `1/sqrt(dimension)`. |
| `max_sequence_length` | An non-negative integer specifying the max sequence length. Any sequence shorter then this will be padded with 0 embeddings and any sequence longer will be truncated. This must be positive for sequence features and 0 for non-sequence features. |
| `learning_rate_fn` | A function that takes global step and returns learning rate for the embedding table. If you intend to use the same learning rate for multiple embedding tables, please ensure that you pass the exact same python function to all calls of embedding\_column, otherwise performence may suffer. |
| `embedding_lookup_device` | The device on which to run the embedding lookup. Valid options are "cpu", "tpu\_tensor\_core", and "tpu\_embedding\_core". If specifying "tpu\_tensor\_core", a tensor\_core\_shape must be supplied. If not specified, the default behavior is embedding lookup on "tpu\_embedding\_core" for training and "cpu" for inference. Valid options for training : \["tpu\_embedding\_core", "tpu\_tensor\_core"\] Valid options for serving : \["cpu", "tpu\_tensor\_core"\] For training, tpu\_embedding\_core is good for large embedding vocab (>1M), otherwise, tpu\_tensor\_core is often sufficient. For serving, doing embedding lookup on tpu\_tensor\_core during serving is a way to reduce host cpu usage in cases where that is a bottleneck. |
| `tensor_core_shape` | If supplied, a list of integers which specifies the intended dense shape to run embedding lookup for this feature on TensorCore. The batch dimension can be left None or -1 to indicate a dynamic shape. Only rank 2 shapes currently supported. |
| `use_safe_embedding_lookup` | If true, uses safe\_embedding\_lookup\_sparse instead of embedding\_lookup\_sparse. safe\_embedding\_lookup\_sparse ensures there are no empty rows and all weights and ids are positive at the expense of extra compute cost. This only applies to rank 2 (NxM) shaped input tensors. Defaults to true, consider turning off if the above checks are not needed. Note that having empty rows will not trigger any error though the output result might be 0 or omitted. |

|     |
| --- |
| Returns<br>------- |     |
| A `_TPUEmbeddingColumnV2`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `dimension` not > 0. |
| `ValueError` | if `initializer` is specified but not callable. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.