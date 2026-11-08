[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.signal.overlap\_and\_add Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/signal/reconstruction_ops.py#L26-L163)

Reconstructs a signal from a framed representation.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.signal.overlap_and_add`](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add)

tf.signal.overlap_and_add(
        signal, frame_step, name=None
    )

Adds potentially overlapping frames of a signal with shape `[..., frames, frame_length]`, offsetting subsequent frames by `frame_step`. The resulting tensor has shape `[..., output_size]` where

output_size = (frames - 1) * frame_step + frame_length

|     |     |
| --- | --- |
| Args<br>---- |     |
| `signal` | A \[..., frames, frame\_length\] `Tensor`. All dimensions may be unknown, and rank must be at least 2. |
| `frame_step` | An integer or scalar `Tensor` denoting overlap offsets. Must be less than or equal to `frame_length`. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with shape `[..., output_size]` containing the overlap-added frames of `signal`'s inner-most two dimensions. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `signal`'s rank is less than 2, or `frame_step` is not a scalar integer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-01 UTC.