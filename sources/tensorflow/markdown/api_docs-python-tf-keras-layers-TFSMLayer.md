[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.TFSMLayer Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TFSMLayer#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/tfsm_layer.py#L9-L182)

Reload a Keras model/layer that was saved via SavedModel / ExportArchive.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.TFSMLayer(
        filepath,
        call_endpoint='serve',
        call_training_endpoint=None,
        trainable=True,
        name=None,
        dtype=None
    )

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `filepath` | `str` or `pathlib.Path` object. The path to the SavedModel. |
| `call_endpoint` | Name of the endpoint to use as the `call()` method of the reloaded layer. If the SavedModel was created via `model.export()`, then the default endpoint name is `'serve'`. In other cases it may be named `'serving_default'`. |

#### Example:

model.export("path/to/artifact")
    reloaded_layer = TFSMLayer("path/to/artifact")
    outputs = reloaded_layer(inputs)

The reloaded object can be used like a regular Keras layer, and supports training/fine-tuning of its trainable weights. Note that the reloaded object retains none of the internal structure or custom methods of the original object -- it's a brand new layer created around the saved function.

**Limitations:**

*   Only call endpoints with a single `inputs` tensor argument (which may optionally be a dict/tuple/list of tensors) are supported. For endpoints with multiple separate input tensor arguments, consider subclassing `TFSMLayer` and implementing a `call()` method with a custom signature.
*   If you need training-time behavior to differ from inference-time behavior (i.e. if you need the reloaded object to support a `training=True` argument in `__call__()`), make sure that the training-time call function is saved as a standalone endpoint in the artifact, and provide its name to the `TFSMLayer` via the `call_training_endpoint` argument.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/export/tfsm_layer.py#L151-L182)

@classmethod

Creates a TFSMLayer from its config.

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |
| `custom_objects` | Optional dictionary mapping names to custom objects. |
| `safe_mode` | Boolean, whether to disallow loading TFSMLayer. When `safe_mode=True`, loading is disallowed because TFSMLayer loads external SavedModels that may contain attacker-controlled executable graph code. Defaults to `True`. |

|     |
| --- |
| Returns |     |
| A TFSMLayer instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.