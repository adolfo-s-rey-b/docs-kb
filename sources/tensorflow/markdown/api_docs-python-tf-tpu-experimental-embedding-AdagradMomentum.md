[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2FAdagradMomentum&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.tpu.experimental.embedding.AdagradMomentum Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L646-L790)

Optimization parameters for Adagrad + Momentum with TPU embeddings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.AdagradMomentum`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/AdagradMomentum)

tf.tpu.experimental.embedding.AdagradMomentum(
        learning_rate: Union[float, Callable[[], float]] = 0.001,
        momentum: float = 0.0,
        use_nesterov: bool = False,
        exponent: float = 2,
        beta2: float = 1,
        epsilon: float = 1e-10,
        use_gradient_accumulation: bool = True,
        clip_weight_min: Optional[float] = None,
        clip_weight_max: Optional[float] = None,
        weight_decay_factor: Optional[float] = None,
        multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None,
        slot_variable_creation_fn: Optional[SlotVarCreationFnType] = None,
        clipvalue: Optional[ClipValueType] = None,
        low_dimensional_packing_status: bool = False
    )

Pass this to [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 via the `optimizer` argument to set the global optimizer and its parameters:

embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        ...
        optimizer=tf.tpu.experimental.embedding.AdagradMomentum(0.1))

This can also be used in a [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 as the optimizer parameter to set a table specific optimizer. This will override the optimizer and parameters for global embedding optimizer defined above:

table_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...,
        optimizer=tf.tpu.experimental.embedding.AdagradMomentum(0.2))
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
        optimizer=tf.tpu.experimental.embedding.AdagradMomentum(0.1))

In the above example, the first feature will be looked up in a table that has a learning rate of 0.2 while the second feature will be looked up in a table that has a learning rate of 0.1.

See 'tensorflow/core/protobuf/tpu/optimization\_parameters.proto' for a complete description of these parameters and their impacts on the optimizer algorithm.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | The learning rate. It should be a floating point value or a callable taking no arguments for a dynamic learning rate. |
| `momentum` | Moving average parameter for the momentum accumulator. |
| `use_nesterov` | Whether to use the Nesterov variant of momentum. See Sutskever et al., 2013. |
| `exponent` | Exponent for the Adagrad accumulator. |
| `beta2` | Moving average parameter for the Adagrad accumulator. |
| `epsilon` | initial accumulator for Adagrad accumulator. |
| `use_gradient_accumulation` | setting this to `False` makes embedding gradients calculation less accurate but faster. |
| `clip_weight_min` | the minimum value to clip by; None means -infinity. |
| `clip_weight_max` | the maximum value to clip by; None means +infinity. |
| `weight_decay_factor` | amount of weight decay to apply; None means that the weights are not decayed. |
| `multiply_weight_decay_factor_by_learning_rate` | if true, `weight_decay_factor` is multiplied by the current learning rate. |
| `slot_variable_creation_fn` | If you wish do directly control the creation of the slot variables, set this to a callable taking three parameters: a table variable, a list of slot names to create for it, and a list of initializers. This function should return a dict with the slot names as keys and the created variables as values with types matching the table variable. When set to None (the default), uses the built-in variable creation. |
| `clipvalue` | Controls clipping of the gradient. Set to either a single positive scalar value to get clipping or a tuple of scalar values (min, max) to set a separate maximum or minimum. If one of the two entries is None, then there will be no clipping that direction. |
| `low_dimensional_packing_status` | Status of the low-dimensional embedding packing optimization controls whether to optimize the packing of 1-dimensional, 2-dimensional, and 4-dimensional embedding tables in memory. |

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L122-L129)

__eq__(
        other: Any
    ) -> Union[Any, bool]

Return self==value.

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.