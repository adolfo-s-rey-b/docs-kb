[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Softmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Softmax Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/activations/softmax.py#L14-L115)

Softmax activation layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Softmax(
        axis=-1, **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Basic classification: Classify images of clothing](https://www.tensorflow.org/tutorials/keras/classification)<br>    <br>*   [TensorFlow 2 quickstart for beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)<br>    <br>*   [Building Your Own Federated Learning Algorithm](https://www.tensorflow.org/federated/tutorials/building_your_own_federated_learning_algorithm)<br>    <br>*   [Composing Learning Algorithms](https://www.tensorflow.org/federated/tutorials/composing_learning_algorithms)<br>    <br>*   [Federated Learning for Image Classification](https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification) |

#### Formula:

exp_x = exp(x - max(x))
    f(x) = exp_x / sum(exp_x)

#### Example:

    softmax_layer = keras.layers.Softmax()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Integer, or list of Integers, axis along which the softmax normalization is applied. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | The inputs (logits) to the softmax layer. |
| `mask` | A boolean mask that is broadcastable to `inputs`. The mask specifies 1 to keep and 0 to mask. Each dimension of the mask must either be 1 or match the corresponding dimension of `inputs`; it must not be larger. Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| Softmaxed output with the same shape as `inputs`. |     |

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