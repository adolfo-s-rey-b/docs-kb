[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FTernaryDense&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#from_config)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.TernaryDense Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#from_config)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TernaryDense#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/layers/core/ternary_dense.py#L13-L287)

Densely-connected layer with Straight-Through Estimator ternary training.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.TernaryDense(
        units,
        threshold=None,
        activation=None,
        use_bias=True,
        kernel_initializer='glorot_uniform',
        bias_initializer='zeros',
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    )

Trains a dense layer whose weights are constrained to `{-1, 0, +1}` via a Straight-Through Estimator (STE). On every forward pass the float kernel is ternarized before the matrix multiply; gradients flow back through the quantization step as if it were the identity, keeping the underlying float weights trainable.

Quantization rule (BitNet b1.58, [https://arxiv.org/abs/2402.17764](https://arxiv.org/abs/2402.17764)
 §3.1):

kernel_ternary[i,j] = sign(kernel[i,j])  if |kernel[i,j]| > threshold
                          0                   otherwise
    output = beta * matmul(inputs, kernel_ternary) + bias

where `threshold` defaults to `0.5 * mean(|kernel|)` and `beta = mean(|kernel|)` per forward pass (both per the BitNet b1.58 §3.1 spec).

For post-training quantization of a regular `Dense` layer (no STE), use [`keras.layers.Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
 with `layer.quantize("ternary")` instead. That path packs the trained float kernel to `~1.58 bits/weight` for checkpoint storage.

Call `layer.quantize("ternary")` on a `TernaryDense` after training to freeze the ternarized kernel into a packed representation. The packed format stores `{-1, 0, +1}` weights at the information-theoretic floor of `log2(3) ~= 1.58` bits/value: five trits per byte (`3 ** 5 == 243 <= 256`), denser than int4 or int8.

**Checkpoint size.** `quantize("ternary")` stores weights at ~1.58 bits/value (~5× smaller than float32, ~2.5× smaller than int4).

**Inference note.** `quantize("ternary")` is a storage format, not a compute win: the packed kernel is unpacked to a full `{-1, 0, +1}` matrix on every forward pass and fed to a standard matmul, so inference is slightly slower than a plain `Dense` call. A native ternary kernel that reads the packed format directly would be needed for a speedup.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `units` | Positive integer, dimensionality of the output space. |
| `threshold` | Non-negative float or `None`. Quantization boundary applied element-wise to `\|kernel\|`. `None` (default) uses `0.5 * mean(\|kernel\|)` per forward pass, matching the BitNet b1.58 §3.1 rule. `0.0` maps every weight to ±1 (no zeros). Large values (e.g. `1e9`) yield an all-zero effective kernel. |
| `activation` | Activation function to use. Defaults to no activation (linear: `a(x) = x`). |
| `use_bias` | Boolean, whether the layer uses a bias vector. Defaults to `True`. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix. Defaults to `"glorot_uniform"`. |
| `bias_initializer` | Initializer for the bias vector. Defaults to `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Defaults to `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Defaults to `None`. |
| `activity_regularizer` | Regularizer function applied to the output of the layer. Defaults to `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Defaults to `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Defaults to `None`. |

|     |
| --- |
| Input shape<br>----------- |     |
| N-D tensor with shape `(batch_size, ..., input_dim)`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| N-D tensor with shape `(batch_size, ..., units)`. |     |

#### Example:

    layer = keras.layers.TernaryDense(64)

Quantize for export and inference (kernel stored at ~1.6 bits/value):

    layer = keras.layers.TernaryDense(64)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `kernel` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/ops/operation.py#L329-L369)

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

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| lora\_enabled | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.