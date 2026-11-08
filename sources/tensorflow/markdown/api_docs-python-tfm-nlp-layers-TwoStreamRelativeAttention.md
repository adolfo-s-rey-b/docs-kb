[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Call args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#call-args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#call)
        
    *   [compute\_attention](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#compute_attention)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.TwoStreamRelativeAttention Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Call args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#call-args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#call)
        
    *   [compute\_attention](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TwoStreamRelativeAttention#compute_attention)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/relative_attention.py#L322-L498)

Two-stream relative self-attention for XLNet.

Inherits From: [`MultiHeadRelativeAttention`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MultiHeadRelativeAttention)

tfm.nlp.layers.TwoStreamRelativeAttention(
        kernel_initializer='variance_scaling', **kwargs
    )

In XLNet, each token has two associated vectors at each self-attention layer, the content stream (h) and the query stream (g).

The content stream is the self-attention stream as in Transformer XL and represents the context and content (the token itself).

The query stream only has access to contextual information and the position, but not the content.

This layer shares the same build signature as `tf_keras.layers.MultiHeadAttention` but has different input/output projections.

|     |     |
| --- | --- |
| Call args<br>--------- |     |
| `content_stream` | `Tensor` of shape `[B, T, dim]`. |
| `content_attention_bias` | Bias `Tensor` for content based attention of shape `[num_heads, dim]`. |
| `positional_attention_bias` | Bias `Tensor` for position based attention of shape `[num_heads, dim]`. |
| `query_stream` | `Tensor` of shape `[B, P, dim]`. |
| `target_mapping` | `Tensor` of shape `[B, P, S]`. |
| `relative_position_encoding` | Relative positional encoding `Tensor` of shape `[B, L, dim]`. |
| `segment_matrix` | Optional `Tensor` representing segmentation IDs used in XLNet of shape `[B, S, S + M]`. |
| `segment_encoding` | Optional `Tensor` representing the segmentation encoding as used in XLNet of shape `[2, num_heads, dim]`. |
| `segment_attention_bias` | Optional trainable bias parameter added to the query had when calculating the segment-based attention score used in XLNet of shape `[num_heads, dim]`. |
| `state` | Optional `Tensor` of shape \[B, M, E\] where M is the length of the state or memory. If passed, this is also attended over as in Transformer XL. |
| `content_attention_mask` | a boolean mask of shape `[B, T, S]` that prevents attention to certain positions for content attention computation. |
| `query_attention_mask` | a boolean mask of shape `[B, T, S]` that prevents attention to certain position for query attention computation. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/relative_attention.py#L367-L498)

call(
        content_stream,
        content_attention_bias,
        positional_attention_bias,
        query_stream,
        relative_position_encoding,
        target_mapping=None,
        segment_matrix=None,
        segment_encoding=None,
        segment_attention_bias=None,
        state=None,
        content_attention_mask=None,
        query_attention_mask=None
    )

Compute multi-head relative attention over inputs.

|     |
| --- |
| Size glossary |     |
| *   Number of heads (H): the number of attention heads.<br>*   Value size (V): the size of each value embedding per head.<br>*   Key size (K): the size of each key embedding per head. Equally, the size of each query embedding per head. Typically K <= V.<br>*   Number of predictions (P): the number of predictions.<br>*   Batch dimensions (B).<br>*   Query (target) attention axes shape (T).<br>*   Value (source) attention axes shape (S), the rank must match the target.<br>*   Encoding length (L): The relative positional encoding length. |     |

|     |     |
| --- | --- |
| Args |     |
| `content_stream` | The content representation, commonly referred to as h. This serves a similar role to the standard hidden states in Transformer-XL. |
| `content_attention_bias` | A trainable bias parameter added to the query head when calculating the content-based attention score. |
| `positional_attention_bias` | A trainable bias parameter added to the query head when calculating the position-based attention score. |
| `query_stream` | The query representation, commonly referred to as g. This only has access to contextual information and position, but not content. If not provided, then this is MultiHeadRelativeAttention with self-attention. |
| `relative_position_encoding` | relative positional encoding for key and value. |
| `target_mapping` | Optional `Tensor` representing the target mapping used in partial prediction. |
| `segment_matrix` | Optional `Tensor` representing segmentation IDs used in XLNet. |
| `segment_encoding` | Optional `Tensor` representing the segmentation encoding as used in XLNet. |
| `segment_attention_bias` | Optional trainable bias parameter added to the query head when calculating the segment-based attention score. |
| `state` | (default None) optional state. If passed, this is also attended over as in TransformerXL and XLNet. |
| `content_attention_mask` | (default None) Optional mask that is added to content attention logits. If state is not None, the mask source sequence dimension should extend M. |
| `query_attention_mask` | (default None) Optional mask that is added to query attention logits. If state is not None, the mask source sequence dimension should extend M. |

|     |
| --- |
| Returns |     |
| content\_attention\_output, query\_attention\_output: the results of the computation, both of shape \[B, T, E\]. `T` is for target sequence shapes, `E` is the query input last dimension if `output_shape` is `None`. Otherwise, the multi-head outputs are projected to the shape specified by `output_shape`. |     |

### `compute_attention`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/relative_attention.py#L155-L229)

compute_attention(
        query,
        key,
        value,
        position,
        content_attention_bias,
        positional_attention_bias,
        segment_matrix=None,
        segment_encoding=None,
        segment_attention_bias=None,
        attention_mask=None
    )

Computes the attention.

This function defines the computation inside `call` with projected multihead Q, K, V, R inputs.

|     |     |
| --- | --- |
| Args |     |
| `query` | Projected query `Tensor` of shape `[B, T, N, key_dim]`. |
| `key` | Projected key `Tensor` of shape `[B, S + M, N, key_dim]`. |
| `value` | Projected value `Tensor` of shape `[B, S + M, N, key_dim]`. |
| `position` | Projected position `Tensor` of shape `[B, L, N, key_dim]`. |
| `content_attention_bias` | Trainable bias parameter added to the query head when calculating the content-based attention score. |
| `positional_attention_bias` | Trainable bias parameter added to the query head when calculating the position-based attention score. |
| `segment_matrix` | Optional `Tensor` representing segmentation IDs used in XLNet. |
| `segment_encoding` | Optional trainable `Tensor` representing the segmentation encoding as used in XLNet. |
| `segment_attention_bias` | Optional trainable bias parameter added to the query had when calculating the segment-based attention score used in XLNet. |
| `attention_mask` | (default None) Optional mask that is added to attention logits. If state is not None, the mask source sequence dimension should extend M. |

|     |     |
| --- | --- |
| Returns |     |
| `attention_output` | Multi-headed output of attention computation of shape `[B, S, N, key_dim]`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.