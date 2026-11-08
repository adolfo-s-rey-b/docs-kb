[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.image Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L141-L253)

Outputs a `Summary` protocol buffer with images.

tf.compat.v1.summary.image(
        name, tensor, max_outputs=3, collections=None, family=None
    )

Migrate to TF2
--------------

For compatibility purposes, when invoked in TF2 where the outermost context is eager mode, this API will check if there is a suitable TF2 summary writer context available, and if so will forward this call to that writer instead. A "suitable" writer context means that the writer is set as the default writer, and there is an associated non-empty value for `step` (see [`tf.summary.SummaryWriter.as_default`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter#as_default)
, [`tf.summary.experimental.set_step`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/set_step)
 or alternatively [`tf.compat.v1.train.create_global_step`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
). For the forwarded call, the arguments here will be passed to the TF2 implementation of [`tf.summary.image`](https://www.tensorflow.org/api_docs/python/tf/summary/image)
, and the return value will be an empty bytestring tensor, to avoid duplicate summary writing. This forwarding is best-effort and not all arguments will be preserved. Additionally:

*   The TF2 op does not do any of the normalization steps described above. Rather than rescaling data that's outside the expected range, it simply clips it.
*   The TF2 op just outputs the data under a single tag that contains multiple samples, rather than multiple tags (i.e. no "/0" or "/1" suffixes).

To migrate to TF2, please use [`tf.summary.image`](https://www.tensorflow.org/api_docs/python/tf/summary/image)
 instead. Please check [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
 for concrete steps for migration.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `name` | `name` | \-  |
| `tensor` | `data` | \-  |
| \-  | `step` | Explicit int64-castable monotonic step value. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>. |
| `max_outputs` | `max_outputs` | \-  |
| `collections` | Not Supported | \-  |
| `family` | Removed | Please use [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instead to manage summary name prefix. |
| \-  | `description` | Optional long-form `str` description for the summary. Markdown is supported. Defaults to empty. |

Description
-----------

The summary has up to `max_outputs` summary values containing images. The images are built from `tensor` which must be 4-D with shape `[batch_size, height, width, channels]` and where `channels` can be:

*   1: `tensor` is interpreted as Grayscale.
*   3: `tensor` is interpreted as RGB.
*   4: `tensor` is interpreted as RGBA.

The images have the same number of channels as the input tensor. For float input, the values are normalized one image at a time to fit in the range `[0, 255]`. `uint8` values are unchanged. The op uses two different normalization algorithms:

*   If the input values are all positive, they are rescaled so the largest one is 255.
    
*   If any input value is negative, the values are shifted so input value 0.0 is at 127. They are then rescaled so that either the smallest value is 0, or the largest one is 255.
    

The `tag` in the outputted Summary.Value protobufs is generated based on the name, with a suffix depending on the max\_outputs setting:

*   If `max_outputs` is 1, the summary value tag is '_name_/image'.
*   If `max_outputs` is greater than 1, the summary value tags are generated sequentially as '_name_/image/0', '_name_/image/1', etc.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the generated node. Will also serve as a series name in TensorBoard. |
| `tensor` | A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height, width, channels]` where `channels` is 1, 3, or 4. |
| `max_outputs` | Max number of batch elements to generate images for. |
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