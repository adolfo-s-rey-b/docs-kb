[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.get\_registered\_name Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_registered_name#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L159-L182)

Returns the name registered to an object within the Keras framework.

tf.keras.utils.get_registered_name(
        obj
    )

This function is part of the Keras serialization and deserialization framework. It maps objects to the string names associated with those objects for serialization/deserialization.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `obj` | The object to look up. |

|     |
| --- |
| Returns<br>------- |     |
| The name associated with the object, or the default Python name if the object is not registered. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.