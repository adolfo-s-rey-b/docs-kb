[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#from_config)
        
    *   [normalized\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#normalized_weights)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.SpectralNormalization Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#from_config)
        
    *   [normalized\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpectralNormalization?version=stable#normalized_weights)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/spectral_normalization.py#L9-L121)

Performs spectral normalization on the weights of a target layer.

Inherits From: [`Wrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Wrapper)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.SpectralNormalization(
        layer, power_iterations=1, **kwargs
    )

This wrapper controls the Lipschitz constant of the weights of a layer by constraining their spectral norm, which can stabilize the training of GANs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `layer` | A [`keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br> instance that has either a `kernel` (e.g. `Conv2D`, `Dense`...) or an `embeddings` attribute (`Embedding` layer). |
| `power_iterations` | int, the number of iterations during normalization. |
| `**kwargs` | Base wrapper keyword arguments. |

#### Examples:

Wrap [`keras.layers.Conv2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D)
:

>>> x = np.random.rand(1, 10, 10, 1)
    >>> conv2d = SpectralNormalization(keras.layers.Conv2D(2, 2))
    >>> y = conv2d(x)
    >>> y.shape
    (1, 9, 9, 2)

Wrap [`keras.layers.Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
:

>>> x = np.random.rand(1, 10, 10, 1)
    >>> dense = SpectralNormalization(keras.layers.Dense(10))
    >>> y = dense(x)
    >>> y.shape
    (1, 10, 10, 10)

#### Reference:

*   [Spectral Normalization for GAN](https://arxiv.org/abs/1802.05957)
    .

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

### `normalized_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/spectral_normalization.py#L93-L116)

normalized_weights()

Generate spectral normalized weights.

This method returns the updated value for `self.kernel` with the spectral normalized value, so that the layer is ready for `call()`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.