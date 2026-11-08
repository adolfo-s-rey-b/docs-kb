[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [References](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.TransformerEncoderBlock Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [References](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/TransformerEncoderBlock#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/transformer_encoder_block.py#L70-L587)

TransformerEncoderBlock layer.

tfm.nlp.layers.TransformerEncoderBlock(
        num_attention_heads,
        inner_dim,
        inner_activation,
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
        use_rms_norm=False,
        output_dropout=0.0,
        attention_dropout=0.0,
        inner_dropout=0.0,
        attention_initializer=None,
        attention_axes=None,
        use_query_residual=True,
        key_dim=None,
        value_dim=None,
        output_last_dim=None,
        diff_q_kv_att_layer_norm=False,
        return_attention_scores=False,
        num_kv_heads=None,
        src_block_size=None,
        tgt_block_size=None,
        use_sigmoid_attn=False,
        sigmoid_attn_bias=None,
        linformer_dim=None,
        linformer_shared_kv_projection=True,
        **kwargs
    )

This layer implements the Transformer Encoder from "Attention Is All You Need". ([https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
), which combines a `tf_keras.layers.MultiHeadAttention` layer with a two-layer feedforward network.

|     |
| --- |
| References<br>---------- |     |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762)<br> [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_attention_heads` | Number of attention heads. |
| `inner_dim` | The output dimension of the first Dense layer in a two-layer feedforward network. |
| `inner_activation` | The activation for the first Dense layer in a two-layer feedforward network. |
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
| `use_rms_norm` | Whether to use RMSNorm instead of LayerNorm. |\
| `output_dropout` | Dropout probability for the post-attention and output dropout. |\
| `attention_dropout` | Dropout probability for within the attention layer. |\
| `inner_dropout` | Dropout probability for the first Dense layer in a two-layer feedforward network. |\
| `attention_initializer` | Initializer for kernels of attention layers. If set `None`, attention layers use kernel\_initializer as initializer for kernel. |\
| `attention_axes` | axes over which the attention is applied. `None` means attention over all axes, but batch, heads, and features. |\
| `use_query_residual` | Toggle to execute residual connection after attention. |\
| `key_dim` | `key_dim` for the `tf_keras.layers.MultiHeadAttention`. If `None`, we use the first `input_shape`'s last dim. |\
| `value_dim` | `value_dim` for the `tf_keras.layers.MultiHeadAttention`. |\
| `output_last_dim` | Final dimension of the output of this module. This also dictates the value for the final dimension of the multi-head-attention. When it's `None`, we use, in order of decreasing precedence, `key_dim` \* `num_heads` or the first `input_shape`'s last dim as the output's last dim. |\
| `diff_q_kv_att_layer_norm` | If `True`, create a separate attention layer norm layer for query and key-value if `norm_first` is `True`. Invalid to set to `True` if `norm_first` is `False`. |\
| `return_attention_scores` | If `True`, the output of this layer will be a tuple and additionally contain the attention scores in the shape of `[batch_size, num_attention_heads, seq_dim, seq_dim]`. |\
| `num_kv_heads` | Number of key-value heads for multi-query attention. Refer to `multi_query_attention.MultiHeadAttention` for more details. |\
| `src_block_size` | Source block size. Refer to `block_sparse_attention.MultiHeadAttention` for more details. |\
| `tgt_block_size` | Target block size. Refer to `block_sparse_attention.MultiHeadAttention` for more details. |\
| `use_sigmoid_attn` | This param is only used in `block_sparse_attention.MultiHeadAttention` |\
| `sigmoid_attn_bias` | This param is only used in `block_sparse_attention.MultiHeadAttention` |\
| `linformer_dim` | Applies low-rank factorization on keys/values as in https://arxiv.org/pdf/2006.04768. |\
| `linformer_shared_kv_projection` | If set, projection layer is shared for keys and values. |\
| `**kwargs` | keyword arguments. |\
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