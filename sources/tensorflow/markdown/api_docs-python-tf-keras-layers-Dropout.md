[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FDropout&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Dropout Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/regularization/dropout.py#L6-L120)

Applies dropout to the input.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Dropout(
        rate, noise_shape=None, seed=None, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Migrate checkpoint saving](https://www.tensorflow.org/guide/migrate/checkpoint_saver)<br>    <br>*   [Migrate evaluation](https://www.tensorflow.org/guide/migrate/evaluator)<br>    <br>*   [Migrate the fault tolerance mechanism](https://www.tensorflow.org/guide/migrate/fault_tolerance)<br>    <br>*   [Migrate TensorBoard: TensorFlow's visualization toolkit](https://www.tensorflow.org/guide/migrate/tensorboard) | *   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification) |

The `Dropout` layer randomly sets input units to 0 with a frequency of `rate` at each step during training time, which helps prevent overfitting. Inputs not set to 0 are scaled up by `1 / (1 - rate)` such that the sum over all inputs is unchanged.

Note that the `Dropout` layer only applies when `training` is set to `True` in `call()`, such that no values are dropped during inference. When using `model.fit`, `training` will be appropriately set to `True` automatically. In other contexts, you can set the argument explicitly to `True` when calling the layer.

(This is in contrast to setting `trainable=False` for a `Dropout` layer. `trainable` does not affect the layer's behavior, as `Dropout` does not have any variables/weights that can be frozen during training.)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `rate` | Float between 0 and 1. Fraction of the input units to drop. |
| `noise_shape` | 1D integer tensor representing the shape of the binary dropout mask that will be multiplied with the input. For instance, if your inputs have shape `(batch_size, timesteps, features)` and you want the dropout mask to be the same for all timesteps, you can use `noise_shape=(batch_size, 1, features)`. |
| `seed` | A Python integer to use as random seed. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | Input tensor (of any rank). |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing). |

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