[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.models.load\_model Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/saving_api.py#L125-L235)

Loads a model saved via `model.save()` or from an Orbax checkpoint.

tf.keras.models.load_model(
        filepath, custom_objects=None, compile=True, safe_mode=True
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model)<br>    <br>*   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)<br>    <br>*   [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)<br>    <br>*   [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filepath` | `str` or `pathlib.Path` object, path to the saved model file or Orbax checkpoint directory. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom classes or functions to be considered during deserialization. |
| `compile` | Boolean, whether to compile the model after loading. |
| `safe_mode` | Boolean, whether to disallow unsafe `lambda` deserialization. When `safe_mode=False`, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the Keras v3 model format. Defaults to `True`. |

|     |
| --- |
| Returns<br>------- |     |
| A Keras model instance. If the original model was compiled, and the argument `compile=True` is set, then the returned model will be compiled. Otherwise, the model will be left uncompiled. |     |

#### Example:

model = keras.Sequential([\
        keras.layers.Dense(5, input_shape=(3,)),\
        keras.layers.Softmax()])
    model.save("model.keras")
    loaded_model = keras.saving.load_model("model.keras")

Note that the model variables may have different name values (`var.name` property, e.g. `"dense_1/kernel:0"`) after being reloaded. It is recommended that you use layer attributes to access specific variables, e.g. `model.get_layer("dense_1").kernel`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.