[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Finverse_stft&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.inverse\_stft Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/spectral_ops.py#L160-L279)

Computes the inverse [Short-time Fourier Transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
 of `stfts`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.inverse_stft`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft)

tf.signal.inverse_stft(
        stfts,
        frame_length,
        frame_step,
        fft_length=None,
        window_fn=tf.signal.hann_window,
        name=None
    )

To reconstruct an original waveform, a complementary window function should be used with `inverse_stft`. Such a window function can be constructed with [`tf.signal.inverse_stft_window_fn`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn)
. Example:

frame_length = 400
    frame_step = 160
    waveform = tf.random.normal(dtype=tf.float32, shape=[1000])
    stft = tf.signal.stft(waveform, frame_length, frame_step)
    inverse_stft = tf.signal.inverse_stft(
        stft, frame_length, frame_step,
        window_fn=tf.signal.inverse_stft_window_fn(frame_step))

If a custom `window_fn` is used with [`tf.signal.stft`](https://www.tensorflow.org/api_docs/python/tf/signal/stft)
, it must be passed to [`tf.signal.inverse_stft_window_fn`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn)
:

frame_length = 400
    frame_step = 160
    window_fn = tf.signal.hamming_window
    waveform = tf.random.normal(dtype=tf.float32, shape=[1000])
    stft = tf.signal.stft(
        waveform, frame_length, frame_step, window_fn=window_fn)
    inverse_stft = tf.signal.inverse_stft(
        stft, frame_length, frame_step,
        window_fn=tf.signal.inverse_stft_window_fn(
           frame_step, forward_window_fn=window_fn))

Implemented with TPU/GPU-compatible ops and supports gradients.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `stfts` | A `complex64`/`complex128` `[..., frames, fft_unique_bins]` `Tensor` of STFT bins representing a batch of `fft_length`\-point STFTs where `fft_unique_bins` is `fft_length // 2 + 1` |
| `frame_length` | An integer scalar `Tensor`. The window length in samples. |
| `frame_step` | An integer scalar `Tensor`. The number of samples to step. |
| `fft_length` | An integer scalar `Tensor`. The size of the FFT that produced `stfts`. If not provided, uses the smallest power of 2 enclosing `frame_length`. |
| `window_fn` | A callable that takes a window length and a `dtype` keyword argument and returns a `[window_length]` `Tensor` of samples in the provided datatype. If set to `None`, no windowing is used. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., samples]` `Tensor` of `float32`/`float64` signals representing the inverse STFT for each input STFT in `stfts`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `stfts` is not at least rank 2, `frame_length` is not scalar, `frame_step` is not scalar, or `fft_length` is not scalar. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.