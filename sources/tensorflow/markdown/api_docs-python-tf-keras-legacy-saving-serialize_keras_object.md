[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flegacy%2Fsaving%2Fserialize_keras_object&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.legacy.saving.serialize\_keras\_object Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/saving/serialization.py#L264-L327)

Serialize a Keras object into a JSON-compatible representation.

#### View aliases

**Main aliases**

[`tf.keras.utils.legacy.serialize_keras_object`](https://www.tensorflow.org/api_docs/python/tf/keras/legacy/saving/serialize_keras_object)

tf.keras.legacy.saving.serialize_keras_object(
        instance
    )

Calls to `serialize_keras_object` while underneath the `SharedObjectSavingScope` context manager will cause any objects re-used across multiple layers to be saved with a special shared object ID. This allows the network to be re-created properly during deserialization.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `instance` | The object to serialize. |

|     |
| --- |
| Returns<br>------- |     |
| A dict-like, JSON-compatible representation of the object's config. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.