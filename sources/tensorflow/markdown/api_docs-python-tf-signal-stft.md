[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/stft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/stft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/stft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/stft#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/stft#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/stft#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.stft Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/signal/stft#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/stft#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/stft#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/spectral_ops.py#L34-L92)

Computes the [Short-time Fourier Transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
 of `signals`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.stft`](https://www.tensorflow.org/api_docs/python/tf/signal/stft)

tf.signal.stft(
        signals,
        frame_length,
        frame_step,
        fft_length=None,
        window_fn=tf.signal.hann_window,
        pad_end=False,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio) |

Implemented with TPU/GPU-compatible ops and supports gradients.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `signals` | A `[..., samples]` `float32`/`float64` `Tensor` of real-valued signals. |
| `frame_length` | An integer scalar `Tensor`. The window length in samples. |
| `frame_step` | An integer scalar `Tensor`. The number of samples to step. |
| `fft_length` | An integer scalar `Tensor`. The size of the FFT to apply. If not provided, uses the smallest power of 2 enclosing `frame_length`. |
| `window_fn` | A callable that takes a window length and a `dtype` keyword argument and returns a `[window_length]` `Tensor` of samples in the provided datatype. If set to `None`, no windowing is used. |
| `pad_end` | Whether to pad the end of `signals` with zeros when the provided frame length and step produces a frame that lies partially past its end. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., frames, fft_unique_bins]` `Tensor` of `complex64`/`complex128` STFT values where `fft_unique_bins` is `fft_length // 2 + 1` (the unique components of the FFT). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `signals` is not at least rank 1, `frame_length` is not scalar, or `frame_step` is not scalar. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.