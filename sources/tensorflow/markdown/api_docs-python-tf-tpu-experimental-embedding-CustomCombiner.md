[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.CustomCombiner Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1135-L1251)

Custom combiner for TPU embeddings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.CustomCombiner`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/CustomCombiner)

tf.tpu.experimental.embedding.CustomCombiner(
        combiner_computation: tf.types.experimental.PolymorphicFunction,
        max_valency: int,
        num_weights: int = 0,
        initializer: Optional[init_ops_v2.Initializer] = None,
        combiner_weights_learning_rate: Union[float, Callable[[], float]] = 0.01
    ) -> Any

This class gives the user the ability to define a custom combiner for running embedding lookups on TPU with SparseCores.

The custom computation should be a function which takes the following arguments: (1) valency: an integer scalar that indicates the actual number of valent IDs in the current sample. (2) vectors: a 2D tensor of shape \[max\_valency, embedding\_dim\] that represents the embedding lookup results to be combined. The vectors are guaranteed to be in the same order as the embedding IDs appear in the input sample. (3) weights: this argument is only present if `num_weights` of this class is greater than 0. It is a 1D tensor of shape \[num\_weights\] that will be back-propagated to during the backward pass. Currently only SGD optimizer is supported on these weights, with the learning rate being the `combiner_weights_learning_rate` argument of the constructor of this class.

The custom computation should return a 1D tensor of shape \[embedding\_dim\] that represents the combined embedding vector. An example combiner computation is as follows (it simply sums over the valent embedding vectors and is semantically equivalent to the `sum` combiner):

@tf.function
    def sum_combiner(valency, vectors):
      max_valency = vectors.shape[0]
      valid_mask = tf.range(max_valency) < valency
      vectors_masked = tf.where(
          tf.expand_dims(valid_mask, axis=-1),
          vectors,
          tf.zeros_like(vectors),
      )
      return tf.reduce_sum(vectors_masked, axis=0)

The custom computation is defined as a per-sample combiner function and it will be vectorized to the given batch size. This means certain constructs (such as control flow ops) may not be supported in the custom computation.

This class can be used in a [`tf.tpu.experimental.embedding.TableConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TableConfig)
 as the combiner parameter to set a table specific combiner.

custom_combiner = tpu_embedding_v2_utils.CustomCombiner(
        sum_combiner,
        max_valency=16,
    )
    
    table_one = tf.tpu.experimental.embedding.TableConfig(
        vocabulary_size=...,
        dim=...,
        combiner=custom_combiner)
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
        batch_size=...)

In this example, the combiner of the first table will be the `sum_combiner`. The second table will use the default `mean` combiner.

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L122-L129)

__eq__(
        other: Any
    ) -> Union[Any, bool]

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| CUSTOM\_COMBINER\_SLOT\_NAME | `'custom_combiner_variables'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.