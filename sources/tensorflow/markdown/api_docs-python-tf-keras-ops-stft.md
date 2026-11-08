[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fstft&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.stft Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/stft#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L903-L962)

Short-Time Fourier Transform along the last axis of the input.

tf.keras.ops.stft(
        x,
        sequence_length,
        sequence_stride,
        fft_length,
        window='hann',
        center=True
    )

The STFT computes the Fourier transform of short overlapping windows of the input. This giving frequency components of the signal as they change over time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. |
| `sequence_length` | An integer representing the sequence length. |
| `sequence_stride` | An integer representing the sequence hop size. |
| `fft_length` | An integer representing the size of the FFT to apply. If not specified, uses the smallest power of 2 enclosing `sequence_length`. |
| `window` | A string, a tensor of the window or `None`. If `window` is a string, available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`. |
| `center` | Whether to pad `x` on both sides so that the t-th sequence is centered at time `t * sequence_stride`. Otherwise, the t-th sequence begins at time `t * sequence_stride`. Defaults to `True`. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple containing two tensors - the real and imaginary parts of the STFT output. |     |

#### Example:

    x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.