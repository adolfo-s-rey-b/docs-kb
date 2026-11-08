[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FKernelAttention&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.KernelAttention Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/KernelAttention#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/kernel_attention.py#L518-L843)

A variant of efficient transformers which replaces softmax with kernels.

tfm.nlp.layers.KernelAttention(
        feature_transform='exp',
        num_random_features=256,
        seed=0,
        redraw=False,
        is_short_seq=False,
        begin_kernel=0,
        scale=None,
        scale_by_length=False,
        use_causal_windowed=False,
        causal_chunk_length=1,
        causal_window_length=3,
        causal_window_decay=None,
        causal_padding=None,
        **kwargs
    )

This module combines ideas from the two following papers:

Rethinking Attention with Performers ([https://arxiv.org/abs/2009.14794](https://arxiv.org/abs/2009.14794)
)

*   exp (Lemma 1, positive), relu
*   random/deterministic projection Chefs' Random Tables: Non-Trigonometric Random Features ([https://arxiv.org/abs/2205.15317](https://arxiv.org/abs/2205.15317)
    )
*   expplus (OPRF mechanism)

Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention ([https://arxiv.org/abs/2006.16236](https://arxiv.org/abs/2006.16236)
)

*   elu

with the theory of approximating angular Performer kernels from go/performer.

The module enables computing efficient attention in both: long sequence and shorter sequence regimes. In the former setting, the attention matrix is never explicitly computed and instead its low-rank decomposition obtained with given kernel feature maps is leveraged to conduct attention module calculations (see: [https://arxiv.org/abs/2006.16236](https://arxiv.org/abs/2006.16236)
). In the latter setting, attention matrix is constructed, but kernel features providing dimensionality reduction are applied, resulting in more efficient computation of the attention matrix.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `feature_transform` | A non-linear transform of the keys and queries. Possible transforms are "elu", "relu", "square", "exp", "expplus", "expmod", "identity". |
| `num_random_features` | Number of random features to be used for projection. if num\_random\_features <= 0, no production is used before transform. |
| `seed` | The seed to begin drawing random features. Once the seed is set, the psedo number generation is determinisitc. Users should pass different seed for different layers. For multi-worker, each layer will use the same projection at each step. |
| `redraw` | Whether to redraw projection every forward pass during training. The argument is only effective when num\_random\_features > 0. |
| `is_short_seq` | boolean predicate indicating whether input data consists of very short sequences or not; in most cases this should be False (default option). |
| `begin_kernel` | Apply kernel\_attention after this sequence id and apply softmax attention before this. |
| `scale` | The value to scale the dot product as described in `Attention Is All You Need`. If None, we use 1/sqrt(dk) as described in the paper. |
| `scale_by_length` | boolean predicate indicating whether additionally scale the dot product based on key length. Set as log\_512^(n) to stablize attention entropy against length. Refer to https://kexue.fm/archives/8823 for details. |
| `use_causal_windowed` | If true perform windowed causal attention. See causal\_windowed\_performer\_attention function docstring for more details. |
| `causal_chunk_length` | Length of each chunk in tokens. |
| `causal_window_length` | Length of attention window in chunks. |
| `causal_window_decay` | Float window decay factor or `None`. If set, exponentially decay past attention window values by this factor before summation. |
| `causal_padding` | Pad the query, value and key input tensors across the axis from either left or right if padding is set to "left" or "right"; apply no padding if padding is set to None. In the latter case, the axis dimension of the query, value and key input tensors must be divisible by the chunk\_length. |
| `**kwargs` | The same arguments `MultiHeadAttention` layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/kernel_attention.py#L747-L824)

call(
        query, value, key=None, attention_mask=None, cache=None, training=False
    )

Compute attention with kernel mechanism.

|     |     |
| --- | --- |
| Args |     |
| `query` | Query `Tensor` of shape `[B, T, dim]`. |
| `value` | Value `Tensor` of shape `[B, S, dim]`. |
| `key` | Optional key `Tensor` of shape `[B, S, dim]`. If not given, will use `value` for both `key` and `value`, which is the most common case. |
| `attention_mask` | a boolean mask of shape `[B, S]`, that prevents attenting to masked positions. Note that the mask is only appied to the keys. User may want to mask the output if query contains pads. |
| `cache` | Cache to accumulate history in memory. Used at inferecne time (streaming, decoding) for causal attention. |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing). |

|     |
| --- |
| Returns |     |
| Multi-headed outputs of attention computation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.