[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fcorrelate&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#returns)
    
*   [Notes](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#notes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.correlate Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#returns)
    
*   [Notes](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate#notes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L9443-L9471)

Compute the cross-correlation of two 1-dimensional tensors.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.correlate`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/correlate)

tf.keras.ops.correlate(
        x1, x2, mode='valid'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | First 1-dimensional input tensor of length M. |
| `x2` | Second 1-dimensional input tensor of length N. |
| `mode` | Either `valid`, `same` or `full`. By default the mode is set to `valid`, which returns an output of length max(M, N) - min(M, N) + 1. `same` returns an output of length max(M, N). `full` mode returns the convolution at each point of overlap, with an output length of N+M-1 |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor, cross-correlation of `x1` and `x2`. |     |

|     |
| --- |
| Notes<br>----- |     |
| Complex-valued inputs are currently not fully supported on the TensorFlow and PyTorch backends. When complex tensors are passed, they are cast to floating-point types and the imaginary component is discarded.<br><br>This behavior is documented for clarity and may change in the future. See discussion in issue #21617. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.