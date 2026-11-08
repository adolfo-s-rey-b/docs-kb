[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#methods)
    *   [bert\_pack\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#bert_pack_inputs)
        
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.BertPackInputs Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#methods)
    *   [bert\_pack\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#bert_pack_inputs)
        
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/BertPackInputs#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L440-L602)

Packs tokens into model inputs for BERT.

tfm.nlp.layers.BertPackInputs(
        seq_length,
        *,
        start_of_sequence_id=None,
        end_of_segment_id=None,
        padding_id=None,
        special_tokens_dict=None,
        truncator='round_robin',
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seq_length` | The desired output length. Must not exceed the max\_seq\_length that was fixed at training time for the BERT model receiving the inputs. |
| `start_of_sequence_id` | The numeric id of the token that is to be placed at the start of each sequence (called "\[CLS\]" for BERT). |
| `end_of_segment_id` | The numeric id of the token that is to be placed at the end of each input segment (called "\[SEP\]" for BERT). |
| `padding_id` | The numeric id of the token that is to be placed into the unused positions after the last segment in the sequence (called "\[PAD\]" for BERT). |
| `special_tokens_dict` | Optionally, a dict from Python strings to Python integers that contains values for `start_of_sequence_id`, `end_of_segment_id` and `padding_id`. (Further values in the dict are silenty ignored.) If this is passed, separate _\_id arguments must be omitted._ |
| `truncator` | The algorithm to truncate a list of batched segments to fit a per-example length limit. The value can be either `round_robin` or `waterfall`: (1) For "round\_robin" algorithm, available space is assigned one token at a time in a round-robin fashion to the inputs that still need some, until the limit is reached. It currently only supports one or two segments. (2) For "waterfall" algorithm, the allocation of the budget is done using a "waterfall" algorithm that allocates quota in a left-to-right manner and fills up the buckets until we run out of budget. It support arbitrary number of segments. |
| `**kwargs`<a id="\*kwargs"> | standard arguments to `Layer()`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | if importing `tensorflow_text` failed. |

Methods
-------

### `bert_pack_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L551-L602)

@staticmethod

Freestanding equivalent of the BertPackInputs layer.

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/text_layers.py#L532-L549)

call(
        inputs: Union[tf.RaggedTensor, List[tf.RaggedTensor]]
    )

Adds special tokens to pack a list of segments into BERT input Tensors.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A Python list of one or two RaggedTensors, each with the batched values one input segment. The j-th segment of the i-th input example consists of slice `inputs[j][i, ...]`. |

|     |
| --- |
| Returns |     |
| A nest of Tensors for use as input to the BERT TransformerEncoder. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.