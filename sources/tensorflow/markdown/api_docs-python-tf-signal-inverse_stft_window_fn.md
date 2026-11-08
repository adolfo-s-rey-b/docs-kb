[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.inverse\_stft\_window\_fn Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/spectral_ops.py#L95-L157)

Generates a window function that can be used in `inverse_stft`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.inverse_stft_window_fn`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn)

tf.signal.inverse_stft_window_fn(
        frame_step,
        forward_window_fn=tf.signal.hann_window,
        name=None
    )

Constructs a window that is equal to the forward window with a further pointwise amplitude correction. `inverse_stft_window_fn` is equivalent to `forward_window_fn` in the case where it would produce an exact inverse.

See examples in `inverse_stft` documentation for usage.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `frame_step` | An integer scalar `Tensor`. The number of samples to step. |
| `forward_window_fn` | window\_fn used in the forward transform, `stft`. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A callable that takes a window length and a `dtype` keyword argument and returns a `[window_length]` `Tensor` of samples in the provided datatype. The returned window is suitable for reconstructing original waveform in inverse\_stft. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.