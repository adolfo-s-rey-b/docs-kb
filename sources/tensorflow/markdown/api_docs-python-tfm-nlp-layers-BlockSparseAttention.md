[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.BlockSparseAttention Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BlockSparseAttention#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/block_sparse_attention.py#L42-L359)

Multi-head block sparse attention layer.

tfm.nlp.layers.BlockSparseAttention(
        src_block_size=None,
        tgt_block_size=None,
        use_sigmoid_attn=False,
        sigmoid_attn_bias=None,
        num_kv_heads=None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `src_block_size` | The block size of the query. An integer that divides the sequence length into blocks. |
| `tgt_block_size` | The block size of the key/value. An integer that divides the sequence length into blocks. The number of blocks in the source and target must be the same. |
| `use_sigmoid_attn` | If enabled, uses sigmoid instead of softmax to compute attn probs. https://arxiv.org/pdf/2409.04431 |
| `sigmoid_attn_bias` | Bias for sigmoid attn. Suggested value -ln(seq\_len). |
| `num_kv_heads` | Number of key/value heads in the multi-head self attention. Refer to multi\_query\_attention.py for more details. |
| `**kwargs` | Args passed to the base class. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/block_sparse_attention.py#L339-L359)

call(
        query,
        value,
        key=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        use_causal_mask=False
    )

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.