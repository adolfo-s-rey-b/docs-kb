[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#used-in-the-notebooks)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#example)
    
*   [Available penalties](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#available_penalties)
    
*   [Directly calling a regularizer](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#directly_calling_a_regularizer)
    
*   [Developing new regularizers](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#developing_new_regularizers)
    *   [A note on serialization and deserialization:](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#a_note_on_serialization_and_deserialization)
        
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Regularizer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#used-in-the-notebooks)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#example)
    
*   [Available penalties](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#available_penalties)
    
*   [Directly calling a regularizer](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#directly_calling_a_regularizer)
    
*   [Developing new regularizers](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#developing_new_regularizers)
    *   [A note on serialization and deserialization:](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#a_note_on_serialization_and_deserialization)
        
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L8-L165)

Regularizer base class.

#### View aliases

**Main aliases**

[`tf.keras.regularizers.Regularizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Regularizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer)

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

Regularizers allow you to apply penalties on layer parameters or layer activity during optimization. These penalties are summed into the loss function that the network optimizes.

Regularization penalties are applied on a per-layer basis. The exact API will depend on the layer, but many layers (e.g. `Dense`, `Conv1D`, `Conv2D` and `Conv3D`) have a unified API.

These layers expose 3 keyword arguments:

*   `kernel_regularizer`: Regularizer to apply a penalty on the layer's kernel
*   `bias_regularizer`: Regularizer to apply a penalty on the layer's bias
*   `activity_regularizer`: Regularizer to apply a penalty on the layer's output

All layers (including custom layers) expose `activity_regularizer` as a settable property, whether or not it is in the constructor arguments.

The value returned by the `activity_regularizer` is divided by the input batch size so that the relative weighting between the weight regularizers and the activity regularizers does not change with the batch size.

You can access a layer's regularization penalties by calling `layer.losses` after calling the layer on inputs.

Example
-------

    layer = Dense(

    # The kernel regularization term is 0.25

Available penalties
-------------------

L1(0.3)  # L1 Regularization Penalty
    L2(0.1)  # L2 Regularization Penalty
    L1L2(l1=0.01, l2=0.01)  # L1 + L2 penalties

Directly calling a regularizer
------------------------------

Compute a regularization loss on a tensor by directly calling a regularizer as if it is a one-argument function.

E.g.

    regularizer = L2(2.)

Developing new regularizers
---------------------------

Any function that takes in a weight matrix and returns a scalar tensor can be used as a regularizer, e.g.:

    def l1_reg(weight_matrix):

Alternatively, you can write your custom regularizers in an object-oriented way by extending this regularizer base class, e.g.:

    class L2Regularizer(Regularizer):

    tensor = ops.ones(shape=(5, 5))

### A note on serialization and deserialization:

Registering the regularizers as serializable is optional if you are just training and executing models, exporting to and from SavedModels, or saving and loading weight checkpoints.

Registration is required for saving and loading models to HDF5 format, Keras model cloning, some visualization utilities, and exporting models to and from JSON. If using this functionality, you must make sure any python process running your model has also defined and registered your custom regularizer.

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L147-L165)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L123-L125)

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