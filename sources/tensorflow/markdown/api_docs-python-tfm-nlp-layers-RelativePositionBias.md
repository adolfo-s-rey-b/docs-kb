[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.RelativePositionBias Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionBias#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/position_embedding.py#L230-L307)

Relative position embedding via per-head bias in T5 style.

tfm.nlp.layers.RelativePositionBias(
        num_heads: int,
        relative_attention_num_buckets: int = 32,
        relative_attention_max_distance: int = 128,
        bidirectional: bool = True,
        embeddings_initializer: Optional[Initializer] = None,
        **kwargs
    )

Reference implementation in MeshTF: [https://github.com/tensorflow/mesh/blob/master/mesh\_tensorflow/transformer/transformer\_layers.py#L1000](https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/transformer_layers.py#L1000)

This layer implements the relative position bias used in "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" ([https://arxiv.org/abs/1910.10683](https://arxiv.org/abs/1910.10683)
)

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/position_embedding.py#L282-L307)

call(
        query: tf.Tensor, key: tf.Tensor
    )

Implements the forward pass.

|     |     |
| --- | --- |
| Args |     |
| `query` | query input tensor shape \[batch, query length, hidden size\]. |
| `key` | key input tensor shape \[batch, key length, hidden size\]. |

|     |
| --- |
| Returns |     |
| A tensor in shape of \[batch, heads, query length, key length\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.