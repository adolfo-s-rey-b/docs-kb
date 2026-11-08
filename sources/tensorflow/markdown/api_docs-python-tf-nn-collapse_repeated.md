[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fcollapse_repeated&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.collapse\_repeated Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L1172-L1233)

Merge repeated labels into single labels.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.collapse_repeated`](https://www.tensorflow.org/api_docs/python/tf/nn/collapse_repeated)

tf.nn.collapse_repeated(
        labels, seq_length, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | Tensor of shape \[batch, max value in seq\_length\] |
| `seq_length` | Tensor of shape \[batch\], sequence length of each batch element. |
| `name` | A name for this `Op`. Defaults to "collapse\_repeated\_labels". |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple `(collapsed_labels, new_seq_length)` where |     |
| `collapsed_labels` | Tensor of shape \[batch, max\_seq\_length\] with repeated labels collapsed and padded to max\_seq\_length, eg: `[[A, A, B, B, A], [A, B, C, D, E]] => [[A, B, A, 0, 0], [A, B, C, D, E]]` |
| `new_seq_length` | int tensor of shape \[batch\] with new sequence lengths. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.