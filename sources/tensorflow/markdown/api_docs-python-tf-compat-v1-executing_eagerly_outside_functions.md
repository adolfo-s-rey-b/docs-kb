[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/executing_eagerly_outside_functions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/executing_eagerly_outside_functions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/executing_eagerly_outside_functions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/executing_eagerly_outside_functions#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.executing\_eagerly\_outside\_functions Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/executing_eagerly_outside_functions#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L4863-L4893)

Returns True if executing eagerly, even if inside a graph function.

tf.compat.v1.executing_eagerly_outside_functions() -> bool

This function will check the outermost context for the program and see if it is in eager mode. It is useful comparing to [`tf.executing_eagerly()`](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly)
, which checks the current context and will return `False` within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 body. It can be used to build library that behave differently in eager runtime and v1 session runtime (deprecated).

#### Example:

    tf.compat.v1.enable_eager_execution()

|     |
| --- |
| Returns<br>------- |     |
| boolean, whether the outermost context is in eager mode. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.