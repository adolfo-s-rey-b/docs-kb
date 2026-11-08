[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#get_special_tokens_dict)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.SentencepieceTokenizer Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/SentencepieceTokenizer#get_special_tokens_dict)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L238-L437)

Wraps `tf_text.SentencepieceTokenizer` as a Keras Layer.

tfm.nlp.layers.SentencepieceTokenizer(
        *,
        lower_case: bool,
        model_file_path: Optional[str] = None,
        model_serialized_proto: Optional[str] = None,
        tokenize_with_offsets: bool = False,
        nbest_size: int = 0,
        alpha: float = 1.0,
        strip_diacritics: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `lower_case` | A Python boolean indicating whether to lowercase the string before tokenization. NOTE: New models are encouraged to build `*_cf` (case folding) normalization into the Sentencepiece model itself and avoid this extra step. |
| `model_file_path` | A Python string with the path of the sentencepiece model. Exactly one of `model_file_path` and `model_serialized_proto` can be specified. In either case, the Keras model config for this layer will store the actual proto (not a filename passed here). |
| `model_serialized_proto` | The sentencepiece model serialized proto string. |
| `tokenize_with_offsets` | A Python boolean. If true, this layer calls [`SentencepieceTokenizer.tokenize_with_offsets()`](https://www.tensorflow.org/text/api_docs/python/text/SentencepieceTokenizer#tokenize_with_offsets)<br> instead of plain `.tokenize()` and outputs a triple of `(tokens, start_offsets, limit_offsets)` insead of just tokens. Note that when following `strip_diacritics` is set to True, returning offsets is not supported now. |
| `nbest_size` | A scalar for sampling: nbest\_size = {0,1}: No sampling is performed. (default) nbest\_size > 1: samples from the nbest\_size results. nbest\_size < 0: assuming that nbest\_size is infinite and samples from the all hypothesis (lattice) using forward-filtering-and-backward-sampling algorithm. |
| `alpha` | A scalar for a smoothing parameter. Inverse temperature for probability rescaling. |
| `strip_diacritics` | Whether to strip diacritics or not. Note that stripping diacritics requires additional text normalization and dropping bytes, which makes it impossible to keep track of the offsets now. Hence when `strip_diacritics` is set to True, we don't yet support `tokenize_with_offsets`. NOTE: New models are encouraged to put this into custom normalization rules for the Sentencepiece model itself to avoid this extra step and the limitation regarding offsets. |
| `**kwargs` | standard arguments to `Layer()`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | if importing tensorflow\_text failed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `tokenize_with_offsets` | If true, calls [`SentencepieceTokenizer.tokenize_with_offsets()`](https://www.tensorflow.org/text/api_docs/python/text/SentencepieceTokenizer#tokenize_with_offsets)<br> instead of plain `.tokenize()` and outputs a triple of `(tokens, start_offsets, limit_offsets)`. |
| `vocab_size` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L330-L371)

call(
        inputs: tf.Tensor
    )

Calls [`text.SentencepieceTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/SentencepieceTokenizer)
 on inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A string Tensor of shape `(batch_size,)`. |

|     |     |
| --- | --- |
| Returns |     |
| One or three of RaggedTensors if tokenize\_with\_offsets is False or True, respectively. These are |     |
| `tokens` | A RaggedTensor of shape `[batch_size, (pieces)]` and type `int32`. `tokens[i,j]` contains the j-th piece in the i-th input. start\_offsets, limit\_offsets: If `tokenize_with_offsets` is True, RaggedTensors of type `int64` with the same indices as tokens. Element `[i,j]` contains the byte offset at the start, or past the end, resp., for the j-th piece in the i-th input. |

### `get_special_tokens_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L377-L394)

get_special_tokens_dict()

Returns dict of token ids, keyed by standard names for their purpose.

|     |
| --- |
| Returns |     |
| A dict from Python strings to Python integers. Each key is a standard name for a special token describing its use. (For example, "padding\_id" is what Sentencepiece calls "" but others may call "\[PAD\]".) The corresponding value is the integer token id. If a special token is not found, its entry is omitted from the dict.<br><br>The supported keys and tokens are:<br><br>*   start\_of\_sequence\_id: looked up from "\[CLS\]"<br>*   end\_of\_segment\_id: looked up from "\[SEP\]"<br>*   padding\_id: looked up from ""<br>*   mask\_id: looked up from "\[MASK\]"<br>*   vocab\_size: one past the largest token id used |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.