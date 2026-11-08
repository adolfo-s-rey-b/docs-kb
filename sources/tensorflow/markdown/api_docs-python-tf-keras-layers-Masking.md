[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Masking Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/masking.py#L8-L76)

Masks a sequence by using a mask value to skip timesteps.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Masking(
        mask_value=0.0, **kwargs
    )

For each timestep in the input tensor (dimension #1 in the tensor), if all values in the input tensor at that timestep are equal to `mask_value`, then the timestep will be masked (skipped) in all downstream layers (as long as they support masking).

If any downstream layer does not support masking yet receives such an input mask, an exception will be raised.

#### Example:

Consider a NumPy data array `x` of shape `(samples, timesteps, features)`, to be fed to an LSTM layer. You want to mask timestep #3 and #5 because you lack data for these timesteps. You can:

*   Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
*   Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

samples, timesteps, features = 32, 10, 8
    inputs = np.random.random([samples, timesteps, features]).astype(np.float32)
    inputs[:, 3, :] = 0.
    inputs[:, 5, :] = 0.
    
    model = keras.models.Sequential()
    model.add(keras.layers.Masking(mask_value=0.0))
    model.add(keras.layers.LSTM(32))
    output = model(inputs)
    # The time step 3 and 5 will be skipped from LSTM calculation.

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