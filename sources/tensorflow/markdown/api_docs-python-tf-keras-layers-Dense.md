[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Dense Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/dense.py#L20-L1247)

Just your regular densely-connected NN layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Dense(
        units,
        activation=None,
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        lora_rank=None,
        lora_alpha=None,
        quantization_config=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging)<br>    <br>*   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Migration examples: Canned Estimators](https://www.tensorflow.org/guide/migrate/canned_estimators)<br>    <br>*   [Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping) | *   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)<br>    <br>*   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder) |

`Dense` implements the operation: `output = activation(dot(input, kernel) + bias)` where `activation` is the element-wise activation function passed as the `activation` argument, `kernel` is a weights matrix created by the layer, and `bias` is a bias vector created by the layer (only applicable if `use_bias` is `True`). When this layer is followed by a `BatchNormalization` layer, it is recommended to set `use_bias=False` as `BatchNormalization` has its own bias term.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, whether the layer uses a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix. |
| `bias_initializer` | Initializer for the bias vector. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. |
| `bias_regularizer` | Regularizer function applied to the bias vector. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. |
| `bias_constraint` | Constraint function applied to the bias vector. |
| `lora_rank` | Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's kernel to non-trainable and replaces it with a delta over the original kernel, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large dense layers. You can also enable LoRA on an existing `Dense` layer by calling `layer.enable_lora(rank)`. |
| `lora_alpha` | Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`. |

|     |
| --- |
| Input shape<br>----------- |     |
| N-D tensor with shape: `(batch_size, ..., input_dim)`. The most common situation would be a 2D input with shape `(batch_size, input_dim)`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| N-D tensor with shape: `(batch_size, ..., units)`. For instance, for a 2D input with shape `(batch_size, input_dim)`, the output would have shape `(batch_size, units)`. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `kernel` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `variable_serialization_spec` | Returns a dict mapping quantization modes to variable names in order.<br><br>This spec is used by `save_own_variables` and `load_own_variables` to determine the correct ordering of variables during serialization for each quantization mode. `None` means no quantization. |

Methods
-------

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/dense.py#L234-L295)

enable_lora(
        rank,
        lora_alpha=None,
        a_initializer='he_uniform',
        b_initializer='zeros'
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/dense.py#L392-L400)

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