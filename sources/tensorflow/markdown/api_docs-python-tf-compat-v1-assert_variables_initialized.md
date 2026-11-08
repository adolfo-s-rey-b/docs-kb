[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assert\_variables\_initialized Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_variables_initialized#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L2022-L2062)

Returns an Op to check if variables are initialized.

tf.compat.v1.assert_variables_initialized(
        var_list=None
    )

When run, the returned Op will raise the exception `FailedPreconditionError` if any of the variables has not yet been initialized.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `var_list` | List of `Variable` objects to check. Defaults to the value of `global_variables().` |

|     |
| --- |
| Returns<br>------- |     |
| An Op, or None if there are no variables. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.