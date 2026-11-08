[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fctc_unique_labels&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.ctc\_unique\_labels Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Example](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ctc_ops.py#L1270-L1303)

Get unique labels and indices for batched labels for [`tf.nn.ctc_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.ctc_unique_labels`](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_unique_labels)

tf.nn.ctc_unique_labels(
        labels, name=None
    )

For use with [`tf.nn.ctc_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/ctc_loss)
 optional argument `unique`: This op can be used to preprocess labels in input pipeline to for better speed/memory use computing the ctc loss on TPU.

|     |
| --- |
| Example<br>------- |     |
| ctc\_unique\_labels(\[\[3, 4, 4, 3\]\]) -> unique labels padded with 0: \[\[3, 4, 0, 0\]\] indices of original labels in unique: \[0, 1, 1, 0\] |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | tensor of shape \[batch\_size, max\_label\_length\] padded with 0. |
| `name` | A name for this `Op`. Defaults to "ctc\_unique\_labels". |

|     |
| --- |
| Returns<br>------- |     |
| tuple of<br><br>*   unique labels, tensor of shape `[batch_size, max_label_length]`<br>*   indices into unique labels, shape `[batch_size, max_label_length]` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.