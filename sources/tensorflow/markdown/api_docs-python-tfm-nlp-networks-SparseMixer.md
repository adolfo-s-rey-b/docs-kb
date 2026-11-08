[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.SparseMixer Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/SparseMixer#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/sparse_mixer.py#L35-L406)

Sparse Mixer encoder network.

tfm.nlp.networks.SparseMixer(
        vocab_size: int,
        hidden_size: int = 512,
        num_layers: int = 14,
        moe_layers: Sequence[int] = (5, 6, 7, 8),
        attention_layers: Sequence[int] = (10, 11, 12, 13),
        num_experts: int = 16,
        train_capacity_factor: float = 1.0,
        eval_capacity_factor: float = 1.0,
        examples_per_group: float = 1.0,
        mixing_mechanism: tfm.nlp.layers.MixingMechanism = tfm.nlp.layers.MixingMechanism.LINEAR,
        use_fft: bool = False,
        num_attention_heads: int = 8,
        max_sequence_length: int = 512,
        type_vocab_size: int = 16,
        inner_dim: int = 2048,
        inner_activation: _Activation = _approx_gelu,
        output_dropout: float = 0.1,
        attention_dropout: float = 0.1,
        initializer: _Initializer = tf_keras.initializers.TruncatedNormal(stddev=0.02),
        output_range: Optional[int] = None,
        embedding_width: Optional[int] = None,
        embedding_layer: Optional[tf_keras.layers.Layer] = None,
        norm_first: bool = False,
        with_dense_inputs: bool = False,
        export_metrics: bool = True,
        **kwargs
    )

Based on ["Sparse Mixers: Combining MoE and Mixing to build a more efficient BERT"](https://arxiv.org/abs/2205.12399)
. Sparse Mixer is an efficient encoder network that replaces typical Transformer encoder blocks with a combination of linear mixing and sparsely activated Mixture-of-Experts (MoE) sublayers.

This implementation defaults to the canonical Sparse Mixer Base model. To use the "Fast Sparse Mixer" configuration, set `*_capacity_factor`\=0.5. This yields a sparser and faster variant of the canonical Sparse Mixer model, in which each expert processes roughly 50% less tokens.

#### Notes:

*   The underlying MoeLayer uses the Keras add\_loss() and add\_metric() APIs to propagate auxiliary MoE losses and metrics. Any model using this network, should collect these losses and, if desired, metrics.
*   The input length is fixed to 'max\_sequence\_length' to accomodate the mixing mechanisms.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | The size of the token vocabulary. |
| `hidden_size` | The size of the transformer hidden layers. |
| `num_layers` | The number of transformer layers. |
| `moe_layers` | Specifies which layers, if any, should be sparsely activated Mixture-of-Experts (MoE) layers. The remaining \[0, num\_layers) setminus moe\_layers will use the vanilla MLP sublayers. Defaults to placing MoE layers in the middle of the model. |\
| `attention_layers` | Specifies which layers, if any, should be attention layers in the encoder. The remaining \[0, num\_layers) setminus attention\_layers will use the specified `mixing_mechanism`. If using attention layers, a good rule of thumb is to place them in the final few layers. |\
| `num_experts` | Number of experts. Experts are themselves MLP modules, with the same `inner_dim` and `inner_activation` as the vanilla MLP sublayers. |\
| `train_capacity_factor` | Scaling factor to increase the expert token capacity during training. See layers.MoeLayer for further details. The "Fast Sparse Mixer" increases model sparsity (and speed) by using a capacity factor of 0.5. |\
| `eval_capacity_factor` | As above, but used during evaluation. |\
| `max_group_size` | The total number of tokens on each device is subdivided into groups of this size. Router computations are then performed on a per-group basis. See layers.MoeLayer for further details. |\
| `mixing_mechanism` | Type of mixing mechanism used in place of self-attention layers. Defaults to 'Linear' mixing. |\
| `use_fft` | Only used for spectral mixing mechanisms. Determines whether to use Fast Fourier Transform (True) or the Discrete Fourier Transform (DFT) matrix (False; default) to compute the Fourier Transform. See layers.FourierTransformLayer or layers.HartleyTransformLayer for advice. |\
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
| `export_metrics` | Whether to export metrics using Keras add\_metric API. |\
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
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/sparse_mixer.py#L300-L355)\
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
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/sparse_mixer.py#L360-L361)\
\
get_embedding_layer()\
\
### `get_embedding_table`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/sparse_mixer.py#L357-L358)\
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