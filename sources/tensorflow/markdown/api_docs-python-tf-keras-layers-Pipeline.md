[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Pipeline Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Pipeline#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/pipeline.py#L7-L91)

Applies a series of layers to an input.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Pipeline(
        layers, name=None
    )

This class is useful to build a preprocessing pipeline, in particular an image data augmentation pipeline. Compared to a `Sequential` model, `Pipeline` features a few important differences:

*   It's not a `Model`, just a plain layer.
*   When the layers in the pipeline are compatible with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
    , the pipeline will also remain [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
     compatible. That is to say, the pipeline will not attempt to convert its inputs to backend-native tensors when in a tf.data context (unlike a `Sequential` model).

#### Example:

from keras import layers
    preprocessing_pipeline = layers.Pipeline([\
        layers.AutoContrast(),\
        layers.RandomZoom(0.2),\
        layers.RandomRotation(0.2),\
    ])
    
    # `ds` is a tf.data.Dataset
    preprocessed_ds = ds.map(
        preprocessing_pipeline,
        num_parallel_calls=4,
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `layers` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/pipeline.py#L69-L82)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.