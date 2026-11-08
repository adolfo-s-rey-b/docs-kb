[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/ifft2d#main-content)

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
    

tf.signal.ifft2d Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

Inverse 2D fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ifft2d`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft2d)
, [`tf.compat.v1.signal.ifft2d`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft2d)
, [`tf.compat.v1.spectral.ifft2d`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft2d)

tf.signal.ifft2d(
        input: Annotated[Any, TV_IFFT2D_Tcomplex], name=None
    ) -> Annotated[Any, TV_IFFT2D_Tcomplex]

Computes the inverse 2-dimensional discrete Fourier transform over the inner-most 2 dimensions of `input`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.