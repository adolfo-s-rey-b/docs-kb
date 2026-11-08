[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.average Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L1341-L1396)

Compute the weighted average along the specified axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.average`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/average)

tf.keras.ops.average(
        x, axis=None, weights=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Integer along which to average `x`. The default, `axis=None`, will average over all of the elements of the input tensor. If axis is negative it counts from the last to the first axis. |
| `weights` | Tensor of weights associated with the values in `x`. Each value in `x` contributes to the average according to its associated weight. The weights array can either be 1-D (in which case its length must be the size of a along the given axis) or of the same shape as `x`. If `weights=None` (default), then all data in `x` are assumed to have a weight equal to one.<br><br>The 1-D calculation is: `avg = sum(a * weights) / sum(weights)`. The only constraint on weights is that `sum(weights)` must not be 0. |

|     |
| --- |
| Returns<br>------- |     |
| Return the average along the specified axis. |     |

#### Examples:

    data = keras.ops.arange(1, 5)

    data = keras.ops.arange(6).reshape((3, 2))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.