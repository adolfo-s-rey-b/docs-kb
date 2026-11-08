[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.CustomObjectScope Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#methods)
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L10-L61)

Exposes custom classes/functions to Keras deserialization internals.

#### View aliases

**Main aliases**

[`tf.keras.utils.custom_object_scope`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/CustomObjectScope)

tf.keras.utils.CustomObjectScope(
        custom_objects
    )

Under a scope `with custom_object_scope(objects_dict)`, Keras methods such as [`keras.models.load_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
 or `keras.models.model_from_config()` will be able to deserialize any custom object referenced by a saved config (e.g. a custom layer or metric).

#### Example:

Consider a custom regularizer `my_regularizer`:

layer = Dense(3, kernel_regularizer=my_regularizer)
    # Config contains a reference to `my_regularizer`
    config = layer.get_config()
    ...
    # Later:
    with custom_object_scope({'my_regularizer': my_regularizer}):
        layer = Dense.from_config(config)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `custom_objects` | Dictionary of `{str: object}` pairs, where the `str` key is the object name. |

Methods
-------

### `__enter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L49-L56)

__enter__()

### `__exit__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L58-L61)

__exit__(
        *args, **kwargs
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.