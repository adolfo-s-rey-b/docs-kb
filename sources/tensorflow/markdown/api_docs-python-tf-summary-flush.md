[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/flush#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/flush)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/flush?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/flush#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/flush#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.flush Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/flush#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/flush#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L1157-L1179)

Forces summary writer to send any buffered data to storage.

tf.summary.flush(
        writer=None, name=None
    )

This operation blocks until that finishes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `writer` | The [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)<br> to flush. If None, the current default writer will be used instead; if there is no current writer, this returns [`tf.no_op`](https://www.tensorflow.org/api_docs/python/tf/no_op)<br>. |
| `name` | Ignored legacy argument for a name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| The created [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.