[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ActivityRegularization Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ActivityRegularization#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/regularization/activity_regularization.py#L6-L43)

Layer that applies an update to the cost function based input activity.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ActivityRegularization(
        l1=0.0, l2=0.0, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `l1` | L1 regularization factor (positive float). |
| `l2` | L2 regularization factor (positive float). |

|     |
| --- |
| Input shape<br>----------- |     |
| Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the samples axis) when using this layer as the first layer in a model. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| Same shape as input. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

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