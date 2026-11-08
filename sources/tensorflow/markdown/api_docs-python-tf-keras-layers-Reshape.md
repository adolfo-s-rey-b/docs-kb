[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FReshape&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.keras.layers.Reshape Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Reshape#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/reshaping/reshape.py#L9-L75)

Layer that reshapes inputs into the given shape.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Reshape(
        target_shape, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Customizing what happens in \`fit()\`](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit)<br>    <br>*   [Using Counterfactual Logit Pairing with Keras](https://www.tensorflow.org/responsible_ai/model_remediation/counterfactual/guide/counterfactual_keras) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target_shape` | Target shape. Tuple of integers, does not include the samples dimension (batch size). One element of the `target_shape` can be -1 in which case the missing value is inferred from the size of the array and remaining dimensions. |

|     |
| --- |
| Input shape<br>----------- |     |
| Arbitrary, but required to be compatible with `target_shape`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| `(batch_size, *target_shape)` |     |

#### Example:

    x = keras.Input(shape=(12,))

    # another example with shape inference using `-1` as dimension

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

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.