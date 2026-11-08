[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.TransformerXLBlock Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerXLBlock#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_xl.py#L54-L319)

Transformer XL block.

tfm.nlp.layers.TransformerXLBlock(
        vocab_size,
        hidden_size,
        num_attention_heads,
        head_size,
        inner_size,
        dropout_rate,
        attention_dropout_rate,
        two_stream=False,
        norm_epsilon=1e-12,
        inner_activation='relu',
        kernel_initializer='variance_scaling',
        inner_dropout=0.0,
        **kwargs
    )

This implements a Transformer XL block from "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context" ([https://arxiv.org/abs/1901.02860](https://arxiv.org/abs/1901.02860)
).

This block is further extended to allow for the Transformer-XL re-parameterization in "XLNet: Generalized Autoregressive Pretraining for Language Understanding" ([https://arxiv.org/abs/1906.08237](https://arxiv.org/abs/1906.08237)
).

Given an input stream, this block computes attention, applies dropouts and layer norms and feeds into the FFN network.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `vocab_size` | The size of the token vocabulary. |
| `hidden_size` | The size of the transformer hidden layers. |
| `num_attention_heads` | The number of attention heads. |
| `head_size` | The dimension size of each attention head. |
| `inner_size` | The inner size for the transformer layers. |
| `dropout_rate` | Dropout rate for the output of this layer. |
| `attention_dropout_rate` | Dropout rate on attention probabilities. |
| `two_stream` | Whether or not to use `TwoStreamRelativeAttention` used in the XLNet pretrainer. If `False`, then it will use `MultiHeadRelativeAttention` as in Transformer XL. |
| `norm_epsilon` | Epsilon value to initialize normalization layers. |
| `inner_activation` | The activation to use for the inner FFN layers. |
| `kernel_initializer` | Initializer for dense layer kernels. |
| `inner_dropout` | Dropout probability for the inner dropout layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_xl.py#L216-L319)

call(
        content_stream,
        content_attention_bias,
        positional_attention_bias,
        relative_position_encoding=None,
        segment_matrix=None,
        segment_encoding=None,
        segment_attention_bias=None,
        state=None,
        content_attention_mask=None,
        query_stream=None,
        query_attention_mask=None,
        target_mapping=None
    )

Implements `call` for the Layer.

|     |     |
| --- | --- |
| Args |     |
| `content_stream` | `Tensor`, the input content stream. This is the standard input to Transformer XL and is commonly referred to as `h` in XLNet. |
| `content_attention_bias` | Bias `Tensor` for content based attention of shape `[num_heads, dim]`. |
| `positional_attention_bias` | Bias `Tensor` for position based attention of shape `[num_heads, dim]`. |
| `relative_position_encoding` | Relative positional encoding `Tensor` of shape `[B, L, dim]`. |
| `segment_matrix` | Optional `Tensor` of shape `[B, S, S + M]`. Used in XLNet, but not in Transformer XL. |
| `segment_encoding` | Optional `Tensor` of shape `[2, num_heads, dim]`. Used in XLNet, but not in Transformer XL. |
| `segment_attention_bias` | Optional bias `Tensor` for segment based attention of shape `[num_heads, dim]`. |
| `state` | Optional `Tensor` of shape `[B, M, E]`, where M is the length of the state or memory. If passed, this is also attended over as in Transformer XL. |
| `content_attention_mask` | Optional `Tensor` representing the mask that is added to content attention logits. If state is not None, the mask source sequence dimension should extend M. |
| `query_stream` | Optional `Tensor`, the query stream. This is introduced in `TwoStreamRelativeAttention`/XLNet pretrainer. This is ignored if `two_stream` is `False`. |
| `query_attention_mask` | Optional `Tensor` representing the mask that is added to query attention logits. If state is not None, the mask source sequence dimension should extend M. |
| `target_mapping` | Optional `Tensor` representing the target mapping when calculating query attention. |

|     |
| --- |
| Returns |     |
| A `dict` object, containing the key value pairs for `content_attention` and (if `two_stream` is `True`) `query_attention`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.