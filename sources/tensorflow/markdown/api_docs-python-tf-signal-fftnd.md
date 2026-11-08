[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Ffftnd&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.fftnd Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/fft_ops.py#L211-L241)

ND fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.fftnd`](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd)

tf.signal.fftnd(
        input_tensor, fft_length=None, axes=None, norm=None, name=None
    )

Computes the n-dimensional discrete Fourier transform over designated dimensions of `input`. The designated dimensions of `input` are assumed to be the result of `FFTND`.

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
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.