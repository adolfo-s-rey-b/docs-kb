[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Firfft2d&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.irfft2d Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/fft_ops.py#L175-L197)

Inverse 2D real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.irfft2d`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d)
, [`tf.compat.v1.spectral.irfft2d`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d)

tf.signal.irfft2d(
        input_tensor, fft_length=None, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

Computes the inverse 2-dimensional discrete Fourier transform of a real-valued signal over the inner-most 2 dimensions of `input_tensor`.

The inner-most 2 dimensions of `input_tensor` are assumed to be the result of `RFFT2D`: The inner-most dimension contains the `fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If `fft_length` is not provided, it is computed from the size of the inner-most 2 dimensions of `input_tensor`. If the FFT length used to compute `input_tensor` is odd, it should be provided since it cannot be inferred properly.

Along each axis `IRFFT2D` is computed on, if `fft_length` (or `fft_length / 2 + 1` for the inner-most dimension) is smaller than the corresponding dimension of `input_tensor`, the dimension is cropped. If it is larger, the dimension is padded with zeros.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. A complex tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape \[2\]. The FFT length for each dimension. |
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