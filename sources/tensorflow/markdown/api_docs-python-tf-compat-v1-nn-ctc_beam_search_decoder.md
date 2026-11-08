[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.ctc\_beam\_search\_decoder Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/ctc_beam_search_decoder#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L380-L443)

Performs beam search decoding on the logits given in input.

tf.compat.v1.nn.ctc_beam_search_decoder(
        inputs, sequence_length, beam_width=100, top_paths=1, merge_repeated=True
    )

*   `ctc_beam_search_decoder` treats blanks as sequence termination
*   `ctc_greedy_decoder` treats blanks as regular elements

If `merge_repeated` is `True`, merge repeated classes in the output beams. This means that if consecutive entries in a beam are the same, only the first of these is emitted. That is, when the sequence is `A B B * B * B` (where '\*' is the blank label), the return value is:

*   `A B` if `merge_repeated = True`.
*   `A B B B` if `merge_repeated = False`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | 3-D `float` `Tensor`, size `[max_time x batch_size x num_classes]`. The logits. |
| `sequence_length` | 1-D `int32` vector containing sequence lengths, having size `[batch_size]`. |
| `beam_width` | An int scalar >= 0 (beam search beam width). |
| `top_paths` | An int scalar >= 0, <= beam\_width (controls output size). |
| `merge_repeated` | Boolean. Default: True. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple `(decoded, log_probabilities)` where |     |
| `decoded` | A list of length top\_paths, where `decoded[j]` is a `SparseTensor` containing the decoded outputs:<br><br>`decoded[j].indices`: Indices matrix `(total_decoded_outputs[j] x 2)` The rows store: \[batch, time\].<br><br>`decoded[j].values`: Values vector, size `(total_decoded_outputs[j])`. The vector stores the decoded classes for beam j.<br><br>`decoded[j].dense_shape`: Shape vector, size `(2)`. The shape values are: `[batch_size, max_decoded_length[j]]`. |
| `log_probability` | A `float` matrix `(batch_size x top_paths)` containing sequence log-probabilities. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.