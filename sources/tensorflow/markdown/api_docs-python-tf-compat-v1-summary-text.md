[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsummary%2Ftext&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.text Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/text#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L467-L552)

Summarizes textual data.

tf.compat.v1.summary.text(
        name, tensor, collections=None
    )

Migrate to TF2
--------------

For compatibility purposes, when invoked in TF2 where the outermost context is eager mode, this API will check if there is a suitable TF2 summary writer context available, and if so will forward this call to that writer instead. A "suitable" writer context means that the writer is set as the default writer, and there is an associated non-empty value for `step` (see [`tf.summary.SummaryWriter.as_default`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter#as_default)
, [`tf.summary.experimental.set_step`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/set_step)
 or alternatively [`tf.compat.v1.train.create_global_step`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
). For the forwarded call, the arguments here will be passed to the TF2 implementation of [`tf.summary.text`](https://www.tensorflow.org/api_docs/python/tf/summary/text)
, and the return value will be an empty bytestring tensor, to avoid duplicate summary writing. This forwarding is best-effort and not all arguments will be preserved.

To migrate to TF2, please use [`tf.summary.text`](https://www.tensorflow.org/api_docs/python/tf/summary/text)
 instead. Please check [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
 for concrete steps for migration.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `name` | `name` | \-  |
| `tensor` | `data` | \-  |
| \-  | `step` | Explicit int64-castable monotonic step value. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>. |
| `collections` | Not Supported | \-  |
| \-  | `description` | Optional long-form `str` description for the summary. Markdown is supported. Defaults to empty. |

Description
-----------

Text data summarized via this plugin will be visible in the Text Dashboard in TensorBoard. The standard TensorBoard Text Dashboard will render markdown in the strings, and will automatically organize 1d and 2d tensors into tables. If a tensor with more than 2 dimensions is provided, a 2d subarray will be displayed along with a warning message. (Note that this behavior is not intrinsic to the text summary api, but rather to the default TensorBoard text plugin.)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the generated node. Will also serve as a series name in TensorBoard. |
| `tensor` | a string-type Tensor to summarize. |
| `collections` | Optional list of ops.GraphKeys. The collections to add the summary to. Defaults to \[\_ops.GraphKeys.SUMMARIES\] |

|     |
| --- |
| Returns<br>------- |     |
| A TensorSummary op that is configured so that TensorBoard will recognize that it contains textual data. The TensorSummary is a scalar `Tensor` of type `string` which contains `Summary` protobufs. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If tensor has the wrong type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.