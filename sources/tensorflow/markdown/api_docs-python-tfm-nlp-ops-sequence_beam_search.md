[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.ops.sequence\_beam\_search Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/sequence_beam_search#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/beam_search.py#L638-L698)

Search for sequence of subtoken ids with the largest probability.

tfm.nlp.ops.sequence_beam_search(
        symbols_to_logits_fn,
        initial_ids,
        initial_cache,
        vocab_size,
        beam_size,
        alpha,
        max_decode_length,
        eos_id,
        padded_decode=False,
        dtype='float32',
        noise_multiplier: float = 0.0,
        decoding_name=None,
        constraint_mask=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `symbols_to_logits_fn` | A function that takes in ids, index, and cache as arguments. The passed in arguments will have shape: ids -> A tensor with shape \[batch\_size \* beam\_size, index\]. index -> A scalar. cache -> A nested dictionary of tensors \[batch\_size \* beam\_size, ...\]. The function must return a tuple of logits and new cache: logits -> A tensor with shape \[batch \* beam\_size, vocab\_size\]. new cache -> A nested dictionary with the same shape/structure as the inputted cache. |
| `initial_ids` | An int32 tensor with shape \[batch\_size\]. Starting ids for each batch item. |
| `initial_cache` | A dictionary, containing starting decoder variables information. |
| `vocab_size` | An integer, the size of tokens. |
| `beam_size` | An integer, the number of beams. |
| `alpha` | A float, defining the strength of length normalization. |
| `max_decode_length` | An integer, the maximum length to decoded a sequence. |
| `eos_id` | An integer, ID of eos token, used to determine when a sequence has finished. |
| `padded_decode` | A bool, indicating if max\_sequence\_length padding is used for beam search. |
| `dtype` | A tensorflow data type used for score computation. The default is tf.float32. |
| `noise_multiplier` | The amount of noise. |
| `decoding_name` | an optional name for the decoding loop tensors. |
| `constraint_mask` | The BS will only constraint the next token to where the mask is 1. |

|     |
| --- |
| Returns<br>------- |     |
| Top decoded sequences \[batch\_size, beam\_size, max\_decode\_length\] sequence scores \[batch\_size, beam\_size\] |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.