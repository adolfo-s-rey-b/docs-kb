[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.register\_keras\_serializable Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/register_keras_serializable#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/object_registration.py#L94-L156)

Registers an object with the Keras serialization framework.

tf.keras.utils.register_keras_serializable(
        package='Custom', name=None
    )

This decorator injects the decorated class or function into the Keras custom object dictionary, so that it can be serialized and deserialized without needing an entry in the user-provided custom object dict. It also injects a function that Keras will call to get the object's serializable string key.

Note that to be serialized and deserialized, classes must implement the `get_config()` method. Functions do not have this requirement.

The object will be registered under the key `'package>name'` where `name`, defaults to the object name if not passed.

#### Example:

# Note that `'my_package'` is used as the `package` argument here, and since
    # the `name` argument is not provided, `'MyDense'` is used as the `name`.
    @register_keras_serializable('my_package')
    class MyDense(keras.layers.Dense):
        pass
    
    assert get_registered_object('my_package>MyDense') == MyDense
    assert get_registered_name(MyDense) == 'my_package>MyDense'

|     |     |
| --- | --- |
| Args<br>---- |     |
| `package` | The package that this class belongs to. This is used for the `key` (which is `"package>name"`) to identify the class. Note that this is the first argument passed into the decorator. |
| `name` | The name to serialize this class under in this package. If not provided or `None`, the class' name will be used (note that this is the case when the decorator is used with only one argument, which becomes the `package`). |

|     |
| --- |
| Returns<br>------- |     |
| A decorator that registers the decorated class with the passed names. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.