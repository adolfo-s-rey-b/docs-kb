[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#call-arguments_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#returns_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.GroupQueryAttention Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#call-arguments_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#returns_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupQueryAttention?version=stable#from_config)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/grouped_query_attention.py#L16-L653)

Grouped Query Attention layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.GroupQueryAttention(
        head_dim,
        num_query_heads,
        num_key_value_heads,
        dropout=0.0,
        use_bias=True,
        sliding_window=None,
        flash_attention=None,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        use_gate=False,
        seed=None,
        **kwargs
    )

This is an implementation of grouped-query attention introduced by [Ainslie et al., 2023](https://arxiv.org/abs/2305.13245)
. Here `num_key_value_heads` denotes number of groups, setting `num_key_value_heads` to 1 is equivalent to multi-query attention, and when `num_key_value_heads` is equal to `num_query_heads` it is equivalent to multi-head attention.

This layer first projects `query`, `key`, and `value` tensors. Then, `key` and `value` are repeated to match the number of heads of `query`.

Then, the `query` is scaled and dot-producted with `key` tensors. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities and concatenated back to a single tensor.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `head_dim` | Size of each attention head. |
| `num_query_heads` | Number of query attention heads. |
| `num_key_value_heads` | Number of key and value attention heads. |
| `dropout` | Dropout probability. |
| `use_bias` | Boolean, whether the dense layers use bias vectors/matrices. |
| `sliding_window` | Optional positive integer. If set, restricts each query position to attend only to key positions within `sliding_window - 1` of itself (a symmetric band). Composes naturally with `use_causal_mask=True` to give the causal sliding window used by Mistral, Llama-3 long-context, and Phi-3. Defaults to `None` (full attention). |
| `flash_attention` | If `None`, the layer attempts to use flash attention for faster and more memory-efficient attention computations when possible. This behavior can be configured using [`keras.config.enable_flash_attention()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_flash_attention)<br> or [`keras.config.disable_flash_attention()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/disable_flash_attention)<br>. |
| `kernel_initializer` | Initializer for dense layer kernels. |
| `bias_initializer` | Initializer for dense layer biases. |
| `kernel_regularizer` | Regularizer for dense layer kernels. |
| `bias_regularizer` | Regularizer for dense layer biases. |
| `activity_regularizer` | Regularizer for dense layer activity. |
| `kernel_constraint` | Constraint for dense layer kernels. |
| `bias_constraint` | Constraint for dense layer kernels. |
| `use_gate` | Boolean, whether to apply a gated attention mechanism. When True, an additional gating branch is added based on the (Gated Attention for Large Language Models)\[https://arxiv.org/abs/2505.06708\]. It applies a sigmoid-activated linear projection to the query which then gates the attention output. This helps improve training stability and eliminates "attention sinks". |
| `seed` | Optional integer to seed the dropout layer. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `query` | Query tensor of shape `(batch_dim, target_seq_len, feature_dim)`, where `batch_dim` is batch size, `target_seq_len` is the length of target sequence, and `feature_dim` is dimension of feature. |
| `value` | Value tensor of shape `(batch_dim, source_seq_len, feature_dim)`, where `batch_dim` is batch size, `source_seq_len` is the length of source sequence, and `feature_dim` is dimension of feature. |
| `key` | Optional key tensor of shape `(batch_dim, source_seq_len, feature_dim)`. If not given, will use `value` for both `key` and `value`, which is most common case. |
| `attention_mask` | A boolean mask of shape `(batch_dim, target_seq_len, source_seq_len)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, where 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension. |
| `return_attention_scores` | A boolean to indicate whether the output should be `(attention_output, attention_scores)` if `True`, or `attention_output` if `False`. Defaults to `False`. |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Will go with either using the training mode of the parent layer/model or `False` (inference) if there is no parent layer. |
| `use_causal_mask` | A boolean to indicate whether to apply a causal mask to prevent tokens from attending to future tokens (e.g., used in a decoder Transformer). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `attention_output` | Result of the computation, of shape `(batch_dim, target_seq_len, feature_dim)`, where `target_seq_len` is for target sequence length and `feature_dim` is the query input last dim. |
| `attention_scores` | (Optional) attention coefficients of shape `(batch_dim, num_query_heads, target_seq_len, source_seq_len)`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.