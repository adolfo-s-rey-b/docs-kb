[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?version=stable#functions_2)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.tpu.experimental.embedding Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tpu/experimental/embedding?version=stable#functions_2)
    

See Stable See Nightly

Public API for tf.\_api.v2.tpu.experimental.embedding namespace

Classes
-------

[`class Adagrad`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adagrad)
: Optimization parameters for Adagrad with TPU embeddings.

[`class AdagradMomentum`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum)
: Optimization parameters for Adagrad + Momentum with TPU embeddings.

[`class Adam`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/Adam)
: Optimization parameters for Adam with TPU embeddings.

[`class CustomCombiner`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner)
: Custom combiner for TPU embeddings.

[`class CustomOptimizer`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer)
: Optimization parameters for custom optimizer for TPU embeddings.

[`class FTRL`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FTRL)
: Optimization parameters for FTRL with TPU embeddings.

[`class FeatureConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/FeatureConfig)
: Configuration data for one embedding feature.

[`class QuantizationConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/QuantizationConfig)
: Settings for simulated quantization of the tpu embedding table.

[`class RowIdInitializer`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer)
: An initializer that initializes the table with vocabulary ids.

[`class SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)
: Optimization parameters for stochastic gradient descent for TPU embeddings.

[`class SparseCoreEmbeddingConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig)
: Config for sparsecore embedding.

[`class TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
: The TPUEmbedding mid level API.

[`class TPUEmbeddingForServing`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingForServing)
: The TPUEmbedding mid level API running on CPU for serving.

[`class TPUEmbeddingV0`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV0)
: The TPUEmbedding mid level API running on TPU without Embedding accelerator.

[`class TPUEmbeddingV2`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2)
: The TPUEmbedding mid level API running on TPU with sparse core accelerator.

[`class TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
: Configuration data for one embedding table.

Functions
---------

[`serving_embedding_lookup(...)`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup)
: Apply standard lookup ops with [`tf.tpu.experimental.embedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding)
 configs.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.