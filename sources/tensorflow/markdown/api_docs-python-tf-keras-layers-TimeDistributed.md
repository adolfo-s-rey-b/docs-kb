[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FTimeDistributed&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.TimeDistributed Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TimeDistributed#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/time_distributed.py#L10-L141)

This wrapper allows to apply a layer to every temporal slice of an input.

Inherits From: [`Wrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Wrapper)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.TimeDistributed(
        layer, **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Load video data](https://www.tensorflow.org/tutorials/load_data/video) |

Every input should be at least 3D, and the dimension of index one of the first input will be considered to be the temporal dimension.

Consider a batch of 32 video samples, where each sample is a 128x128 RGB image with `channels_last` data format, across 10 timesteps. The batch input shape is `(32, 10, 128, 128, 3)`.

You can then use `TimeDistributed` to apply the same `Conv2D` layer to each of the 10 timesteps, independently:

    inputs = layers.Input(shape=(10, 128, 128, 3), batch_size=32)

Because `TimeDistributed` applies the same instance of `Conv2D` to each of the timestamps, the same set of weights are used at each timestamp.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `layer` | a [`keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br> instance. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | Input tensor of shape (batch, time, ...) or nested tensors, and each of which has shape (batch, time, ...). |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the wrapped layer (only if the layer supports this argument). |
| `mask` | Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked. This argument is passed to the wrapped layer (only if the layer supports this argument). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/wrapper.py#L38-L44)

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