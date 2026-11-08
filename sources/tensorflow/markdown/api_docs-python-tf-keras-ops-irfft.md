[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.irfft Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/irfft#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L814-L855)

Inverse real-valued Fast Fourier transform along the last axis.

tf.keras.ops.irfft(
        x, fft_length=None
    )

Computes the inverse 1D Discrete Fourier Transform of a real-valued signal over the inner-most dimension of input.

The inner-most dimension of the input is assumed to be the result of RFFT: the `fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If `fft_length` is not provided, it is computed from the size of the inner-most dimension of the input `(fft_length = 2 * (inner - 1))`. If the FFT length used to compute is odd, it should be provided since it cannot be inferred properly.

Along the axis IRFFT is computed on, if `fft_length / 2 + 1` is smaller than the corresponding dimension of the input, the dimension is cropped. If it is larger, the dimension is padded with zeros.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type. |
| `fft_length` | An integer representing the number of the fft length. If not specified, it is inferred from the length of the last axis of `x`. Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the inverse real-valued Fast Fourier Transform along the last axis of `x`. |     |

#### Examples:

    real = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0])

    irfft(rfft(real, 5), 5)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.