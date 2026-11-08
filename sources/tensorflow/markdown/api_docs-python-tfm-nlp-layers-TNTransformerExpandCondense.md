[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.TNTransformerExpandCondense Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TNTransformerExpandCondense#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/tn_transformer_expand_condense.py#L24-L253)

Transformer layer using tensor network Expand-Condense layer.

tfm.nlp.layers.TNTransformerExpandCondense(
        num_attention_heads,
        intermediate_size,
        intermediate_activation,
        dropout_rate=0.0,
        attention_dropout_rate=0.0,
        output_range=None,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        use_bias=True,
        norm_first=False,
        norm_epsilon=1e-12,
        intermediate_dropout=0.0,
        attention_initializer=None,
        **kwargs
    )

This layer implements the Transformer from transformer.py, with a single tensor network layer replacing the usual intermediate and output Dense layers.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_attention_heads` | Number of attention heads. |
| `intermediate_size` | Size of the intermediate layer. |
| `intermediate_activation` | Activation for the intermediate layer. |
| `dropout_rate` | Dropout probability for the post-attention and output dropout. |
| `attention_dropout_rate` | Dropout probability for within the attention layer. |
| `output_range` | the sequence output range, \[0, output\_range) by slicing the target sequence. `None` means the target sequence is not sliced. |\
| `kernel_initializer` | Initializer for dense layer kernels. |\
| `bias_initializer` | Initializer for dense layer biases. |\
| `kernel_regularizer` | Regularizer for dense layer kernels. |\
| `bias_regularizer` | Regularizer for dense layer biases. |\
| `activity_regularizer` | Regularizer for dense layer activity. |\
| `kernel_constraint` | Constraint for dense layer kernels. |\
| `bias_constraint` | Constraint for dense layer kernels. |\
| `use_bias` | Whether to enable use\_bias in attention layer. If set to False, use\_bias in attention layer is disabled. |\
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set False, output of attention and intermediate dense layers is normalized. |\
| `norm_epsilon` | Epsilon value to initialize normalization layers. |\
| `intermediate_dropout` | Dropout probability for intermediate\_dropout\_layer. |\
| `attention_initializer` | Initializer for kernels of attention layers. If set `None`, attention layers use kernel\_initializer as initializer for kernel. |\
\
Methods\
-------\
\
### `call`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/tn_transformer_expand_condense.py#L215-L253)\
\
call(\
        inputs\
    )\
\
This is where the layer's logic lives.\
\
The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)\
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)\
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |\
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |\
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |\
\
|     |\
| --- |\
| Returns |     |\
| A tensor or list/tuple of tensors. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.