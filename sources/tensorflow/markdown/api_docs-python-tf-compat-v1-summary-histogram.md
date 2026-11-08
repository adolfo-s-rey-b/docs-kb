[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsummary%2Fhistogram&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.histogram Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/histogram#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L256-L344)

Outputs a `Summary` protocol buffer with a histogram.

tf.compat.v1.summary.histogram(
        name, values, collections=None, family=None
    )

Migrate to TF2
--------------

For compatibility purposes, when invoked in TF2 where the outermost context is eager mode, this API will check if there is a suitable TF2 summary writer context available, and if so will forward this call to that writer instead. A "suitable" writer context means that the writer is set as the default writer, and there is an associated non-empty value for `step` (see [`tf.summary.SummaryWriter.as_default`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter#as_default)
, [`tf.summary.experimental.set_step`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/set_step)
 or alternatively [`tf.compat.v1.train.create_global_step`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
). For the forwarded call, the arguments here will be passed to the TF2 implementation of [`tf.summary.histogram`](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
, and the return value will be an empty bytestring tensor, to avoid duplicate summary writing. This forwarding is best-effort and not all arguments will be preserved.

To migrate to TF2, please use [`tf.summary.histogram`](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
 instead. Please check [Migrating tf.summary usage to TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x)
 for concrete steps for migration.

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `name` | `name` | \-  |
| `values` | `data` | \-  |
| \-  | `step` | Explicit int64-castable monotonic step value. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step) |
| \-  | `buckets` | Optional positive `int` specifying the histogram bucket number. |
| `collections` | Not Supported | \-  |
| `family` | Removed | Please use [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instead to manage summary name prefix. |
| \-  | `description` | Optional long-form `str` description for the summary. Markdown is supported. Defaults to empty. |

Description
-----------

Adding a histogram summary makes it possible to visualize your data's distribution in TensorBoard. You can see a detailed explanation of the TensorBoard histogram dashboard [here](https://www.tensorflow.org/get_started/tensorboard_histograms)
.

The generated [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
 has one summary value containing a histogram for `values`.

This op reports an `InvalidArgument` error if any value is not finite.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the generated node. Will also serve as a series name in TensorBoard. |
| `values` | A real numeric `Tensor`. Any shape. Values to use to build the histogram. |
| `collections` | Optional list of graph collections keys. The new summary op is added to these collections. Defaults to `[GraphKeys.SUMMARIES]`. |
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