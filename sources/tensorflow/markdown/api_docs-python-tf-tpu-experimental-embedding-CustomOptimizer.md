[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2FCustomOptimizer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.CustomOptimizer Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L219-L398)

Optimization parameters for custom optimizer for TPU embeddings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.CustomOptimizer`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomOptimizer)

tf.tpu.experimental.embedding.CustomOptimizer(
        custom_computation: tf.types.experimental.PolymorphicFunction,
        learning_rate: Union[float, Callable[[], float]] = 0.01,
        slot_names: Optional[List[str]] = None,
        slot_initializers: Optional[List[init_ops_v2.Initializer]] = None,
        hyperparameters: Optional[List[Union[float, Callable[[], float]]]] = None,
        slot_dims: Optional[List[int]] = None
    ) -> Any

This optimizer gives the user the ability to define a custom optimizer for running embedding lookups on TPU v5p.

The custom computation should be a function which takes gradient, embedding table, a list of slot variables, learning\_rate and a list of hyperparameters. The function should perform the gradient update on the embedding\_table + slot\_variables and return the updated embedding\_table and slot\_variables. e.g.

@tf.function
    def sgd_optimizer_computation(
        gradient,
        embedding_table,
        slot_variables,
        learning_rate,
        hyperparameters,
    ):
      del slot_variables, hyperparameters
      return embedding_table - gradient * learning_rate

Above is a simple example of a sgd optimizer. You can also define a more complex optimizer which updates multiple tables and slot variables.

@def_function.function
    def adagrad_optimizer_computation(
        gradient,
        embedding_table,
        slot_variables,
        learning_rate,
        hyperparameters,
    ):
      del hyperparameters
      accumulator = slot_variables[0]
      new_accumulator = accumulator + gradient * gradient
      updated_embedding_table = (
          embedding_table
          - learning_rate * gradient / math_ops.sqrt(new_accumulator)
      )
      return (updated_embedding_table, new_accumulator)

The custom computation is defined as a per-row update function and it will be auto scaled for the entire table (slot variables).

Pass this to [`tf.tpu.experimental.embedding.TPUEmbeddingV2`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbeddingV2)
 via the `optimizer` argument to set the global optimizer and its parameters:

optimizer = tf.tpu.experimental.embedding.CustomOptimizer(
          custom_computation=adagrad_optimizer_computation,
          learning_rate=1.0,
          slot_names=['accumulators'],
          slot_initializers=[\
              tf.constant_initializer(0.1, support_partition=True)\
          ],
      )
    embedding = tf.tpu.experimental.embedding.TPUEmbeddingV2(
        ...
        optimizer=optimizer)

This can also be used in a [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 as the optimizer parameter to set a table specific optimizer. This will override the optimizer and parameters for global embedding optimizer defined above:

table_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...,
        optimizer=optimizer)
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
        optimizer=optimizer)

In this example, the optimizer of the first table will be the one specified in the table config. The second table will use the optimizer specified in the TPUEmbedding argument.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `custom_computation` |     |
| `hyperparameters` |     |
| `slot_dims` | Optional per-slot dimensions metadata for variable creation.<br><br>Each entry corresponds to the same-index item in `slot_names`. This is consumed by the embedding layer when creating slot variables. |

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