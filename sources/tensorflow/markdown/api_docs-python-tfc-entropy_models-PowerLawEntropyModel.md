[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#decompress)
        
    *   [penalty](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#penalty)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#quantize)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.PowerLawEntropyModel Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#decompress)
        
    *   [penalty](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#penalty)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#quantize)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L27-L209)

Entropy model for power-law distributed random variables.

#### View aliases

**Main aliases**

[`tfc.PowerLawEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel)

tfc.entropy_models.PowerLawEntropyModel(
        coding_rank, alpha=0.01, bottleneck_dtype=None
    )

This entropy model handles quantization and compression of a bottleneck tensor and implements a penalty that encourages compressibility under the Elias gamma code.

The gamma code has code lengths `1 + 2 floor(log_2(x))`, for `x` a positive integer, and is close to optimal if `x` is distributed according to a power law. Being a universal code, it also guarantees that in the worst case, the expected code length is no more than 3 times the entropy of the empirical distribution of `x`, as long as probability decreases with increasing `x`. For details on the gamma code, see:

> "Universal Codeword Sets and Representations of the Integers"  
> P. Elias  
> [https://doi.org/10.1109/TIT.1975.1055349](https://doi.org/10.1109/TIT.1975.1055349)

Given a signed integer, `run_length_gamma_encode` encodes zeros using a run-length code, the sign using a uniform bit, and applies the gamma code to the magnitude.

The penalty applied by this class is given by:

log((abs(x) + alpha) / alpha)

This encourages `x` to follow a symmetrized power law, but only approximately for `alpha > 0`. Without `alpha`, the penalty would have a singularity at zero. Setting `alpha` to a small positive value ensures that the penalty is non-negative, and that its gradients are useful for optimization.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the estimated rate is summed over each coding unit in `bits()`. |
| `alpha` | Float. Regularization parameter preventing gradient singularity around zero. |
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `alpha` | Alpha parameter. |
| `bottleneck_dtype` | Data type of the bottleneck tensor. |
| `coding_rank` | Number of innermost dimensions considered a coding unit. |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `compress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L149-L186)

compress(
        bottleneck
    )

Compresses a floating-point tensor.

Compresses the tensor to bit strings. `bottleneck` is first quantized as in `quantize()`, and then compressed using the run-length gamma code. The quantized tensor can later be recovered by calling `decompress()`.

The innermost `self.coding_rank` dimensions are treated as one coding unit, i.e. are compressed into one string each. Any additional dimensions to the left are treated as batch dimensions.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions, containing a string for each coding unit. |     |

### `decompress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L188-L209)

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

### `penalty`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L116-L130)

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

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L132-L147)

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

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/power_law.py#L102-L114)

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