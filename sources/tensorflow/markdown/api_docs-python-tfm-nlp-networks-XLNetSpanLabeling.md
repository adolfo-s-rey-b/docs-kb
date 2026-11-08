[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#call)
        
    *   [end\_logits](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#end_logits)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.XLNetSpanLabeling Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#call)
        
    *   [end\_logits](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetSpanLabeling#end_logits)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/span_labeling.py#L114-L340)

Span labeling network head for XLNet on SQuAD2.0.

tfm.nlp.networks.XLNetSpanLabeling(
        input_width,
        start_n_top=5,
        end_n_top=5,
        activation='tanh',
        dropout_rate=0.0,
        initializer='glorot_uniform',
        **kwargs
    )

This networks implements a span-labeler based on dense layers and question possibility classification. This is the complex version seen in the original XLNet implementation.

This applies a dense layer to the input sequence data to predict the start positions, and then uses either the true start positions (if training) or beam search to predict the end positions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_width` | The innermost dimension of the input tensor to this network. |
| `start_n_top` | Beam size for span start. |
| `end_n_top` | Beam size for span end. |
| `activation` | The activation, if any, for the dense layer in this network. |
| `dropout_rate` | The dropout rate used for answer classification. |
| `initializer` | The initializer for the dense layer in this network. Defaults to a Glorot uniform initializer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/span_labeling.py#L217-L333)

call(
        sequence_data,
        class_index,
        paragraph_mask=None,
        start_positions=None,
        training=False
    )

Implements call().

#### Einsum glossary:

*   b: the batch size.
*   l: the sequence length.
*   h: the hidden size, or input width.
*   k: the start/end top n.

|     |     |
| --- | --- |
| Args |     |
| `sequence_data` | The input sequence data of shape `(batch_size, seq_length, input_width)`. |
| `class_index` | The class indices of the inputs of shape `(batch_size,)`. |
| `paragraph_mask` | Invalid position mask such as query and special symbols (e.g. PAD, SEP, CLS) of shape `(batch_size,)`. |
| `start_positions` | The start positions of each example of shape `(batch_size,)`. |
| `training` | Whether or not this is the training phase. |

|     |
| --- |
| Returns |     |
| A dictionary with the keys `start_predictions`, `end_predictions`, `start_logits`, `end_logits`.<br><br>If inference, then `start_top_predictions`, `start_top_index`, `end_top_predictions`, `end_top_index` are also included. |     |

### `end_logits`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/span_labeling.py#L189-L215)

end_logits(
        inputs
    )

Computes the end logits.

Input shapes into the inner, layer norm, output layers should match.

During training, inputs shape should be \[batch\_size, seq\_length, input\_width\].

During inference, input shapes should be \[batch\_size, seq\_length, start\_n\_top, input\_width\].

|     |     |
| --- | --- |
| Args |     |
| `inputs` | The input for end logits. |

|     |
| --- |
| Returns |     |
| Calculated end logits. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.