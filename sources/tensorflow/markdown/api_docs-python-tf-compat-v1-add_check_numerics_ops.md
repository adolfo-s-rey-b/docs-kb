[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.add\_check\_numerics\_ops Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/add_check_numerics_ops#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/numerics.py#L81-L131)

Connect a [`tf.debugging.check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics)
 to every floating point tensor.

tf.compat.v1.add_check_numerics_ops()

`check_numerics` operations themselves are added for each `half`, `float`, or `double` tensor in the current default graph. For all ops in the graph, the `check_numerics` op for all of its (`half`, `float`, or `double`) inputs is guaranteed to run before the `check_numerics` op on any of its outputs.

|     |
| --- |
| Returns<br>------- |     |
| A `group` op depending on all `check_numerics` ops added. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the graph contains any numeric operations in a control flow structure. |
| `RuntimeError` | If called with eager execution enabled. |

eager compatibility
-------------------

Not compatible with eager execution. To check for `Inf`s and `NaN`s under eager execution, call [`tf.debugging.enable_check_numerics()`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics)
 once before executing the checked operations.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.