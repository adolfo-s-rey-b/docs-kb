[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.threshold Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L880-L906)

Threshold activation function.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.threshold`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/threshold)

tf.keras.ops.threshold(
        x, threshold, default_value
    )

The function thresholds the input `x` as follows: `f(x) = x` if `x > threshold`, `f(x) = default_value` otherwise.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `threshold` | The value that decides when to retain or replace x. |
| `default_value` | Value to assign when `x <= threshold`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with the same shape as `x`. |     |

#### Example:

    x = np.array([-1.0, 0.0, 1.0, 2.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.