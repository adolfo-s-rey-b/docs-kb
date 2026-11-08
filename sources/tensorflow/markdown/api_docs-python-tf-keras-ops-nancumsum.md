[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.nancumsum Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L5768-L5796)

Returns the cumulative sum of elements along a given axis, treating NaNs as zero.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.nancumsum`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/nancumsum)

tf.keras.ops.nancumsum(
        x, axis=None, dtype=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Axis along which the cumulative sum is computed. By default the input is flattened. |
| `dtype` | dtype of returned tensor. Defaults to x.dtype. |

|     |
| --- |
| Returns<br>------- |     |
| Output tensor. |     |

#### Examples:

    import numpy as np

    ops.nancumsum(x, axis=1)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.