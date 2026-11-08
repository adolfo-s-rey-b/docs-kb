[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.name\_scope Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/__init__.py#L70-L72)

Creates a sub-namespace for variable paths.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.name_scope`](https://www.tensorflow.org/api_docs/python/tf/keras/name_scope)

tf.keras.name_scope(
        name, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | Name of the current scope (string). |
| `caller` | Optional ID of a caller object (e.g. class instance). |
| `deduplicate` | If `True`, if `caller` was passed, and the previous caller matches the current caller, and the previous name matches the current name, do not reenter a new namespace. |
| `override_parent` | Can be used to provide an absolute path which would override any previously opened name scopes. |

Methods
-------

### `__enter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/core.py#L864-L880)

__enter__()

### `__exit__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/core.py#L882-L885)

__exit__(
        *args, **kwargs
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.