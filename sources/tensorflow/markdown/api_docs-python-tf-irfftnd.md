[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/irfftnd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/irfftnd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/irfftnd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Firfftnd&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/irfftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/irfftnd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.irfftnd Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/irfftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/irfftnd#returns)
    

ND inverse real fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.irfftnd`](https://www.tensorflow.org/api_docs/python/tf/irfftnd)

tf.irfftnd(
        input: Annotated[Any, TV_IRFFTND_Tcomplex],
        fft_length: Annotated[Any, _atypes.Int32],
        axes: Annotated[Any, _atypes.Int32],
        Treal: TV_IRFFTND_Treal = tf.dtypes.float32,
        name=None
    ) -> Annotated[Any, TV_IRFFTND_Treal]

Computes the n-dimensional inverse real discrete Fourier transform over designated dimensions of `input`. The designated dimensions of `input` are assumed to be the result of `IRFFTND`. The inner-most dimension contains the `fft_length / 2 + 1` unique components of the DFT of a real-valued signal.

If fft\_length\[i\]shape(input)\[i\], the input is padded with zeros. If fft\_length is not given, the default shape(input) is used.

Axes mean the dimensions to perform the transform on. Default is to perform on all axes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor. The FFT length for each dimension. |
| `axes` | A `Tensor` of type `int32`. An int32 tensor with a same shape as fft\_length. Axes to perform the transform. |
| `Treal` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.float32, tf.float64`. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `Treal`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.