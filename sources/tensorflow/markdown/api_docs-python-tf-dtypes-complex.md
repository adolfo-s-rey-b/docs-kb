[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdtypes%2Fcomplex&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dtypes.complex Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L727-L772)

Converts two real numbers to a complex number.

#### View aliases

**Main aliases**

[`tf.complex`](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.complex`](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex)
, [`tf.compat.v1.dtypes.complex`](https://www.tensorflow.org/api_docs/python/tf/dtypes/complex)

tf.dtypes.complex(
        real, imag, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

Given a tensor `real` representing the real part of a complex number, and a tensor `imag` representing the imaginary part of a complex number, this operation returns complex numbers elementwise of the form a+bj, where _a_ represents the `real` part and _b_ represents the `imag` part.

The input tensors `real` and `imag` must have the same shape.

#### For example:

real = tf.constant([2.25, 3.25])
    imag = tf.constant([4.75, 5.75])
    tf.complex(real, imag)  # [[2.25 + 4.75j], [3.25 + 5.75j]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `real` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `imag` | A `Tensor`. Must have the same type as `real`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `complex64` or `complex128`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | Real and imag must be correct types |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.