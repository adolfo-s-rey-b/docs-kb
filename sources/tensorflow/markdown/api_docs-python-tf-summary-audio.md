[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/audio#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/audio)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/audio?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/audio#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/audio#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/audio#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.audio Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/audio#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/audio#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/audio#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/tb_summary.py#L30-L82)

Write an audio summary.

tf.summary.audio(
        name,
        data,
        sample_rate,
        step=None,
        max_outputs=3,
        encoding=None,
        description=None
    )

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `name` | A name for this summary. The summary tag used for TensorBoard will be this name prefixed by any active name scopes. |
| `data` | A `Tensor` representing audio data with shape `[k, t, c]`, where `k` is the number of audio clips, `t` is the number of frames, and `c` is the number of channels. Elements should be floating-point values in `[-1.0, 1.0]`. Any of the dimensions may be statically unknown (i.e., `None`). |
| `sample_rate` | An `int` or rank-0 `int32` `Tensor` that represents the sample rate, in Hz. Must be positive. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `max_outputs` | Optional `int` or rank-0 integer `Tensor`. At most this many audio clips will be emitted at each step. When more than `max_outputs` many clips are provided, the first `max_outputs` many clips will be used and the rest silently discarded. |
| `encoding` | Optional constant `str` for the desired encoding. Only "wav" is currently supported, but this is not guaranteed to remain the default, so if you want "wav" in particular, set this explicitly. |
| `description` | Optional long-form description for this summary, as a constant `str`. Markdown is supported. Defaults to empty. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or false if no summary was emitted because no default summary writer was available. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if a default writer exists, but no step was provided and [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br> is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.