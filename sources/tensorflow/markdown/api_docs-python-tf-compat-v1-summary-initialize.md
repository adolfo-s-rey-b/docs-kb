[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.initialize Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/initialize#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L477-L517)

Initializes summary writing for graph execution mode.

tf.compat.v1.summary.initialize(
        graph=None, session=None
    )

This operation is a no-op when executing eagerly.

This helper method provides a higher-level alternative to using `tf.contrib.summary.summary_writer_initializer_op` and `tf.contrib.summary.graph`.

Most users will also want to call [`tf.compat.v1.train.create_global_step`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
 which can happen before or after this function is called.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | A [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)<br> or [`tf.compat.v1.GraphDef`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphDef)<br> to output to the writer. This function will not write the default graph by default. When writing to an event log file, the associated step will be zero. |
| `session` | So this method can call `tf.Session.run`. This defaults to [`tf.compat.v1.get_default_session`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_session)<br>. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If the current thread has no default `tf.contrib.summary.SummaryWriter`. |
| `ValueError` | If session wasn't passed and no default session. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.