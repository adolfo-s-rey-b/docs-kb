[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.ReuseTransformer Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ReuseTransformer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/reuse_transformer.py#L22-L360)

Transformer layer.

tfm.nlp.layers.ReuseTransformer(
        num_attention_heads,
        inner_dim,
        inner_activation,
        head_size=None,
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
        output_dropout=0.0,
        attention_dropout=0.0,
        inner_dropout=0.0,
        attention_initializer=None,
        attention_axes=None,
        reuse_attention=0,
        use_relative_pe=False,
        pe_max_seq_length=512,
        layer_idx=None,
        max_reuse_layer_idx=None,
        **kwargs
    )

This layer implements the ReuseTransformer Encoder from "Leveraging redundancy in attention with Reuse Transformers". ([https://arxiv.org/abs/2110.06821](https://arxiv.org/abs/2110.06821)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_attention_heads` | Number of attention heads. |
| `inner_dim` | The output dimension of the first Dense layer in a two-layer feedforward network. |
| `inner_activation` | The activation for the first Dense layer in a two-layer feedforward network. |
| `head_size` | Projection size of heads. |
| `output_range` | the sequence output range, \[0, output\_range) for slicing the target sequence. `None` means the target sequence is not sliced. |\
| `kernel_initializer` | Initializer for dense layer kernels. |\
| `bias_initializer` | Initializer for dense layer biases. |\
| `kernel_regularizer` | Regularizer for dense layer kernels. |\
| `bias_regularizer` | Regularizer for dense layer biases. |\
| `activity_regularizer` | Regularizer for dense layer activity. |\
| `kernel_constraint` | Constraint for dense layer kernels. |\
| `bias_constraint` | Constraint for dense layer kernels. |\
| `use_bias` | Whether to enable use\_bias in attention layer. If set False, use\_bias in attention layer is disabled. |\
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set False, output of attention and intermediate dense layers is normalized. |\
| `norm_epsilon` | Epsilon value to initialize normalization layers. |\
| `output_dropout` | Dropout probability for the post-attention and output dropout. |\
| `attention_dropout` | Dropout probability for within the attention layer. |\
| `inner_dropout` | Dropout probability for the first Dense layer in a two-layer feedforward network. |\
| `attention_initializer` | Initializer for kernels of attention layers. If set `None`, attention layers use kernel\_initializer as initializer for kernel. |\
| `attention_axes` | axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features. |\
| `reuse_attention` | reuse\_attention: An integer specifying number of heads to reuse. -1 for all heads. |\
| `use_relative_pe` | whether to use relative position bias. |\
| `pe_max_seq_length` | used to set the size of the relative positin encodings. |\
| `layer_idx` | the idx of this layer. |\
| `max_reuse_layer_idx` | layer idx (if passed) greater than this value will not reuse attention scores from previous layers. |\
| `**kwargs` | keyword arguments. |\
\
Methods\
-------\
\
### `call`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/reuse_transformer.py#L276-L360)\
\
call(\
        inputs\
    )\
\
Transformer self-attention encoder block call.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `inputs` | a single tensor or a list of tensors. `input tensor` as the single sequence of embeddings. \[`input tensor`, `attention mask`\] to have the additional attention mask. \[`query tensor`, `attention mask`, `attention scores`\] to have additional attention scores for reuse computation. If `attention scores` is None, the reuse\_attention flag will be ignored. |\
\
|     |\
| --- |\
| Returns |     |\
| An output tensor with the same dimensions as input/query tensor. Attention scores if return\_attention\_scores is true. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.