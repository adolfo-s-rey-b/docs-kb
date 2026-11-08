[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.imag Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/imag#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L863-L894)

Returns the imaginary part of a complex (or real) tensor.

tf.compat.v1.math.imag(
        input, name=None
    )

Given a tensor `input`, this operation returns a tensor of type `float` that is the imaginary part of each element in `input` considered as a complex number. If `input` is real, a tensor of all zeros is returned.

#### For example:

x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
    tf.math.imag(x)  # [4.75, 5.75]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float`, `double`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float32` or `float64`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.