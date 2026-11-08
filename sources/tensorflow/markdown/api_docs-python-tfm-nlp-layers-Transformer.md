[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.Transformer Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/Transformer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer.py#L29-L144)

Transformer layer.

Inherits From: [`TransformerEncoderBlock`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock)

tfm.nlp.layers.Transformer(
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

This layer implements the Transformer from "Attention Is All You Need". ([https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
).

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
| `use_bias` | Whether to enable use\_bias in attention layer. If set False, use\_bias in attention layer is disabled. |\
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
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_encoder_block.py#L468-L587)\
\
call(\
        inputs: Any, output_range: Optional[tf.Tensor] = None\
    ) -> Any\
\
Transformer self-attention encoder block call.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `inputs` | a single tensor or a list of tensors. `input tensor` as the single sequence of embeddings. \[`input tensor`, `attention mask`\] to have the additional attention mask. \[`query tensor`, `key value tensor`, `attention mask`\] to have separate input streams for the query, and key/value to the multi-head attention. |\
| `output_range` | the sequence output range, \[0, output\_range) for slicing the target sequence. `None` means the target sequence is not sliced. If you would like to have no change to the model training, it is better to only set the `output_range` for serving. |\
\
|     |\
| --- |\
| Returns |     |\
| An output tensor with the same dimensions as input/query tensor. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.