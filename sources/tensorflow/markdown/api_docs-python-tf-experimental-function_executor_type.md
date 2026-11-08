[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.function\_executor\_type Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/context.py#L2903-L2923)

Context manager for setting the executor of eager defined functions.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.function_executor_type`](https://www.tensorflow.org/api_docs/python/tf/experimental/function_executor_type)

@tf_contextlib.contextmanager

Eager defined functions are functions decorated by tf.contrib.eager.defun.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `executor_type` | a string for the name of the executor to be used to execute functions defined by tf.contrib.eager.defun. |

|     |
| --- |
| Yields<br>------ |     |
| Context manager for setting the executor of eager defined functions. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.