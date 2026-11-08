[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.MultiHeadAttention Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/multi_head_attention.py#L19-L879)

MultiHeadAttention layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.MultiHeadAttention(
        num_heads,
        key_dim,
        value_dim=None,
        dropout=0.0,
        use_bias=True,
        output_shape=None,
        attention_axes=None,
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

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer) |

This is an implementation of multi-headed attention as described in the paper "Attention is all you Need" [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
. If `query`, `key,` `value` are the same, then this is self-attention. Each timestep in `query` attends to the corresponding sequence in `key`, and returns a fixed-width vector.

This layer first projects `query`, `key` and `value`. These are (effectively) a list of tensors of length `num_attention_heads`, where the corresponding shapes are `(batch_size, <query dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, value_dim)`.

Then, the query and key tensors are dot-producted and scaled. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities, then concatenated back to a single tensor.

Finally, the result tensor with the last dimension as `value_dim` can take a linear projection and return.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_heads` | Number of attention heads. |
| `key_dim` | Size of each attention head for query and key. |
| `value_dim` | Size of each attention head for value. |
| `dropout` | Dropout probability. |
| `use_bias` | Boolean, whether the dense layers use bias vectors/matrices. |
| `output_shape` | The expected shape of an output tensor, besides the batch and sequence dims. If not specified, projects back to the query feature dim (the query input's last dimension). |
| `attention_axes` | axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features. |
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
| `query` | Query tensor of shape `(B, T, dim)`, where `B` is the batch size, `T` is the target sequence length, and dim is the feature dimension. |
| `value` | Value tensor of shape `(B, S, dim)`, where `B` is the batch size, `S` is the source sequence length, and dim is the feature dimension. |
| `key` | Optional key tensor of shape `(B, S, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case. |
| `attention_mask` | a boolean mask of shape `(B, T, S)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension. |
| `return_attention_scores` | A boolean to indicate whether the output should be `(attention_output, attention_scores)` if `True`, or `attention_output` if `False`. Defaults to `False`. |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Will go with either using the training mode of the parent layer/model, or `False` (inference) if there is no parent layer. |
| `use_causal_mask` | A boolean to indicate whether to apply a causal mask to prevent tokens from attending to future tokens (e.g., used in a decoder Transformer). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `attention_output` | The result of the computation, of shape `(B, T, E)`, where `T` is for target sequence shapes and `E` is the query input last dimension if `output_shape` is `None`. Otherwise, the multi-head outputs are projected to the shape specified by `output_shape`. |
| `attention_scores` | (Optional) multi-head attention coefficients over attention axes. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `attention_axes` |     |
| `dropout` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `key_dense` |     |
| `key_dim` |     |
| `num_heads` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output_dense` |     |
| `query_dense` |     |
| `use_bias` |     |
| `value_dense` |     |
| `value_dim` |     |

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