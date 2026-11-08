[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Finverse_mdct&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.inverse\_mdct Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/spectral_ops.py#L372-L454)

Computes the inverse modified DCT of `mdcts`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.inverse_mdct`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct)

tf.signal.inverse_mdct(
        mdcts,
        window_fn=tf.signal.vorbis_window,
        norm=None,
        name=None
    )

To reconstruct an original waveform, the same window function should be used with `mdct` and `inverse_mdct`.

#### Example usage:

    @tf.function

Implemented with TPU/GPU-compatible ops and supports gradients.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mdcts` | A `float32`/`float64` `[..., frames, frame_length // 2]` `Tensor` of MDCT bins representing a batch of `frame_length // 2`\-point MDCTs. |
| `window_fn` | A callable that takes a frame\_length and a `dtype` keyword argument and returns a `[frame_length]` `Tensor` of samples in the provided datatype. If set to `None`, a rectangular window with a scale of 1/sqrt(2) is used. For perfect reconstruction of a signal from `mdct` followed by `inverse_mdct`, please use [`tf.signal.vorbis_window`](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window)<br>, [`tf.signal.kaiser_bessel_derived_window`](https://www.tensorflow.org/api_docs/python/tf/signal/kaiser_bessel_derived_window)<br> or `None`. If using another window function, make sure that w\[n\]^2 + w\[n + frame\_length // 2\]^2 = 1 and w\[n\] = w\[frame\_length - n - 1\] for n = 0,...,frame\_length // 2 - 1 to achieve perfect reconstruction. |
| `norm` | If "ortho", orthonormal inverse DCT4 is performed, if it is None, a regular dct4 followed by scaling of `1/frame_length` is performed. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., samples]` `Tensor` of `float32`/`float64` signals representing the inverse MDCT for each input MDCT in `mdcts` where `samples` is `(frames - 1) * (frame_length // 2) + frame_length`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `mdcts` is not at least rank 2. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.