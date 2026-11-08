[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#get_special_tokens_dict)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.BertTokenizer Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertTokenizer#get_special_tokens_dict)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L61-L235)

Wraps TF.Text's BertTokenizer with pre-defined vocab as a Keras Layer.

tfm.nlp.layers.BertTokenizer(
        *,
        vocab_file: str,
        lower_case: Optional[bool] = None,
        tokenize_with_offsets: bool = False,
        tokenizer_kwargs: Optional[Mapping[Text, Any]] = None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_file` | A Python string with the path of the vocabulary file. This is a text file with newline-separated wordpiece tokens. This layer initializes a lookup table from it that gets used with [`text.BertTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer)<br>. |
| `lower_case` | Optional boolean forwarded to [`text.BertTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer)<br>. If true, input text is converted to lower case (where applicable) before tokenization. This must be set to match the way in which the `vocab_file` was created. If passed, this overrides whatever value may have been passed in `tokenizer_kwargs`. |
| `tokenize_with_offsets` | A Python boolean. If true, this layer calls [`text.BertTokenizer.tokenize_with_offsets()`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer#tokenize_with_offsets)<br> instead of plain [`text.BertTokenizer.tokenize()`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer#tokenize)<br> and outputs a triple of `(tokens, start_offsets, limit_offsets)` insead of just tokens. |
| `tokenizer_kwargs` | Optional mapping with keyword arguments to forward to [`text.BertTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer)<br>'s constructor. |
| `**kwargs` | Standard arguments to `Layer()`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | If importing `tensorflow_text` failed. |

|     |     |     |
| --- | --- | --- |
| Attributes<br>---------- |     |
| `tokenize_with_offsets` | If true, calls [`text.BertTokenizer.tokenize_with_offsets()`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer#tokenize_with_offsets)<br> instead of plain [`text.BertTokenizer.tokenize()`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer#tokenize)<br> and outputs a triple of `(tokens, start_offsets, limit_offsets)`. |
| `raw_table_access` | An object with methods `.lookup(keys) and`.size()`that operate on the raw lookup table of tokens. It can be used to look up special token synbols like`\[MASK\]`. </td> </tr><tr> <td>`vocab\_size\` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L138-L173)

call(
        inputs: tf.Tensor
    )

Calls [`text.BertTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer)
 on inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A string Tensor of shape `(batch_size,)`. |

|     |
| --- |
| Returns |     |
| One or three of `RaggedTensors` if `tokenize_with_offsets` is False or True, respectively. These are tokens: A `RaggedTensor` of shape `[batch_size, (words), (pieces_per_word)]` and type int32. `tokens[i,j,k]` contains the k-th wordpiece of the j-th word in the i-th input. start\_offsets, limit\_offsets: If `tokenize_with_offsets` is True, RaggedTensors of type int64 with the same indices as tokens. Element `[i,j,k]` contains the byte offset at the start, or past the end, resp., for the k-th wordpiece of the j-th word in the i-th input. |     |

### `get_special_tokens_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L179-L196)

get_special_tokens_dict()

Returns dict of token ids, keyed by standard names for their purpose.

|     |
| --- |
| Returns |     |
| A dict from Python strings to Python integers. Each key is a standard name for a special token describing its use. (For example, "padding\_id" is what BERT traditionally calls "\[PAD\]" but others may call "".) The corresponding value is the integer token id. If a special token is not found, its entry is omitted from the dict.<br><br>The supported keys and tokens are:<br><br>*   start\_of\_sequence\_id: looked up from "\[CLS\]"<br>*   end\_of\_segment\_id: looked up from "\[SEP\]"<br>*   padding\_id: looked up form "\[PAD\]"<br>*   mask\_id: looked up from "\[MASK\]"<br>*   vocab\_size: one past the largest token id used |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.