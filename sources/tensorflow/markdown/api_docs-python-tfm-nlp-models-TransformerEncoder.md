[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.TransformerEncoder Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/TransformerEncoder#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L362-L471)

Transformer encoder.

tfm.nlp.models.TransformerEncoder(
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
        **kwargs
    )

Transformer encoder is made up of N identical layers. Each layer is composed of the sublayers:

1.  Self-attention layer
2.  Feedforward network (which is 2 fully-connected layers)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_layers` | Number of layers. |
| `num_attention_heads` | Number of attention heads. |
| `intermediate_size` | Size of the intermediate (Feedforward) layer. |
| `activation` | Activation for the intermediate layer. |
| `dropout_rate` | Dropout probability. |
| `attention_dropout_rate` | Dropout probability for attention layers. |
| `use_bias` | Whether to enable use\_bias in attention layer. If set False, use\_bias in attention layer is disabled. |
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set False, output of attention and intermediate dense layers is normalized. |
| `norm_epsilon` | Epsilon value to initialize normalization layers. |
| `intermediate_dropout` | Dropout probability for intermediate\_dropout\_layer. |
| `**kwargs` | key word arguemnts passed to tf\_keras.layers.Layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L451-L471)

call(
        encoder_inputs, attention_mask=None
    )

Return the output of the encoder.

|     |     |
| --- | --- |
| Args |     |
| `encoder_inputs` | A tensor with shape `(batch_size, input_length, hidden_size)`. |
| `attention_mask` | A mask for the encoder self-attention layer with shape `(batch_size, input_length, input_length)`. |

|     |
| --- |
| Returns |     |
| Output of encoder which is a `float32` tensor with shape `(batch_size, input_length, hidden_size)`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.