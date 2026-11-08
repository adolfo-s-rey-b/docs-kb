[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fget_registered_object%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.get\_registered\_object Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_object?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L185-L230)

Returns the class associated with `name` if it is registered with Keras.

tf.keras.utils.get_registered_object(
        name, custom_objects=None, module_objects=None
    )

This function is part of the Keras serialization and deserialization framework. It maps strings to the objects associated with them for serialization/deserialization.

#### Example:

def from_config(cls, config, custom_objects=None):
        if 'my_custom_object_name' in config:
            config['hidden_cls'] = tf.keras.saving.get_registered_object(
                config['my_custom_object_name'], custom_objects=custom_objects)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The name to look up. |
| `custom_objects` | A dictionary of custom objects to look the name up in. Generally, custom\_objects is provided by the user. |
| `module_objects` | A dictionary of custom objects to look the name up in. Generally, module\_objects is provided by midlevel library implementers. |

|     |
| --- |
| Returns<br>------- |     |
| An instantiable class associated with `name`, or `None` if no such class exists. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.