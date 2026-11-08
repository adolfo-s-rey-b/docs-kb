[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/rfft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Frfft&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.rfft Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/rfft#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/fft_ops.py#L140-L166)

Real-valued fast Fourier transform.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.rfft`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)
, [`tf.compat.v1.spectral.rfft`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)

tf.signal.rfft(
        input_tensor, fft_length=None, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series) |

Computes the 1-dimensional discrete Fourier transform of a real-valued signal over the inner-most dimension of `input`.

Since the DFT of a real signal is Hermitian-symmetric, `RFFT` only returns the `fft_length / 2 + 1` unique components of the FFT: the zero-frequency term, followed by the `fft_length / 2` positive-frequency terms.

Along the axis `RFFT` is computed on, if `fft_length` is smaller than the corresponding dimension of `input`, the dimension is cropped. If it is larger, the dimension is padded with zeros.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`. A float32 or float64 tensor. |
| `fft_length` | A `Tensor` of type `int32`. An int32 tensor of shape \[1\]. The FFT length. Should be [`tf.complex64`](https://www.tensorflow.org/api_docs/python/tf#complex64)<br> when the type of `input` is `float32`. Should be [`tf.complex128`](https://www.tensorflow.org/api_docs/python/tf#complex128)<br> when the type of `input` is `float64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `Tcomplex`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.