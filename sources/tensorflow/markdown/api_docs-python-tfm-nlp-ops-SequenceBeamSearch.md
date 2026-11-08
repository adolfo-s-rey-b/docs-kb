[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#methods)
    *   [search](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#search)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.ops.SequenceBeamSearch Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#methods)
    *   [search](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SequenceBeamSearch#search)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/beam_search.py#L102-L635)

Implementation of beam search loop.

tfm.nlp.ops.SequenceBeamSearch(
        symbols_to_logits_fn,
        vocab_size,
        beam_size,
        alpha,
        max_decode_length,
        eos_id,
        padded_decode,
        dtype=tf.float32,
        noise_multiplier: float = 0.0,
        decoding_name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `symbols_to_logits_fn` | A function to provide logits, which is the interface to the Transformer model. The passed in arguments are: ids -> A tensor with shape \[batch\_size \* beam\_size, index\]. index -> A scalar. cache -> A nested dictionary of tensors \[batch\_size \* beam\_size, ...\]. The function must return a tuple of logits and the updated cache: logits -> A tensor with shape \[batch \* beam\_size, vocab\_size\]. updated cache -> A nested dictionary with the same structure as the input cache. |
| `vocab_size` | An integer, the size of the vocabulary, used for topk computation. |
| `beam_size` | An integer, number of beams for beam search. |
| `alpha` | A float, defining the strength of length normalization. |
| `max_decode_length` | An integer, the maximum number of steps to decode a sequence. |
| `eos_id` | An integer or a list. ID of end of sentence token. |
| `padded_decode` | A bool, indicating if max\_sequence\_length padding is used for beam search. |
| `dtype` | A tensorflow data type used for score computation. The default is tf.float32. |
| `noise_multiplier` | The amount of noise. |
| `decoding_name` | an optional name for the decoding loop tensors. |

Methods
-------

### `search`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/beam_search.py#L156-L424)

search(
        initial_ids, initial_cache, constraint_mask=None
    )

Beam search for sequences with highest scores.

|     |     |
| --- | --- |
| Args |     |
| `initial_ids` | initial ids to pass into the symbols\_to\_logits\_fn. int tensor with shape \[batch\_size, 1\] |
| `initial_cache` | dictionary storing values to be passed into the symbols\_to\_logits\_fn. |
| `constraint_mask` | a \[vocab\_size\] tensor, with 1 represent prefix. During autoregressive decoding, the first token should be among where the constraint\_mask is 1. |

|     |
| --- |
| Returns |     |
| finished\_seq and finished\_scores. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.