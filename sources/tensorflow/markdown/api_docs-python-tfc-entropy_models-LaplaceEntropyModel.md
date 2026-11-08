[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#compress)
        
    *   [decode\_fn](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#decode_fn)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#decompress)
        
    *   [encode\_fn](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#encode_fn)
        
    *   [penalty](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#penalty)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#quantize)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.LaplaceEntropyModel Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#compress)
        
    *   [decode\_fn](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#decode_fn)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#decompress)
        
    *   [encode\_fn](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#encode_fn)
        
    *   [penalty](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#penalty)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#quantize)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LaplaceEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L27-L233)

Entropy model for Laplace distributed random variables.

tfc.entropy_models.LaplaceEntropyModel(
        coding_rank,
        l1=0.01,
        run_length_code=-1,
        magnitude_code=0,
        use_run_length_for_non_zeros=False,
        bottleneck_dtype=None
    )

This entropy model handles quantization and compression of a bottleneck tensor and implements a penalty that encourages compressibility under the Rice code.

Given a signed integer, `run_length_encode` encodes zeros using a run-length code, the sign using a uniform bit, and applies the Rice code to the magnitude.

The penalty applied by this class is given by:

l1 * reduce_sum(abs(x))

This encourages `x` to follow a symmetrized laplace distribution.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the estimated rate is summed over each coding unit in `bits()`. |
| `l1` | Float. L1 regularization factor. |
| `run_length_code` | Int. Rice code if >= 0 else Gamma code. |
| `magnitude_code` | Int. Rice code if >= 0 else Gamma code. |
| `use_run_length_for_non_zeros` | Bool. Whether to encode nonzero run lengths. |
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `bottleneck_dtype` | Data type of the bottleneck tensor. |
| `coding_rank` | Number of innermost dimensions considered a coding unit. |
| `l1` | L1 parameter. |
| `magnitude_code` | magnitude\_code parameter. |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `run_length_code` | run\_length\_code parameter. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `use_run_length_for_non_zeros` | use\_run\_length\_for\_non\_zeros parameter. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `compress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L173-L210)

compress(
        bottleneck
    )

Compresses a floating-point tensor.

Compresses the tensor to bit strings. `bottleneck` is first quantized as in `quantize()`, and then compressed using the run-length rice code. The quantized tensor can later be recovered by calling `decompress()`.

The innermost `self.coding_rank` dimensions are treated as one coding unit, i.e. are compressed into one string each. Any additional dimensions to the left are treated as batch dimensions.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions, containing a string for each coding unit. |     |

### `decode_fn`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L118-L124)

decode_fn(
        x, shape
    )

### `decompress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L212-L233)

decompress(
        strings, code_shape
    )

Decompresses a tensor.

Reconstructs the quantized tensor from bit strings produced by `compress()`.

|     |     |
| --- | --- |
| Args |     |
| `strings` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the compressed bit strings. |
| `code_shape` | Shape of innermost dimensions of the output [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape `tf.shape(strings) + code_shape`. |     |

### `encode_fn`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L111-L116)

encode_fn(
        x
    )

### `penalty`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L140-L154)

penalty(
        bottleneck
    )

Computes penalty encouraging compressibility.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions. |

|     |
| --- |
| Returns |     |
| Penalty value, which has the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions. |     |

### `quantize`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L156-L171)

quantize(
        bottleneck
    )

Quantizes a floating-point bottleneck tensor.

The tensor is rounded to integer values. The gradient of this rounding operation is overridden with the identity (straight-through gradient estimator).

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be quantized. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the quantized values. |     |

### `with_name_scope`

@classmethod

Decorator to automatically enter the module name scope.

    class MyModule(tf.Module):

Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s whose names included the module name:

    mod = MyModule()

|     |     |
| --- | --- |
| Args |     |
| `method` | The method to wrap. |

|     |
| --- |
| Returns |     |
| The original method wrapped such that it enters the module's name scope. |     |

### `__call__`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/laplace.py#L126-L138)

__call__(
        bottleneck
    )

Perturbs a tensor with (quantization) noise and computes penalty.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions. |

|     |
| --- |
| Returns |     |
| A tuple `(self.quantize(bottleneck), self.penalty(bottleneck))`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.