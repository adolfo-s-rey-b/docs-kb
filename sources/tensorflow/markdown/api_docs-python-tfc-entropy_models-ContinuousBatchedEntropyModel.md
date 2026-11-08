[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#decompress)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.ContinuousBatchedEntropyModel Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#decompress)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L32-L436)

Batched entropy model for continuous random variables.

#### View aliases

**Main aliases**

[`tfc.ContinuousBatchedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel)

tfc.entropy_models.ContinuousBatchedEntropyModel(
        prior=None,
        coding_rank=None,
        compression=False,
        stateless=False,
        expected_grads=False,
        tail_mass=(2 ** -8),
        range_coder_precision=12,
        bottleneck_dtype=None,
        prior_shape=None,
        cdf=None,
        cdf_offset=None,
        cdf_shapes=None,
        offset_heuristic=True,
        quantization_offset=None,
        decode_sanity_check=True,
        laplace_tail_mass=0
    )

This entropy model handles quantization of a bottleneck tensor and helps with training of the parameters of the probability distribution modeling the tensor (a shared "prior" between sender and receiver). It also pre-computes integer probability tables, which can then be used to compress and decompress bottleneck tensors reliably across different platforms.

A typical workflow looks like this:

*   Train a model using an instance of this entropy model as a bottleneck, passing the bottleneck tensor through it. With `training=True`, the model computes a differentiable upper bound on the number of bits needed to compress the bottleneck tensor.
*   For evaluation, get a closer estimate of the number of compressed bits using `training=False`.
*   Instantiate an entropy model with `compression=True` (and the same parameters as during training), and share the model between a sender and a receiver.
*   On the sender side, compute the bottleneck tensor and call `compress()` on it. The output is a compressed string representation of the tensor. Transmit the string to the receiver, and call `decompress()` there. The output is the quantized bottleneck tensor. Continue processing the tensor on the receiving side.

This class assumes that all scalar elements of the encoded tensor are statistically independent, and that the parameters of their scalar distributions do not depend on data. The innermost dimensions of the bottleneck tensor must be broadcastable to the batch shape of `prior`. Any dimensions to the left of the batch shape are assumed to be i.i.d., i.e. the likelihoods are broadcast to the bottleneck tensor accordingly.

A more detailed description (and motivation) of this way of performing quantization and range coding can be found in the following paper. Please cite the paper when using this code for derivative work.

> "End-to-end Optimized Image Compression"  
> J. Ballé, V. Laparra, E.P. Simoncelli  
> [https://openreview.net/forum?id=rJxdQ3jeg](https://openreview.net/forum?id=rJxdQ3jeg)

Entropy models which contain range coding tables (i.e. with `compression=True`) can be instantiated in three ways:

*   By providing a continuous "prior" distribution object. The range coding tables are then derived from that continuous distribution.
*   From a config as returned by `get_config`, followed by a call to `set_weights`. This implements the Keras serialization protocol. In this case, the initializer creates empty state variables for the range coding tables, which are then filled by `set_weights`. As a consequence, this method requires `stateless=False`.
*   In a more low-level way, by directly providing the range coding tables to `__init__`, for use cases where the Keras protocol can't be used (e.g., when the entropy model must not create variables).

The `quantization_offset` and `offset_heuristic` arguments control whether quantization is performed with respect to integer values, or potentially non-integer offsets (i.e., `y = tf.round(x - o) + o`). There are three modes of operation:

*   If `quantization_offset` is provided manually (not `None`), these values are used and `offset_heuristic` is ineffective.
*   Otherwise, if `offset_heuristic and compression`, the offsets are computed once on initialization, and then fixed. If the entropy model is serialized, they are preserved.
*   Otherwise, if `offset_heuristic and not compression`, the offsets are recomputed every time quantization is performed. Note this may be computationally expensive when the prior does not have a mode that is computable in closed form (e.g. for `NoisyDeepFactorized`).

This offset heuristic is discussed in Section III.A of:

> "Nonlinear Transform Coding"  
> J. Ballé, P.A. Chou, D. Minnen, S. Singh, N. Johnston, E. Agustsson, S.J. Hwang, G. Toderici  
> [https://doi.org/10.1109/JSTSP.2020.3034501](https://doi.org/10.1109/JSTSP.2020.3034501)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `prior` | A [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object. A density model fitting the marginal distribution of the bottleneck data with additive uniform noise, which is shared a priori between the sender and the receiver. For best results, the distribution should be flexible enough to have a unit-width uniform distribution as a special case, since this is the marginal distribution for bottleneck dimensions that are constant. The distribution parameters may not depend on data (they must be either variables or constants). |
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the bits in the **call** method are summed over each coding unit. |
| `compression` | Boolean. If set to `True`, the range coding tables used by `compress()` and `decompress()` will be built on instantiation. If set to `False`, these two methods will not be accessible. |
| `stateless` | Boolean. If `False`, range coding tables are created as `Variable`s. This allows the entropy model to be serialized using the `SavedModel` protocol, so that both the encoder and the decoder use identical tables when loading the stored model. If `True`, creates range coding tables as `Tensor`s. This makes the entropy model stateless and allows it to be constructed within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> body, for when the range coding tables are provided manually. If `compression=False`, then `stateless=True` is implied and the provided value is ignored. |
| `expected_grads` | If True, will use analytical expected gradients during backpropagation w.r.t. additive uniform noise. |
| `tail_mass` | Float. Approximate probability mass which is encoded using an Elias gamma code embedded into the range coder. |
| `range_coder_precision` | Integer. Precision passed to the range coding op. |
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |
| `prior_shape` | Batch shape of the prior (dimensions which are not assumed i.i.d.). Must be provided if `prior` is omitted. |
| `cdf` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`. If provided, is used for range coding rather than tables built from the prior. |
| `cdf_offset` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`. Must be provided along with `cdf`. |
| `cdf_shapes` | Shapes of `cdf` and `cdf_offset`. If provided, empty range coding tables are created, which can then be restored using `set_weights`. Requires `compression=True` and `stateless=False`. |
| `offset_heuristic` | Boolean. Whether to quantize to non-integer offsets heuristically determined from mode/median of prior. Set this to `False` if you are using soft quantization during training. |
| `quantization_offset` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or `None`. The quantization offsets to use. If provided (not `None`), then `offset_heuristic` is ineffective. |
| `decode_sanity_check` | Boolean. If `True`, an raises an error if the binary strings passed into `decompress` are not completely decoded. |
| `laplace_tail_mass` | Float, or a float-valued tf.Tensor. If positive, will augment the prior with a `NoisyLaplace` mixture component for training stability. (experimental) |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `bottleneck_dtype` | Data type of the bottleneck tensor. |
| `cdf` | The CDFs used by range coding. |
| `cdf_offset` | The CDF offsets used by range coding. |
| `coding_rank` | Number of innermost dimensions considered a coding unit. |
| `compression` | Whether this entropy model is prepared for compression. |
| `expected_grads` | Whether to use analytical expected gradients during backpropagation. |
| `laplace_tail_mass` | Whether to augment the prior with a `NoisyLaplace` mixture. |
| `name` | Returns the name of this module as passed or determined in the ctor. |
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
| `offset_heuristic` | Whether to use heuristic to determine quantization offsets. |
| `prior` | Prior distribution, used for deriving range coding tables. |
| `prior_shape` | Batch shape of `prior` (dimensions which are not assumed i.i.d.). |
| `prior_shape_tensor` | Batch shape of `prior` as a `Tensor`. |
| `quantization_offset` | The quantization offset used in `quantize` and `compress`. |
| `range_coder_precision` | Precision used in range coding op. |
| `stateless` | Whether range coding tables are created as `Tensor`s or `Variable`s. |
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |
| `tail_mass` | Approximate probability mass which is range encoded with overflow. |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |
| `variables` | Sequence of variables owned by this module and its submodules. |

Methods
-------

### `compress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L347-L383)

compress(
        bottleneck
    )

Compresses a floating-point tensor.

Compresses the tensor to bit strings. `bottleneck` is first quantized as in `quantize()`, and then compressed using the probability tables in `self.cdf` (derived from `self.prior`). The quantized tensor can later be recovered by calling `decompress()`.

The innermost `self.coding_rank` dimensions are treated as one coding unit, i.e. are compressed into one string each. Any additional dimensions to the left are treated as batch dimensions.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions, and the innermost dimensions must be broadcastable to `self.prior_shape`. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions, containing a string for each coding unit. |     |

### `decompress`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L385-L422)

decompress(
        strings, broadcast_shape
    )

Decompresses a tensor.

Reconstructs the quantized tensor from bit strings produced by `compress()`. It is necessary to provide a part of the output shape in `broadcast_shape`.

|     |     |
| --- | --- |
| Args |     |
| `strings` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the compressed bit strings. |
| `broadcast_shape` | Iterable of ints. The part of the output tensor shape between the shape of `strings` on the left and `self.prior_shape` on the right. This must match the shape of the input to `compress()`. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of shape `strings.shape + broadcast_shape + self.prior_shape`. |     |

### `get_config`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L424-L436)

get_config()

Returns the configuration of the entropy model.

|     |
| --- |
| Returns |     |
| A JSON-serializable Python dict. |     |

### `get_weights`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_base.py#L362-L363)

get_weights()

### `quantize`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L324-L345)

quantize(
        bottleneck
    )

Quantizes a floating-point bottleneck tensor.

The tensor is rounded to integer values potentially shifted by offsets (if `self.quantization_offset is not None`). These offsets can depend on `self.prior`. For instance, for a Gaussian distribution, when `self.offset_heuristic == True`, the returned values would be rounded to the location of the mode of the distribution plus or minus an integer.

The gradient of this rounding operation is overridden with the identity (straight-through gradient estimator).

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be quantized. The innermost dimensions must be broadcastable to `self.prior_shape`. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the quantized values. |     |

### `set_weights`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_base.py#L365-L370)

set_weights(
        weights
    )

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

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_batched.py#L291-L322)

__call__(
        bottleneck, training=True
    )

Perturbs a tensor with (quantization) noise and estimates rate.

|     |     |
| --- | --- |
| Args |     |
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. Must have at least `self.coding_rank` dimensions, and the innermost dimensions must be broadcastable to `self.prior_shape`. |
| `training` | Boolean. If `False`, computes the Shannon information of `bottleneck` under the distribution `self.prior`, which is a non-differentiable, tight _lower_ bound on the number of bits needed to compress `bottleneck` using `compress()`. If `True`, returns a somewhat looser, but differentiable _upper_ bound on this quantity. |

|     |
| --- |
| Returns |     |
| A tuple (bottleneck\_perturbed, bits) where `bottleneck_perturbed` is `bottleneck` perturbed with (quantization) noise, and `bits` is the rate. `bits` has the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.