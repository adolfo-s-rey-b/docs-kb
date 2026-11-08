[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.TransformerXL Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXL#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_xl.py#L322-L560)

Transformer XL.

tfm.nlp.layers.TransformerXL(
        vocab_size,
        num_layers,
        hidden_size,
        num_attention_heads,
        head_size,
        inner_size,
        dropout_rate,
        attention_dropout_rate,
        initializer,
        two_stream=False,
        tie_attention_biases=True,
        memory_length=None,
        reuse_length=None,
        inner_activation='relu',
        **kwargs
    )

This layer combines multiple Transformer XL blocks from "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context" ([https://arxiv.org/abs/1901.02860](https://arxiv.org/abs/1901.02860)
).

This layer handles the attention biases as well as memory caching and reuse as in Transformer XL and XLNet.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `vocab_size` | The number of tokens in vocabulary. |
| `num_layers` | The number of layers. |
| `hidden_size` | The hidden size. |
| `num_attention_heads` | The number of attention heads. |
| `head_size` | The dimension size of each attention head. |
| `inner_size` | The hidden size in feed-forward layers. |
| `dropout_rate` | Dropout rate used in each Transformer XL block. |
| `attention_dropout_rate` | Dropout rate on attention probabilities. |
| `two_stream` | Whether or not to use `TwoStreamRelativeAttention` used in the XLNet pretrainer. If `False`, then it will use `MultiHeadRelativeAttention` as in Transformer XL. |
| `initializer` | The initializer to use for attention biases. |
| `tie_attention_biases` | Whether or not to tie biases together. If `True`, then each Transformer XL block shares the same trainable attention bias. If `False`, then each block has its own attention bias. This is usually set to `True`. |
| `memory_length` | The number of tokens to cache. |
| `reuse_length` | The number of tokens in the current batch to be cached and reused in the future. |
| `inner_activation` | The activation to use in the inner layers for Transformer XL blocks. Typically "relu" or "gelu". |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_xl.py#L467-L560)

call(
        content_stream,
        relative_position_encoding,
        segment_matrix=None,
        segment_embedding=None,
        state=None,
        content_attention_mask=None,
        query_stream=None,
        query_attention_mask=None,
        target_mapping=None
    )

Implements call() for the layer.

|     |     |
| --- | --- |
| Args |     |
| `content_stream` | `Tensor`, the input content stream. This is the standard input to Transformer XL and is commonly referred to as `h` in XLNet. |
| `relative_position_encoding` | Relative positional encoding `Tensor` of shape `[B, L, dim]`. |
| `segment_matrix` | Optional `Tensor` of shape `[B, S, S + M]`. Used in XLNet, but not in Transformer XL. |
| `segment_embedding` | Optional `Tensor` of shape `[2, num_heads, dim]`. Used in XLNet, but not in Transformer XL. |
| `state` | Optional `Tensor` of shape `[B, M, E]`, where M is the length of the state or memory. If passed, this is also attended over as in Transformer XL. |
| `content_attention_mask` | Optional `Tensor` representing the mask that is added to content attention logits. If state is not None, the mask source sequence dimension should extend M. |
| `query_stream` | Optional `Tensor`, the query stream. This is introduced in `TwoStreamRelativeAttention`/XLNet pretrainer. This is ignored if `two_stream` is `False`. |
| `query_attention_mask` | Optional `Tensor` representing the mask that is added to query attention logits. If state is not None, the mask source sequence dimension should extend M. |
| `target_mapping` | Optional `Tensor` representing the target mapping when calculating query attention. |

|     |
| --- |
| Returns |     |
| A tuple consisting of the attention output and the list of cached memory states. The attention output is `content_attention` if `two_stream` is `False`, otherwise it is `query_attention`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.