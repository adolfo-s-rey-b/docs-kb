[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.all\_v2\_summary\_ops Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/all_v2_summary_ops#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L665-L678)

Returns all V2-style summary ops defined in the current default graph.

tf.compat.v1.summary.all_v2_summary_ops()

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Migrating tf.summary usage to TF 2.x](https://www.tensorflow.org/tensorboard/migrate) |

This includes ops from TF 2.0 tf.summary and TF 1.x tf.contrib.summary (except for `tf.contrib.summary.graph` and `tf.contrib.summary.import_event`), but does _not_ include TF 1.x tf.summary ops.

|     |
| --- |
| Returns<br>------- |     |
| List of summary ops, or None if called under eager execution. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.