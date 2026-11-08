[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.rot90 Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L50-L87)

Rotate an array by 90 degrees in the plane specified by axes.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.rot90`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/rot90)

tf.keras.ops.rot90(
        array, k=1, axes=(0, 1)
    )

This function rotates an array counterclockwise by 90 degrees `k` times in the plane specified by `axes`. Supports arrays of two or more dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `array` | Input array to rotate. |
| `k` | Number of times the array is rotated by 90 degrees. |
| `axes` | A tuple of two integers specifying the plane of rotation (defaults to `(0, 1)`). |

|     |
| --- |
| Returns<br>------- |     |
| Rotated array. |     |

#### Examples:

    import numpy as np

    m = np.arange(8).reshape((2, 2, 2))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.