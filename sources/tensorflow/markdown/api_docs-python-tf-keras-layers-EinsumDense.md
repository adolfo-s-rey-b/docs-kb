[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FEinsumDense%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#methods_2)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.EinsumDense Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#methods_2)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/EinsumDense?version=stable#from_config)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/einsum_dense.py#L26-L1611)

A layer that uses `einsum` as the backing computation.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.EinsumDense(
        equation,
        output_shape,
        activation=None,
        bias_axes=None,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        lora_rank=None,
        lora_alpha=None,
        gptq_unpacked_column_size=None,
        quantization_config=None,
        **kwargs
    )

This layer can perform einsum calculations of arbitrary dimensionality.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `equation` | An equation describing the einsum to perform. This equation must be a valid einsum string of the form `ab,bc->ac`, `...ab,bc->...ac`, or `ab...,bc->ac...` where 'ab', 'bc', and 'ac' can be any valid einsum axis expression sequence. |
| `output_shape` | The expected shape of the output tensor (excluding the batch dimension and any dimensions represented by ellipses). You can specify `None` for any dimension that is unknown or can be inferred from the input shape. |
| `activation` | Activation function to use. If you don't specify anything, no activation is applied (that is, a "linear" activation: `a(x) = x`). |
| `bias_axes` | A string containing the output dimension(s) to apply a bias to. Each character in the `bias_axes` string should correspond to a character in the output portion of the `equation` string. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix. |
| `bias_initializer` | Initializer for the bias vector. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. |
| `bias_regularizer` | Regularizer function applied to the bias vector. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. |
| `bias_constraint` | Constraint function applied to the bias vector. |
| `lora_rank` | Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's kernel to non-trainable and replaces it with a delta over the original kernel, obtained via multiplying two lower-rank trainable matrices (the factorization happens on the last dimension). This can be useful to reduce the computation cost of fine-tuning large dense layers. You can also enable LoRA on an existing `EinsumDense` layer by calling `layer.enable_lora(rank)`. lora\_alpha: Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

#### Examples:

**Biased dense layer with einsums**

This example shows how to instantiate a standard Keras dense layer using einsum operations. This example is equivalent to [`keras.layers.Dense(64, use_bias=True)`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
.

    layer = keras.layers.EinsumDense("ab,bc->ac",

**Applying a dense layer to a sequence**

This example shows how to instantiate a layer that applies the same dense operation to every element in a sequence. Here, the `output_shape` has two values (since there are two non-batch dimensions in the output); the first dimension in the `output_shape` is `None`, because the sequence dimension `b` has an unknown shape.

    layer = keras.layers.EinsumDense("abc,cd->abd",

**Applying a dense layer to a sequence using ellipses**

This example shows how to instantiate a layer that applies the same dense operation to every element in a sequence, but uses the ellipsis notation instead of specifying the batch and sequence dimensions.

Because we are using ellipsis notation and have specified only one axis, the `output_shape` arg is a single value. When instantiated in this way, the layer can handle any number of sequence dimensions - including the case where no sequence dimension exists.

    layer = keras.layers.EinsumDense("...x,xy->...y",

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/einsum_dense.py#L320-L378)

enable_lora(
        rank,
        lora_alpha=None,
        a_initializer='he_uniform',
        b_initializer='zeros'
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/einsum_dense.py#L481-L489)

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