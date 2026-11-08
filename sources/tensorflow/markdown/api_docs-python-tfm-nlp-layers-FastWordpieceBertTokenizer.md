[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FFastWordpieceBertTokenizer&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#get_special_tokens_dict)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.FastWordpieceBertTokenizer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#call)
        
    *   [get\_special\_tokens\_dict](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FastWordpieceBertTokenizer#get_special_tokens_dict)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L605-L738)

A bert tokenizer keras layer using text.FastWordpieceTokenizer.

tfm.nlp.layers.FastWordpieceBertTokenizer(
        *,
        vocab_file: str,
        lower_case: bool,
        tokenize_with_offsets: bool = False,
        **kwargs
    )

See details: "Fast WordPiece Tokenization" ([https://arxiv.org/abs/2012.15524](https://arxiv.org/abs/2012.15524)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_file` | A Python string with the path of the vocabulary file. This is a text file with newline-separated wordpiece tokens. This layer loads a list of tokens from it to create text.FastWordpieceTokenizer. |
| `lower_case` | A Python boolean forwarded to text.BasicTokenizer. If true, input text is converted to lower case (where applicable) before tokenization. This must be set to match the way in which the vocab\_file was created. |
| `tokenize_with_offsets` | A Python boolean. If true, this layer calls FastWordpieceTokenizer.tokenize\_with\_offsets() instead of plain .tokenize() and outputs a triple of (tokens, start\_offsets, limit\_offsets) insead of just tokens. |
| `**kwargs` | standard arguments to Layer(). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `vocab_size` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L707-L738)

call(
        inputs: tf.Tensor
    )

Calls text.BertTokenizer on inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A string Tensor of shape \[batch\_size\]. |

|     |     |
| --- | --- |
| Returns |     |
| One or three of RaggedTensors if tokenize\_with\_offsets is False or True, respectively. These are |     |
| `tokens` | A RaggedTensor of shape \[batch\_size, (words), (pieces\_per\_word)\] and type int32. tokens\[i,j,k\] contains the k-th wordpiece of the j-th word in the i-th input. start\_offsets, limit\_offsets: If tokenize\_with\_offsets is True, RaggedTensors of type int64 with the same indices as tokens. Element \[i,j,k\] contains the byte offset at the start, or past the end, resp., for the k-th wordpiece of the j-th word in the i-th input. |

### `get_special_tokens_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L655-L672)

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