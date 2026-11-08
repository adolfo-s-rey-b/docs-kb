[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_custom_objects#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_custom_objects)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_custom_objects?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_custom_objects#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.get\_custom\_objects Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_custom_objects#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L68-L91)

Retrieves a live reference to the global dictionary of custom objects.

tf.keras.utils.get_custom_objects()

Custom objects set using `custom_object_scope()` are not added to the global dictionary of custom objects, and will not appear in the returned dictionary.

#### Example:

get_custom_objects().clear()
    get_custom_objects()['MyObject'] = MyObject

|     |
| --- |
| Returns<br>------- |     |
| Global dictionary mapping registered class names to classes. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.