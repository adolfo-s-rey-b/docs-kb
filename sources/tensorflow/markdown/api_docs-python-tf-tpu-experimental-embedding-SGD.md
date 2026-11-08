[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.SGD Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L401-L514)

Optimization parameters for stochastic gradient descent for TPU embeddings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.SGD`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SGD)

tf.tpu.experimental.embedding.SGD(
        learning_rate: Union[float, Callable[[], float]] = 0.01,
        use_gradient_accumulation: bool = True,
        clip_weight_min: Optional[float] = None,
        clip_weight_max: Optional[float] = None,
        weight_decay_factor: Optional[float] = None,
        multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None,
        clipvalue: Optional[ClipValueType] = None,
        low_dimensional_packing_status: bool = False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer) |

Pass this to [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 via the `optimizer` argument to set the global optimizer and its parameters:

embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        ...
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))

This can also be used in a [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 as the optimizer parameter to set a table specific optimizer. This will override the optimizer and parameters for global embedding optimizer defined above:

table_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...,
        optimizer=tf.tpu.experimental.embedding.SGD(0.2))
    table_two = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...)
    
    feature_config = (
        tf.tpu.experimental.embedding.FeatureConfig(
            table=table_one),
        tf.tpu.experimental.embedding.FeatureConfig(
            table=table_two))
    
    embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config=feature_config,
        batch_size=...
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))

In the above example, the first feature will be looked up in a table that has a learning rate of 0.2 while the second feature will be looked up in a table that has a learning rate of 0.1.

See 'tensorflow/core/protobuf/tpu/optimization\_parameters.proto' for a complete description of these parameters and their impacts on the optimizer algorithm.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | The learning rate. It should be a floating point value or a callable taking no arguments for a dynamic learning rate. |
| `use_gradient_accumulation` | setting this to `False` makes embedding gradients calculation less accurate but faster. |
| `clip_weight_min` | the minimum value to clip by; None means -infinity. |
| `clip_weight_max` | the maximum value to clip by; None means +infinity. |
| `weight_decay_factor` | amount of weight decay to apply; None means that the weights are not decayed. Weights are decayed by multiplying the weight by this factor each step. |
| `multiply_weight_decay_factor_by_learning_rate` | if true, `weight_decay_factor` is multiplied by the current learning rate. |
| `clipvalue` | Controls clipping of the gradient. Set to either a single positive scalar value to get clipping or a tiple of scalar values (min, max) to set a separate maximum or minimum. If one of the two entries is None, then there will be no clipping that direction. Note if this is set, you may see a decrease in performance as gradient accumulation will be enabled (it is normally off for SGD as it has no affect on accuracy). See 'tensorflow/core/protobuf/tpu/optimization\_parameters.proto' for more information on gradient accumulation and its impact on tpu embeddings. |
| `low_dimensional_packing_status` | Status of the low-dimensional embedding packing optimization controls whether to optimize the packing of 1-dimensional, 2-dimensional, and 4-dimensional embedding tables in memory. |

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L122-L129)

__eq__(
        other: Any
    ) -> Union[Any, bool]

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.