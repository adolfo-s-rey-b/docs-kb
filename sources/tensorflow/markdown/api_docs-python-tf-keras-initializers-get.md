[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/get#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.initializers.get Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/__init__.py#L82-L163)

Retrieves a Keras initializer object via an identifier.

tf.keras.initializers.get(
        identifier
    )

The `identifier` may be the string name of a initializers function or class (case-sensitively).

    identifier = 'Ones'

You can also specify `config` of the initializer to this function by passing dict containing `class_name` and `config` as an identifier. Also note that the `class_name` must map to a `Initializer` class.

    cfg = {'class_name': 'Ones', 'config': {} }

In the case that the `identifier` is a class, this method will return a new instance of the class by its constructor.

You may also pass a callable function with a signature that includes `shape` and `dtype=None` as an identifier.

    fn = lambda shape, dtype=None: ops.ones(shape, dtype)

Alternatively, you can pass a backend tensor or numpy array as the `identifier` to define the initializer values directly. Note that when calling the initializer, the specified `shape` argument must be the same as the shape of the tensor.

    tensor = ops.ones(shape=(5, 5))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `identifier` | A string, dict, callable function, or tensor specifying the initializer. If a string, it should be the name of an initializer. If a dict, it should contain the configuration of an initializer. Callable functions or predefined tensors are also accepted. |

|     |
| --- |
| Returns<br>------- |     |
| Initializer instance base on the input identifier. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.