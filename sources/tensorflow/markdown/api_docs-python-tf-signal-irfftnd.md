[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.irfftnd Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/fft_ops.py#L348-L389)

ND inverse real fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.irfftnd`](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd)

tf.signal.irfftnd(
        input_tensor, fft_length=None, axes=None, norm=None, name=None
    )

Computes the n-dimensional inverse real discrete Fourier transform over designated dimensions of `input_tensor`. The designated dimensions of `input_tensor` are assumed to be the result of `IRFFTND`. The inner-most dimension contains the `fft_length / 2 + 1` unique components of the DFT of a real-valued signal.

If fft\_length\[i\]shape(input)\[i\], the input is padded with zeros. If fft\_length is not given, the default shape(input) is used.

Axes mean the dimensions to perform the transform on. Default is to perform on all axes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor. The FFT length for each dimension. |
| `axes` | A `Tensor` of type `int32`. An int32 tensor with a same shape as fft\_length. Axes to perform the transform. |
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

Last updated 2026-10-31 UTC.