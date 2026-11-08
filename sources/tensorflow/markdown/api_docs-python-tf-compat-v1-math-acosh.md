[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/acosh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.acosh Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

Computes inverse hyperbolic cosine of x element-wise.

tf.compat.v1.math.acosh(
        x: Annotated[Any, TV_Acosh_T], name=None
    ) -> Annotated[Any, TV_Acosh_T]

Given an input tensor, the function computes inverse hyperbolic cosine of every element. Input range is `[1, inf]`. It returns `nan` if the input lies outside the range.

x = tf.constant([-2, -0.5, 1, 1.2, 200, 10000, float("inf")])
    tf.math.acosh(x) ==> [nan nan 0. 0.62236255 5.9914584 9.903487 inf]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.