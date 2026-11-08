[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.experimental.write\_raw\_pb Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/write_raw_pb#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L820-L872)

Writes a summary using raw [`tf.compat.v1.Summary`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/Summary)
 protocol buffers.

tf.summary.experimental.write_raw_pb(
        tensor, step=None, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | the string Tensor holding one or more serialized `Summary` protobufs |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `name` | Optional string name for this op. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or false if no summary was written because no default summary writer was available. |     |

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