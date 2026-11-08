[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/frame#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.frame Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/shape_ops.py#L55-L231)

Expands `signal`'s `axis` dimension into frames of `frame_length`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.frame`](https://www.tensorflow.org/api_docs/python/tf/signal/frame)

tf.signal.frame(
        signal,
        frame_length,
        frame_step,
        pad_end=False,
        pad_value=0,
        axis=-1,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Transfer Learning for the Audio Domain with TensorFlow Lite Model Maker](https://www.tensorflow.org/lite/models/modify/model_maker/audio_classification) |

Slides a window of size `frame_length` over `signal`'s `axis` dimension with a stride of `frame_step`, replacing the `axis` dimension with `[frames, frame_length]` frames.

If `pad_end` is True, window positions that are past the end of the `axis` dimension are padded with `pad_value` until the window moves fully past the end of the dimension. Otherwise, only window positions that fully overlap the `axis` dimension are produced.

#### For example:

    # A batch size 3 tensor of 9152 audio samples.

If the dimension along `axis` is N, and `pad_end=False`, the number of frames can be computed by:

 num_frames = 1 + (N - frame_size) // frame_step

If `pad_end=True`, the number of frames can be computed by:

num_frames = -(-N // frame_step) # ceiling division

|     |     |
| --- | --- |
| Args<br>---- |     |
| `signal` | A `[..., samples, ...]` `Tensor`. The rank and dimensions may be unknown. Rank must be at least 1. |
| `frame_length` | The frame length in samples. An integer or scalar `Tensor`. |
| `frame_step` | The frame hop size in samples. An integer or scalar `Tensor`. |
| `pad_end` | Whether to pad the end of `signal` with `pad_value`. |
| `pad_value` | An optional scalar `Tensor` to use where the input signal does not exist when `pad_end` is True. |
| `axis` | A scalar integer `Tensor` indicating the axis to frame. Defaults to the last axis. Supports negative values for indexing from the end. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of frames with shape `[..., num_frames, frame_length, ...]`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `frame_length`, `frame_step`, `pad_value`, or `axis` are not scalar. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.