[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fctc_greedy_decoder&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.ctc\_greedy\_decoder Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L297-L377)

Performs greedy decoding on the logits given in input (best path).

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.ctc_greedy_decoder`](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_greedy_decoder)

tf.nn.ctc_greedy_decoder(
        inputs, sequence_length, merge_repeated=True, blank_index=None
    )

Given a tensor as `inputs`, the `blank_index` parameter defines the class index of the blank symbol.

#### For example:

If `blank_index` is equal to 1:

    inf = float("inf")

#### Notes:

*   Unlike `ctc_beam_search_decoder`, `ctc_greedy_decoder` considers blanks as regular elements when computing the probability of a sequence.
*   Default `blank_index` is `(num_classes - 1)`, unless overridden.

If `merge_repeated` is `True`, merge repeated classes in output. This means that if consecutive logits' maximum indices are the same, only the first of these is emitted. The sequence `A B B * B * B` (where '\*' is the blank label) becomes

*   `A B B B` if `merge_repeated=True`.
*   `A B B B B` if `merge_repeated=False`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | 3-D `float` `Tensor` sized `[max_time, batch_size, num_classes]`. The logits. |
| `sequence_length` | 1-D `int32` vector containing sequence lengths, having size `[batch_size]`. |
| `merge_repeated` | Boolean. Default: True. |
| `blank_index` | (Optional). Default: `num_classes - 1`. Define the class index to use for the blank label. Negative values will start from num\_classes, ie, -1 will reproduce the ctc\_greedy\_decoder behavior of using num\_classes<br><br>*   1 for the blank symbol, which corresponds to the default. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple `(decoded, neg_sum_logits)` where |     |
| `decoded` | A single-element list. `decoded[0]` is an `SparseTensor` containing the decoded outputs s.t.:<br><br>`decoded.indices`: Indices matrix `(total_decoded_outputs, 2)`. The rows store: `[batch, time]`.<br><br>`decoded.values`: Values vector, size `(total_decoded_outputs)`. The vector stores the decoded classes.<br><br>`decoded.dense_shape`: Shape vector, size `(2)`. The shape values are: `[batch_size, max_decoded_length]` |
| `neg_sum_logits` | A `float` matrix `(batch_size x 1)` containing, for the sequence found, the negative of the sum of the greatest logit at each timeframe. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.