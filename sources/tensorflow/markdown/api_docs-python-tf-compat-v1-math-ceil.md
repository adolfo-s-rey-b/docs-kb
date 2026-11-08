[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.ceil Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/ceil#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5704-L5729)

Return the ceiling of the input, element-wise.

tf.compat.v1.math.ceil(
        x, name=None
    )

#### For example:

    tf.math.ceil([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. `int32` |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. Has the same type as `x`. |     |

numpy compatibility
-------------------

Equivalent to np.ceil

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.