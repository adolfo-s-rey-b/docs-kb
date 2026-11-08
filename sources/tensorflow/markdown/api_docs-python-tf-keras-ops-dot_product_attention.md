[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.dot\_product\_attention Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2859-L2963)

Scaled dot product attention function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.dot_product_attention`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/dot_product_attention)

tf.keras.ops.dot_product_attention(
        query,
        key,
        value,
        bias=None,
        mask=None,
        scale=None,
        is_causal=False,
        flash_attention=None,
        attn_logits_soft_cap=None
    )

Computes the attention function on Q (`query`), K (`key`), and V(`value`): `attention(Q, K, V) = softmax(Q * K / sqrt(d)) * V`. If we define `logits` as the output of `Q * K` and the `probs` as the output of `softmax`.

Throughout this function, we utilize the following notation to represent the shape of array:

*   B: batch size
*   S: length of the key/value
*   T: length of the query
*   N: number of attention heads
*   H: dimensions of each attention head
*   K: number of key/value heads
*   G: number of groups, which equals to `N // K`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `query` | The query array with the shape of `(B, T, N, H)`. |
| `key` | The key array with the shape of `(B, S, K, H)`. When `K` equals `N`, multi-headed attention (MHA) is performed. Otherwise, grouped query attention (GQA) is performed if `N` is a multiple of `K`. and multi-query attention (MQA) is performed if `K==1` (a special case of GQA). |
| `value` | The value array with the same shape of `key`. |
| `bias` | Optional bias array to be added to logits. The shape must be broadcastable to `(B, N, T, S)`. |
| `mask` | Optional mask array used to filter out logits. It is a boolean mask where `True` indicates the element should take part in attention. For an additive mask, users should pass it to bias. The shape must be broadcastable to `(B, N, T, S)`. |
| `scale` | Optional scale for the logits. If `None`, the scale will be set to `1.0 / sqrt(H)`. |
| `is_causal` | Whether to apply causal mask. |
| `flash_attention` | Whether to use flash attention. If `None`, it will attempt to use flash attention if the required conditions are met. Typically, the inputs must be in float16 and bfloat16 dtype and the input layout requirements may vary depending on the backend. |
| `attn_logits_soft_cap` | The value limit for maximum value of the attention logits before the softmax function is applied. This is only supported in JAX TPU backend. Defaults to None. |

|     |
| --- |
| Returns<br>------- |     |
| An array of the attention output with the same shape of `query`. |     |

#### Example:

    query = keras.random.normal((2, 4, 8, 16))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.