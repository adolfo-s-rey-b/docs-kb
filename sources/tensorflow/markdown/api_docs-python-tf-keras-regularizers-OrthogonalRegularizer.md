[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.regularizers.OrthogonalRegularizer Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L271-L338)

Regularizer that encourages input vectors to be orthogonal to each other.

Inherits From: [`Regularizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Regularizer)

#### View aliases

**Main aliases**

[`tf.keras.regularizers.orthogonal_regularizer`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/OrthogonalRegularizer)

tf.keras.regularizers.OrthogonalRegularizer(
        factor=0.01, mode='rows'
    )

It can be applied to either the rows of a matrix (`mode="rows"`) or its columns (`mode="columns"`). When applied to a `Dense` kernel of shape `(input_dim, units)`, rows mode will seek to make the feature vectors (i.e. the basis of the output space) orthogonal to each other.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `factor` | Float. The regularization factor. The regularization penalty will be proportional to `factor` times the mean of the dot products between the L2-normalized rows (if `mode="rows"`, or columns if `mode="columns"`) of the inputs, excluding the product of each row/column with itself. Defaults to `0.01`. |
| `mode` | String, one of `{"rows", "columns"}`. Defaults to `"rows"`. In rows mode, the regularization effect seeks to make the rows of the input orthogonal to each other. In columns mode, it seeks to make the columns of the input orthogonal to each other. |

#### Example:

    regularizer = OrthogonalRegularizer(factor=0.01)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L337-L338)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/regularizers/regularizers.py#L312-L335)

__call__(
        inputs
    )

Compute a regularization penalty from an input tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.