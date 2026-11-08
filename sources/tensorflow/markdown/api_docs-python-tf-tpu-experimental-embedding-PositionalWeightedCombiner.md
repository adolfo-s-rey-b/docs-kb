[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2FPositionalWeightedCombiner&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.PositionalWeightedCombiner Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1254-L1316)

Positional weighted combiner for TPU embeddings on SparseCore.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.PositionalWeightedCombiner`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/PositionalWeightedCombiner)

tf.tpu.experimental.embedding.PositionalWeightedCombiner(
        max_valency: int,
        initializer: init_ops_v2.Initializer,
        custom_optimizer: tf.tpu.experimental.embedding.CustomOptimizer
    ) -> Any

This class specifies a positional weighted sum combiner over the TPU embedding lookup results. It also supports a custom optimizer computation to be performed on the positional weights.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_valency` | The valency cap of the corresponding feature. This value is also used as the number of positional weights. |
| `initializer` | The initializer for the positional weights. |
| `custom_optimizer` | CustomOptimizer encapsulating the custom optimizer computation, learning rate, slot names, slot initializers, and hyperparameters. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `hyperparameters` |     |

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L122-L129)

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