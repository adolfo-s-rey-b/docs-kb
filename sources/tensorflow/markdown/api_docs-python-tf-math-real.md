[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/real#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/real)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/real?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/real#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/real#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/real#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.real Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/real#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/real#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/real#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L822-L860)

Returns the real part of a complex (or real) tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.real`](https://www.tensorflow.org/api_docs/python/tf/math/real)

tf.math.real(
        input, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data) |

Given a tensor `input`, this operation returns a tensor of type `float` that is the real part of each element in `input` considered as a complex number.

#### For example:

x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
    tf.math.real(x)  # [-2.25, 3.25]

If `input` is already real, it is returned unchanged.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must have numeric type. |
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