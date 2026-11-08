[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.diag Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2602-L2638)

Extract a diagonal or construct a diagonal array.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.diag`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/diag)

tf.keras.ops.diag(
        x, k=0
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. If `x` is 2-D, returns the k-th diagonal of `x`. If `x` is 1-D, return a 2-D tensor with `x` on the k-th diagonal. |
| `k` | The diagonal to consider. Defaults to `0`. Use `k > 0` for diagonals above the main diagonal, and `k < 0` for diagonals below the main diagonal. |

|     |
| --- |
| Returns<br>------- |     |
| The extracted diagonal or constructed diagonal tensor. |     |

#### Examples:

    from keras.src import ops

    ops.diag(x)

    ops.diag(ops.diag(x)))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.