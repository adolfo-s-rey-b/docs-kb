[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.regularizers.L1 Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L214-L240)

A regularizer that applies a L1 regularization penalty.

Inherits From: [`Regularizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer)

#### View aliases

**Main aliases**

[`tf.keras.regularizers.l1`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L1)

tf.keras.regularizers.L1(
        l1=0.01
    )

The L1 regularization penalty is computed as: `loss = l1 * reduce_sum(abs(x))`

L1 may be passed to a layer as a string identifier:

    dense = Dense(3, kernel_regularizer='l1')

In this case, the default value used is `l1=0.01`.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `l1` | float, L1 regularization factor. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L127-L145)

@classmethod

Creates a regularizer from its config.

This method is the reverse of `get_config`, capable of instantiating the same regularizer from the config dictionary.

This method is used by Keras `model_to_estimator`, saving and loading models to HDF5 formats, Keras model cloning, some visualization utilities, and exporting models to and from JSON.

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of get\_config. |

|     |
| --- |
| Returns |     |
| A regularizer instance. |     |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L239-L240)

get_config()

Returns the config of the regularizer.

An regularizer config is a Python dictionary (serializable) containing all configuration parameters of the regularizer. The same regularizer can be reinstantiated later (without any saved state) from this configuration.

This method is optional if you are just training and executing models, exporting to and from SavedModels, or using weight checkpoints.

This method is required for Keras `model_to_estimator`, saving and loading models to HDF5 formats, Keras model cloning, some visualization utilities, and exporting models to and from JSON.

|     |
| --- |
| Returns |     |
| Python dictionary. |     |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L236-L237)

__call__(
        x
    )

Compute a regularization penalty from an input tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.