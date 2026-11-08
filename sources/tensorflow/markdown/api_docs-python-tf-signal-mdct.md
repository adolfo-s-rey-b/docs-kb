[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/mdct)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/mdct?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsignal%2Fmdct&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.mdct Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/mdct#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/spectral_ops.py#L296-L369)

Computes the [Modified Discrete Cosine Transform](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform)
 of `signals`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.mdct`](https://www.tensorflow.org/api_docs/python/tf/signal/mdct)

tf.signal.mdct(
        signals,
        frame_length,
        window_fn=tf.signal.vorbis_window,
        pad_end=False,
        norm=None,
        name=None
    )

Implemented with TPU/GPU-compatible ops and supports gradients.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `signals` | A `[..., samples]` `float32`/`float64` `Tensor` of real-valued signals. |
| `frame_length` | An integer scalar `Tensor`. The window length in samples which must be divisible by 4. |
| `window_fn` | A callable that takes a frame\_length and a `dtype` keyword argument and returns a `[frame_length]` `Tensor` of samples in the provided datatype. If set to `None`, a rectangular window with a scale of 1/sqrt(2) is used. For perfect reconstruction of a signal from `mdct` followed by `inverse_mdct`, please use [`tf.signal.vorbis_window`](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window)<br>, [`tf.signal.kaiser_bessel_derived_window`](https://www.tensorflow.org/api_docs/python/tf/signal/kaiser_bessel_derived_window)<br> or `None`. If using another window function, make sure that w\[n\]^2 + w\[n + frame\_length // 2\]^2 = 1 and w\[n\] = w\[frame\_length - n - 1\] for n = 0,...,frame\_length // 2 - 1 to achieve perfect reconstruction. |
| `pad_end` | Whether to pad the end of `signals` with zeros when the provided frame length and step produces a frame that lies partially past its end. |
| `norm` | If it is None, unnormalized dct4 is used, if it is "ortho" orthonormal dct4 is used. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `[..., frames, frame_length // 2]` `Tensor` of `float32`/`float64` MDCT values where `frames` is roughly `samples // (frame_length // 2)` when `pad_end=False`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `signals` is not at least rank 1, `frame_length` is not scalar, or `frame_length` is not a multiple of `4`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.