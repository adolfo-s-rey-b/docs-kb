[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.ptp Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6988-L7032)

Return the peak-to-peak (max - min) value of tensor elements over a given axis.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.ptp`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ptp)

tf.keras.ops.ptp(
        x, axis=None, keepdims=False
    )

The peak-to-peak value is defined as the difference between the maximum and minimum values along the specified axis.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `axis` | Axis or axes along which the peak-to-peak value is computed. The default, `axis=None`, will compute the peak-to-peak value over all elements in the input tensor. |
| `keepdims` | If this is set to `True`, the axes which are reduced are left in the result as dimensions with size one. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the peak-to-peak values of `x` over the given axis or axes. |     |

#### Examples:

    x = keras.ops.array([[1., 3., 2.],\
\
    # Peak-to-peak over all elements\
\
    # Peak-to-peak along axis 1\
\
    # Peak-to-peak over multiple axes\
\
    # Keep reduced dimensions\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.