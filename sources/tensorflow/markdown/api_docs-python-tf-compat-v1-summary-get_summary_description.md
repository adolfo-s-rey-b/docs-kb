[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsummary%2Fget_summary_description&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.summary.get\_summary\_description Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/get_summary_description#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary.py#L763-L790)

Given a TensorSummary node\_def, retrieve its SummaryDescription.

tf.compat.v1.summary.get_summary_description(
        node_def
    )

When a Summary op is instantiated, a SummaryDescription of associated metadata is stored in its NodeDef. This method retrieves the description.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `node_def` | the node\_def\_pb2.NodeDef of a TensorSummary op |

|     |
| --- |
| Returns<br>------- |     |
| a summary\_pb2.SummaryDescription |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the node is not a summary op. |

eager compatibility
-------------------

Not compatible with eager execution. To write TensorBoard summaries under eager execution, use `tf.contrib.summary` instead.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.