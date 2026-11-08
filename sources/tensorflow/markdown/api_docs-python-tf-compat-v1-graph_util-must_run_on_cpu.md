[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.graph\_util.must\_run\_on\_cpu Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/graph_util/must_run_on_cpu#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/graph_util_impl.py#L102-L147)

Returns True if the given node\_def must run on CPU, otherwise False. (deprecated)

tf.compat.v1.graph_util.must_run_on_cpu(
        node, pin_variables_on_cpu=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `node` | The node to be assigned to a device. Could be either an ops.Operation or NodeDef. |
| `pin_variables_on_cpu` | If True, this function will return False if node\_def represents a variable-related op. |

|     |
| --- |
| Returns<br>------- |     |
| True if the given node must run on CPU, otherwise False. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.