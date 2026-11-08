[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fnetworks%2FFNet&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.FNet Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/FNet#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/fnet.py#L35-L351)

FNet encoder network.

tfm.nlp.networks.FNet(
        vocab_size: int,
        hidden_size: int = 768,
        num_layers: int = 12,
        mixing_mechanism: tfm.nlp.layers.MixingMechanism = tfm.nlp.layers.MixingMechanism.FOURIER,
        use_fft: bool = False,
        attention_layers: Sequence[int] = (),
        num_attention_heads: int = 12,
        max_sequence_length: int = 512,
        type_vocab_size: int = 16,
        inner_dim: int = 3072,
        inner_activation: _Activation = _approx_gelu,
        output_dropout: float = 0.1,
        attention_dropout: float = 0.1,
        initializer: _Initializer = tf_keras.initializers.TruncatedNormal(stddev=0.02),
        output_range: Optional[int] = None,
        embedding_width: Optional[int] = None,
        embedding_layer: Optional[tf_keras.layers.Layer] = None,
        norm_first: bool = False,
        with_dense_inputs: bool = False,
        **kwargs
    )

Based on ["FNet: Mixing Tokens with Fourier Transforms"](https://aclanthology.org/2022.naacl-main.319/)
. FNet is an efficient Transformer-like encoder network that replaces self-attention sublayers with Fourier sublayers.

This implementation defaults to the canonical FNet Base model, but the network also supports more general mixing models (e.g. 'Linear', 'HNet') and hybrid models (e.g. 'FNet-Hybrid') models that use both mixing and self-attention layers. The input length is fixed to 'max\_sequence\_length'.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | The size of the token vocabulary. |
| `hidden_size` | The size of the transformer hidden layers. |
| `num_layers` | The number of transformer layers. |
| `mixing_mechanism` | Type of mixing mechanism used in place of self-attention layers. Defaults to FNet ('Fourier') mixing. |
| `use_fft` | Only used for spectral mixing mechanisms. Determines whether to use Fast Fourier Transform (True) or the Discrete Fourier Transform (DFT) matrix (False; default) to compute the Fourier Transform. See layers.FourierTransformLayer or layers.HartleyTransformLayer for advice. |
| `attention_layers` | Specifies which layers, if any, should be attention layers in the encoder. The remaining \[0, num\_layers) setminus attention\_layers will use the specified `mixing_mechanism`. If using attention layers, a good rule of thumb is to place them in the final few layers. |\
| `num_attention_heads` | The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads. |\
| `max_sequence_length` | The only sequence length that this encoder can consume. This determines the variable shape for positional embeddings and the size of the mixing matrices. |\
| `type_vocab_size` | The number of types that the 'type\_ids' input can take. |\
| `inner_dim` | The output dimension of the first Dense layer in a two-layer feedforward network for each transformer. |\
| `inner_activation` | The activation for the first Dense layer in a two-layer feedforward network for each transformer. |\
| `output_dropout` | Dropout probability for the post-attention and output dropout. |\
| `attention_dropout` | The dropout rate to use for the attention layers within the transformer layers. |\
| `initializer` | The initializer to use for all weights in this encoder. |\
| `output_range` | The sequence output range, \[0, output\_range), by slicing the target sequence of the last transformer layer. `None` means the entire target sequence will attend to the source sequence, which yields the full output. |\
| `embedding_width` | The width of the word embeddings. If the embedding width is not equal to hidden size, embedding parameters will be factorized into two matrices in the shape of \['vocab\_size', 'embedding\_width'\] and ['embedding\_width', 'hidden\_size'](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/'embedding_width'%20is%20usually%20much%0Asmaller%20than "hidden_size")<br>. |\
| `embedding_layer` | An optional Layer instance which will be called to generate embeddings for the input word IDs. |\
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set False, output of attention and intermediate dense layers is normalized. |\
| `with_dense_inputs` | Whether to accept dense embeddings as the input. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `pooler_layer` | The pooler dense layer after the transformer layers. |\
| `transformer_layers` | List of Transformer layers in the encoder. |\
\
Methods\
-------\
\
### `call`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/fnet.py#L245-L300)\
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
### `get_embedding_layer`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/fnet.py#L305-L306)\
\
get_embedding_layer()\
\
### `get_embedding_table`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/fnet.py#L302-L303)\
\
get_embedding_table()\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.