[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fmodels%2FTransformerDecoder&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.TransformerDecoder Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerDecoder#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L474-L643)

Transformer decoder.

tfm.nlp.models.TransformerDecoder(
        num_layers=6,
        num_attention_heads=8,
        intermediate_size=2048,
        activation='relu',
        dropout_rate=0.0,
        attention_dropout_rate=0.0,
        use_bias=False,
        norm_first=True,
        norm_epsilon=1e-06,
        intermediate_dropout=0.0,
        self_attention_cls=None,
        cross_attention_cls=None,
        **kwargs
    )

Like the encoder, the decoder is made up of N identical layers. Each layer is composed of the sublayers:

1.  Self-attention layer
2.  Multi-headed attention layer combining encoder outputs with results from the previous self-attention layer.
3.  Feedforward network (2 fully-connected layers)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_layers` | Number of layers. |
| `num_attention_heads` | Number of attention heads. |
| `intermediate_size` | Size of the intermediate (Feedforward) layer. |
| `activation` | Activation for the intermediate layer. |
| `dropout_rate` | Dropout probability. |
| `attention_dropout_rate` | Dropout probability for attention layers. |
| `use_bias` | Whether to enable use\_bias in attention layer. If set `False`, use\_bias in attention layer is disabled. |
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set `False`, output of attention and intermediate dense layers is normalized. |
| `norm_epsilon` | Epsilon value to initialize normalization layers. |
| `intermediate_dropout` | Dropout probability for intermediate\_dropout\_layer. |
| `self_attention_cls` | An optional class to use for self attention or a function that provides the class per layer. |
| `cross_attention_cls` | An optional class to use for cross attention or a function that provides the class per layer. |
| `**kwargs` | key word arguemnts passed to tf\_keras.layers.Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L589-L643)

call(
        target,
        memory,
        self_attention_mask=None,
        cross_attention_mask=None,
        cache=None,
        decode_loop_step=None,
        return_all_decoder_outputs=False
    )

Return the output of the decoder layer stacks.

|     |     |
| --- | --- |
| Args |     |
| `target` | A tensor with shape `(batch_size, target_length, hidden_size)`. |
| `memory` | A tensor with shape `(batch_size, input_length, hidden_size)`. |
| `self_attention_mask` | A tensor with shape `(batch_size, target_len, target_length)`, the mask for decoder self-attention layer. |
| `cross_attention_mask` | A tensor with shape `(batch_size, target_length, input_length)` which is the mask for encoder-decoder attention layer. |
| `cache` | (Used for fast decoding) A nested dictionary storing previous decoder self-attention values. The items are: {layer\_n: {"k": A tensor with shape `(batch_size, i, key_channels)`, "v": A tensor with shape `(batch_size, i, value_channels)`}, ...} |
| `decode_loop_step` | An integer, the step number of the decoding loop. Used only for autoregressive inference on TPU. |
| `return_all_decoder_outputs` | Return all decoder layer outputs. Note that the outputs are layer normed. This is useful when introducing per layer auxiliary loss. |

|     |
| --- |
| Returns |     |
| Output of decoder. float32 tensor with shape `(batch_size, target_length, hidden_size`). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.