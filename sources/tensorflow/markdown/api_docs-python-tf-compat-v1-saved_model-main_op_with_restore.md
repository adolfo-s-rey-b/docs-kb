[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.main\_op\_with\_restore Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/main_op_impl.py#L48-L66)

Returns a main op to init variables, tables and restore the graph. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.main_op.main_op_with_restore`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/main_op_with_restore)

tf.compat.v1.saved_model.main_op_with_restore(
        restore_op_name
    )

Returns the main op including the group of ops that initializes all variables, initialize local variables, initialize all tables and the restore op name.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `restore_op_name` | Name of the op to use to restore the graph. |

|     |
| --- |
| Returns<br>------- |     |
| The set of ops to be run as part of the main op upon the load operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.