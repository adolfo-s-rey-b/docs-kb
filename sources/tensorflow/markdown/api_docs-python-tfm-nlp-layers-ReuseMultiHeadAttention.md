[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.ReuseMultiHeadAttention Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#call-arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#returns)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseMultiHeadAttention#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/reuse_attention.py#L112-L608)

MultiHeadAttention layer.

tfm.nlp.layers.ReuseMultiHeadAttention(
        num_heads,
        key_dim,
        value_dim=None,
        dropout=0.0,
        reuse_attention=0,
        use_relative_pe=False,
        pe_max_seq_length=512,
        use_bias=True,
        output_shape=None,
        attention_axes=None,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    )

This is an implementation of multi-headed attention as described in the paper "Attention is all you Need" (Vaswani et al., 2017). If `query`, `key,` `value` are the same, then this is self-attention. Each timestep in `query` attends to the corresponding sequence in `key`, and returns a fixed-width vector.

This layer first projects `query`, `key` and `value`. These are (effectively) a list of tensors of length `num_attention_heads`, where the corresponding shapes are `(batch_size, <query dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, key_dim)`, `(batch_size, <key/value dimensions>, value_dim)`.

Then, the query and key tensors are dot-producted and scaled. These are softmaxed to obtain attention probabilities. The value tensors are then interpolated by these probabilities, then concatenated back to a single tensor.

Finally, the result tensor with the last dimension as value\_dim can take an linear projection and return.

#### Examples:

Performs 1D cross-attention over two sequence inputs with an attention mask. Returns the additional attention weights over heads.

    layer = MultiHeadAttention(num_heads=2, key_dim=2)

Performs 2D self-attention over a 5D input tensor on axes 2 and 3.

    layer = MultiHeadAttention(num_heads=2, key_dim=2, attention_axes=(2, 3))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_heads` | Number of attention heads. |
| `key_dim` | Size of each attention head for query and key. |
| `value_dim` | Size of each attention head for value. |
| `dropout` | Dropout probability. |
| `reuse_attention` | An integer specifying number of heads to reuse. -1 for all heads. |
| `use_relative_pe` | Whether to use relative position bias. |
| `max_sequence_length` | Used to set the size of the relative positin encodings. |
| `use_bias` | Boolean, whether the dense layers use bias vectors/matrices. |
| `output_shape` | The expected shape of an output tensor, besides the batch and sequence dims. If not specified, projects back to the key feature dim. |
| `attention_axes` | axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features. |
| `kernel_initializer` | Initializer for dense layer kernels. |
| `bias_initializer` | Initializer for dense layer biases. |
| `kernel_regularizer` | Regularizer for dense layer kernels. |
| `bias_regularizer` | Regularizer for dense layer biases. |
| `activity_regularizer` | Regularizer for dense layer activity. |
| `kernel_constraint` | Constraint for dense layer kernels. |
| `bias_constraint` | Constraint for dense layer kernels. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `query` | Query `Tensor` of shape `(B, T, dim)`. |
| `value` | Value `Tensor` of shape `(B, S, dim)`. |
| `key` | Optional key `Tensor` of shape `(B, S, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case. |
| `attention_mask` | a boolean mask of shape `(B, T, S)`, that prevents attention to certain positions. The boolean mask specifies which query elements can attend to which key elements, 1 indicates attention and 0 indicates no attention. Broadcasting can happen for the missing batch dimensions and the head dimension. |
| `return_attention_scores` | A boolean to indicate whether the output should be attention output if True, or (attention\_output, attention\_scores) if False. Defaults to False. |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). Defaults to either using the training mode of the parent layer/model, or False (inference) if there is no parent layer. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `attention_output` | The result of the computation, of shape `(B, T, E)`, where `T` is for target sequence shapes and `E` is the query input last dimension if `output_shape` is `None`. Otherwise, the multi-head outputs are project to the shape specified by `output_shape`. |
| `attention_scores` | \[Optional\] multi-head attention coeffients over attention axes. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/reuse_attention.py#L568-L608)

call(
        query,
        value,
        key=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        reuse_attention_scores=None
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