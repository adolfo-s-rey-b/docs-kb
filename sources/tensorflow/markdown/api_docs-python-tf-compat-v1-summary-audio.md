[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.audio Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/audio#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L347-L464)

Outputs a `Summary` protocol buffer with audio.

tf.compat.v1.summary.audio(
        name, tensor, sample_rate, max_outputs=3, collections=None, family=None
    )

Migrate to TF2
--------------

For compatibility purposes, when invoked in TF2 where the outermost context is eager mode, this API will check if there is a suitable TF2 summary writer context available, and if so will forward this call to that writer instead. A "suitable" writer context means that the writer is set as the default writer, and there is an associated non-empty value for `step` (see [`tf.summary.SummaryWriter.as_default`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter#as_default)
, [`tf.summary.experimental.set_step`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/set_step)
 or alternatively [`tf.compat.v1.train.create_global_step`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
). For the forwarded call, the arguments here will be passed to the TF2 implementation of [`tf.summary.audio`](https://www.tensorflow.org/api_docs/python/tf/summary/audio)
, and the return value will be an empty bytestring tensor, to avoid duplicate summary writing. This forwarding is best-effort and not all arguments will be preserved. Additionally:

*   The TF2 op just outputs the data under a single tag that contains multiple samples, rather than multiple tags (i.e. no "/0" or "/1" suffixes).

To migrate to TF2, please use [`tf.summary.audio`](https://www.tensorflow.org/api_docs/python/tf/summary/audio)
 instead. Please check [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
 for concrete steps for migration.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `name` | `name` | \-  |
| `tensor` | `data` | Input for this argument now must be three-dimensional `[k, t, c]`, where `k` is the number of audio clips, `t` is the number of frames, and `c` is the number of channels. Two-dimensional input is no longer supported. |
| `sample_rate` | `sample_rate` | \-  |
| \-  | `step` | Explicit int64-castable monotonic step value. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>. |
| `max_outputs` | `max_outputs` | \-  |
| `collections` | Not Supported | \-  |
| `family` | Removed | Please use [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instead to manage summary name prefix. |
| \-  | `encoding` | Optional constant str for the desired encoding. Check the docs for [`tf.summary.audio`](https://www.tensorflow.org/api_docs/python/tf/summary/audio)<br> for latest supported audio formats. |
| \-  | `description` | Optional long-form `str` description for the summary. Markdown is supported. Defaults to empty. |

Description
-----------

The summary has up to `max_outputs` summary values containing audio. The audio is built from `tensor` which must be 3-D with shape `[batch_size, frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are assumed to be in the range of `[-1.0, 1.0]` with a sample rate of `sample_rate`.

The `tag` in the outputted Summary.Value protobufs is generated based on the name, with a suffix depending on the max\_outputs setting:

*   If `max_outputs` is 1, the summary value tag is '_name_/audio'.
*   If `max_outputs` is greater than 1, the summary value tags are generated sequentially as '_name_/audio/0', '_name_/audio/1', etc

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the generated node. Will also serve as a series name in TensorBoard. |
| `tensor` | A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]` or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`. |
| `sample_rate` | A Scalar `float32` `Tensor` indicating the sample rate of the signal in hertz. |
| `max_outputs` | Max number of batch elements to generate audio for. |
| `collections` | Optional list of ops.GraphKeys. The collections to add the summary to. Defaults to \[\_ops.GraphKeys.SUMMARIES\] |
| `family` | Optional; if provided, used as the prefix of the summary tag name, which controls the tab name used for display on Tensorboard. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of type `string`. The serialized `Summary` protocol buffer. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.