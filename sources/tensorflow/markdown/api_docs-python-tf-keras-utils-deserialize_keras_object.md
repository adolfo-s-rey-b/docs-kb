[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fdeserialize_keras_object&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.deserialize\_keras\_object Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/deserialize_keras_object#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/serialization_lib.py#L427-L798)

Retrieve the object by deserializing the config dict.

tf.keras.utils.deserialize_keras_object(
        config, custom_objects=None, safe_mode=True, **kwargs
    )

The config dict is a Python dictionary that consists of a set of key-value pairs, and represents a Keras object, such as an `Optimizer`, `Layer`, `Metrics`, etc. The saving and loading library uses the following keys to record information of a Keras object:

*   `class_name`: String. This is the name of the class, as exactly defined in the source code, such as "LossesContainer".
*   `config`: Dict. Library-defined or user-defined key-value pairs that store the configuration of the object, as obtained by `object.get_config()`.
*   `module`: String. The path of the python module. Built-in Keras classes expect to have prefix `keras`.
*   `registered_name`: String. The key the class is registered under via `keras.saving.register_keras_serializable(package, name)` API. The key has the format of '{package}>{name}', where `package` and `name` are the arguments passed to `register_keras_serializable()`. If `name` is not provided, it uses the class name. If `registered_name` successfully resolves to a class (that was registered), the `class_name` and `config` values in the dict will not be used. `registered_name` is only used for non-built-in classes.

For example, the following dictionary represents the built-in Adam optimizer with the relevant config:

dict_structure = {
        "class_name": "Adam",
        "config": {
            "amsgrad": false,
            "beta_1": 0.8999999761581421,
            "beta_2": 0.9990000128746033,
            "decay": 0.0,
            "epsilon": 1e-07,
            "learning_rate": 0.0010000000474974513,
            "name": "Adam"
        },
        "module": "keras.optimizers",
        "registered_name": None
    }
    # Returns an `Adam` instance identical to the original one.
    deserialize_keras_object(dict_structure)

If the class does not have an exported Keras namespace, the library tracks it by its `module` and `class_name`. For example:

dict_structure = {
      "class_name": "MetricsList",
      "config": {
          ...
      },
      "module": "keras.trainers.compile_utils",
      "registered_name": "MetricsList"
    }
    
    # Returns a `MetricsList` instance identical to the original one.
    deserialize_keras_object(dict_structure)

And the following dictionary represents a user-customized `MeanSquaredError` loss:

@keras.saving.register_keras_serializable(package='my_package')
    class ModifiedMeanSquaredError(keras.losses.MeanSquaredError):
      ...
    
    dict_structure = {
        "class_name": "ModifiedMeanSquaredError",
        "config": {
            "fn": "mean_squared_error",
            "name": "mean_squared_error",
            "reduction": "auto"
        },
        "registered_name": "my_package>ModifiedMeanSquaredError"
    }
    # Returns the `ModifiedMeanSquaredError` object
    deserialize_keras_object(dict_structure)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | Python dict describing the object. |
| `custom_objects` | Python dict containing a mapping between custom object names the corresponding classes or functions. |
| `safe_mode` | Boolean, defaults to False. If True, disables unsafe lambda deserialization.<br><br>Note that safe\_mode is designed to protect against code serialized within the Keras model file being loaded. It does not provide isolation from the local Python environment and does not guard against modifications made outside of the serialized file. |

|     |
| --- |
| Returns<br>------- |     |
| The object described by the `config` dictionary. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.