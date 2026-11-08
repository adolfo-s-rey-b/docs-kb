[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.models.save\_model Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/save_model#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/saving/saving_api.py#L19-L122)

Saves a model as a `.keras` file.

tf.keras.models.save_model(
        model, filepath, overwrite=True, zipped=None, **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Train and serve a TensorFlow model with TensorFlow Serving](https://www.tensorflow.org/tfx/tutorials/serving/rest_simple) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | Keras model instance to be saved. |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the model. |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |
| `zipped` | Whether to save the model as a zipped `.keras` archive (default when saving locally), or as an unzipped directory (default when saving on the Hugging Face Hub). |

#### Example:

model = keras.Sequential(
        [\
            keras.layers.Dense(5, input_shape=(3,)),\
            keras.layers.Softmax(),\
        ],
    )
    model.save("model.keras")
    loaded_model = keras.saving.load_model("model.keras")
    x = keras.random.uniform((10, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file is a `zip` archive that contains:

*   The model's configuration (architecture)
*   The model's weights
*   The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.