[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.istft Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/istft#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1032-L1097)

Inverse Short-Time Fourier Transform along the last axis of the input.

tf.keras.ops.istft(
        x,
        sequence_length,
        sequence_stride,
        fft_length,
        length=None,
        window='hann',
        center=True
    )

To reconstruct an original waveform, the parameters should be the same in `stft`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type. |
| `sequence_length` | An integer representing the sequence length. |
| `sequence_stride` | An integer representing the sequence hop size. |
| `fft_length` | An integer representing the size of the FFT that produced `stft`. Should be of type `int32`. |
| `length` | An integer representing the output is clipped to exactly length. If not specified, no padding or clipping take place. Defaults to `None`. |
| `window` | A string, a tensor of the window or `None`. If `window` is a string, available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`. |
| `center` | Whether `x` was padded on both sides so that the t-th sequence is centered at time `t * sequence_stride`. Defaults to `True`. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the inverse Short-Time Fourier Transform along the last axis of `x`. |     |

#### Example:

    x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.