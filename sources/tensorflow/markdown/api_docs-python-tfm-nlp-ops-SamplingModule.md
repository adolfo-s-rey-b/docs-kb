[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#methods)
    *   [generate](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#generate)
        
    *   [inf](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#inf)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.ops.SamplingModule Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#methods)
    *   [generate](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#generate)
        
    *   [inf](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/SamplingModule#inf)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/sampling_module.py#L150-L473)

Implementation for sampling strategies (go/decoding-tf-nlp).

tfm.nlp.ops.SamplingModule(
        symbols_to_logits_fn,
        vocab_size: int,
        max_decode_length: int,
        eos_id: int,
        padded_decode: bool,
        length_normalization_fn: Optional[Callable[[int, tf.DType], float]] = None,
        top_k=0,
        top_p=1.0,
        sample_temperature=0.0,
        enable_greedy: bool = True,
        dtype: tf.DType = tf.float32,
        decoding_name: Optional[str] = None,
        extra_cache_output: bool = False
    )

Methods
-------

### `generate`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/decoding_module.py#L132-L200)

generate(
        initial_ids: tf.Tensor,
        initial_cache: Dict[str, tf.Tensor],
        initial_log_probs: Optional[tf.Tensor] = None
    ) -> Output

Implements the decoding strategy (beam\_search or sampling).

|     |     |
| --- | --- |
| Args |     |
| `initial_ids` | initial ids to pass into the symbols\_to\_logits\_fn. int tensor with shape \[batch\_size, 1\] |
| `initial_cache` | dictionary for caching model outputs from previous step. |
| `initial_log_probs` | Optionally initial log probs if there is a prefix sequence we want to start to decode from. |

|     |
| --- |
| Returns |     |
| Tuple of tensors representing finished\_sequence: shape \[batch, max\_seq\_length\] finished\_scores: \[batch\] first\_cache: The cache after init token |     |

### `inf`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/decoding_module.py#L293-L307)

inf()

Returns a value close to infinity, but is still finite in `dtype`.

This is useful to get a very large value that is still zero when multiplied by zero. The floating-point "Inf" value is NaN when multiplied by zero.

|     |
| --- |
| Returns |     |
| A very large value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.