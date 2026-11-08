[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fpsnr&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.psnr Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2760-L2808)

Peak Signal-to-Noise Ratio (PSNR) function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.psnr`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/psnr)

tf.keras.ops.psnr(
        x1, x2, max_val
    )

This function computes the Peak Signal-to-Noise Ratio between two signals, `x1` and `x2`. PSNR is a measure of the quality of a reconstructed signal. The higher the PSNR, the closer the reconstructed signal is to the original signal. Note that it can become negative when the signal power is smaller that the noise power.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | The first input signal. |
| `x2` | The second input signal. Must have the same shape as `x1`. |
| `max_val` | The maximum possible value in the signals. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `float` | The PSNR value between `x1` and `x2`. |

#### Examples:

    x1 = keras.random.normal((2, 4, 4, 3))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.