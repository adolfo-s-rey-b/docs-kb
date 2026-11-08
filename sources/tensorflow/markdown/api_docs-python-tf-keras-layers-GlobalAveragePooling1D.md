[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.GlobalAveragePooling1D Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/global_average_pooling1d.py#L6-L86)

Global average pooling operation for temporal data.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.GlobalAvgPool1D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GlobalAveragePooling1D)

tf.keras.layers.GlobalAveragePooling1D(
        data_format=None, keepdims=False, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Taking advantage of context features](https://www.tensorflow.org/recommenders/examples/context_features)<br>    <br>*   [Building deep retrieval models](https://www.tensorflow.org/recommenders/examples/deep_recommenders)<br>    <br>*   [Using side features: feature preprocessing](https://www.tensorflow.org/recommenders/examples/featurization) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `keepdims` | A boolean, whether to keep the temporal dimension or not. If `keepdims` is `False` (default), the rank of the tensor is reduced for spatial dimensions. If `keepdims` is `True`, the temporal dimension are retained with length 1. The behavior is the same as for [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)<br> or `np.mean`. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A 3D tensor. |
| `mask` | Binary tensor of shape `(batch_size, steps)` indicating whether a given step should be masked (excluded from the average). |

#### Input shape:

*   If `data_format='channels_last'`: 3D tensor with shape: `(batch_size, steps, features)`
*   If `data_format='channels_first'`: 3D tensor with shape: `(batch_size, features, steps)`

#### Output shape:

*   If `keepdims=False`: 2D tensor with shape `(batch_size, features)`.
*   If `keepdims=True`:
    *   If `data_format="channels_last"`: 3D tensor with shape `(batch_size, 1, features)`
    *   If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, 1)`

#### Example:

    x = np.random.rand(2, 3, 4)

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