[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.cross Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#note)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L2346-L2392)

Returns the cross product of two (arrays of) vectors.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.cross`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cross)

tf.keras.ops.cross(
        x1, x2, axisa=-1, axisb=-1, axisc=-1, axis=None
    )

The cross product of `x1` and `x2` in R^3 is a vector perpendicular to both `x1` and `x2`. If `x1` and `x2` are arrays of vectors, the vectors are defined by the last axis of `x1` and `x2` by default, and these axes can have dimensions 2 or 3.

Where the dimension of either `x1` or `x2` is 2, the third component of the input vector is assumed to be zero and the cross product calculated accordingly.

In cases where both input vectors have dimension 2, the z-component of the cross product is returned.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x1` | Components of the first vector(s). |
| `x2` | Components of the second vector(s). |
| `axisa` | Axis of `x1` that defines the vector(s). Defaults to `-1`. |
| `axisb` | Axis of `x2` that defines the vector(s). Defaults to `-1`. |
| `axisc` | Axis of the result containing the cross product vector(s). Ignored if both input vectors have dimension 2, as the return is scalar. By default, the last axis. |
| `axis` | If defined, the axis of `x1`, `x2` and the result that defines the vector(s) and cross product(s). Overrides `axisa`, `axisb` and `axisc`. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend does not support two dimensional vectors, or the arguments `axisa`, `axisb` and `axisc`. Use `axis` instead. |     |

|     |
| --- |
| Returns<br>------- |     |
| Vector cross product(s). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.