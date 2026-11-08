[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.legacy.saving.deserialize\_keras\_object Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/saving/serialization.py#L412-L552)

Turns the serialized form of a Keras object back into an actual object.

#### View aliases

**Main aliases**

[`tf.keras.utils.legacy.deserialize_keras_object`](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/deserialize_keras_object)

tf.keras.legacy.saving.deserialize_keras_object(
        identifier,
        module_objects=None,
        custom_objects=None,
        printable_module_name='object'
    )

This function is for mid-level library implementers rather than end users.

Importantly, this utility requires you to provide the dict of `module_objects` to use for looking up the object config; this is not populated by default. If you need a deserialization utility that has preexisting knowledge of built-in Keras objects, use e.g. [`keras.layers.deserialize(config)`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/deserialize)
, [`keras.metrics.deserialize(config)`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/deserialize)
, etc.

Calling `deserialize_keras_object` while underneath the `SharedObjectLoadingScope` context manager will cause any already-seen shared objects to be returned as-is rather than creating a new object.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `identifier` | the serialized form of the object. |
| `module_objects` | A dictionary of built-in objects to look the name up in. Generally, `module_objects` is provided by midlevel library implementers. |
| `custom_objects` | A dictionary of custom objects to look the name up in. Generally, `custom_objects` is provided by the end user. |
| `printable_module_name` | A human-readable string representing the type of the object. Printed in case of exception. |

|     |
| --- |
| Returns<br>------- |     |
| The deserialized object. |     |

#### Example:

A mid-level library implementer might want to implement a utility for retrieving an object from its config, as such:

def deserialize(config, custom_objects=None):
       return deserialize_keras_object(
         identifier,
         module_objects=globals(),
         custom_objects=custom_objects,
         name="MyObjectType",
       )

This is how e.g. [`keras.layers.deserialize()`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/deserialize)
 is implemented.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.