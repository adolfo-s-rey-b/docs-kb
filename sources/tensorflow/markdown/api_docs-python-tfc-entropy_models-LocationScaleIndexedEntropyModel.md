[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#decompress)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.LocationScaleIndexedEntropyModel Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#decompress)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L431-L633)

Indexed entropy model for location-scale family of random variables.

Inherits From: [`ContinuousIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel)

#### View aliases

**Main aliases**

[`tfc.LocationScaleIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel)

tfc.entropy_models.LocationScaleIndexedEntropyModel(
        prior_fn,
        num_scales,
        scale_fn,
        coding_rank,
        compression=False,
        stateless=False,
        expected_grads=False,
        tail_mass=(2 ** -8),
        range_coder_precision=12,
        bottleneck_dtype=None,
        prior_dtype=tf.float32,
        laplace_tail_mass=0
    )

This class is a common special case of `ContinuousIndexedEntropyModel`. The specified distribution is parameterized with `num_scales` values of scale parameters. An element-wise location parameter is handled by shifting the distributions to zero.

This method is illustrated in Figure 10 of:

> "Nonlinear Transform Coding"  
> J. Ballé, P.A. Chou, D. Minnen, S. Singh, N. Johnston, E. Agustsson, S.J. Hwang, G. Toderici  
> [https://doi.org/10.1109/JSTSP.2020.3034501](https://doi.org/10.1109/JSTSP.2020.3034501)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `prior_fn` | A callable returning a [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object, typically a `Distribution` class or factory function. This is a density model fitting the marginal distribution of the bottleneck data with additive uniform noise, which is shared a priori between the sender and the receiver. For best results, the distributions should be flexible enough to have a unit-width uniform distribution as a special case, since this is the marginal distribution for bottleneck dimensions that are constant. The callable will receive keyword arguments as determined by `parameter_fns`. |
| `num_scales` | Integer. Values in `indexes` must be in the range `[0, num_scales)`. |\
| `scale_fn` | Callable. `indexes` is passed to the callable, and the return value is given as `scale` keyword argument to `prior_fn`. |\
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the bits in the `__call__` method are summed over each coding unit. |\
| `compression` | Boolean. If set to `True`, the range coding tables used by `compress()` and `decompress()` will be built on instantiation. If set to `False`, these two methods will not be accessible. |\
| `stateless` | Boolean. If `False`, range coding tables are created as `Variable`s. This allows the entropy model to be serialized using the `SavedModel` protocol, so that both the encoder and the decoder use identical tables when loading the stored model. If `True`, creates range coding tables as `Tensor`s. This makes the entropy model stateless and allows it to be constructed within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> body, for when the range coding tables are provided manually. If `compression=False`, then `stateless=True` is implied and the provided value is ignored. |\
| `expected_grads` | If True, will use analytical expected gradients during backpropagation w.r.t. additive uniform noise. |\
| `tail_mass` | Float. Approximate probability mass which is encoded using an Elias gamma code embedded into the range coder. |\
| `range_coder_precision` | Integer. Precision passed to the range coding op. |\
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |\
| `prior_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of prior and probability computations. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |\
| `laplace_tail_mass` | Float, or a float-valued tf.Tensor. If positive, will augment the prior with a `NoisyLaplace` mixture component for training stability. (experimental) |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `bottleneck_dtype` | Data type of the bottleneck tensor. |\
| `cdf` | The CDFs used by range coding. |\
| `cdf_offset` | The CDF offsets used by range coding. |\
| `channel_axis` | Position of channel axis in `indexes` tensor. |\
| `coding_rank` | Number of innermost dimensions considered a coding unit. |\
| `compression` | Whether this entropy model is prepared for compression. |\
| `expected_grads` | Whether to use analytical expected gradients during backpropagation. |\
| `index_ranges` | Upper bound(s) on values allowed in `indexes` tensor. |\
| `laplace_tail_mass` | Whether to augment the prior with a `NoisyLaplace` mixture. |\
| `name` | Returns the name of this module as passed or determined in the ctor. |\
| `name_scope` | Returns a [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br> instance for this class. |\
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |\
| `parameter_fns` | Functions mapping `indexes` to each distribution parameter. |\
| `prior` | Prior distribution, used for deriving range coding tables. |\
| `prior_dtype` | Data type of `prior`. |\
| `prior_fn` | Class or factory function returning a `Distribution` object. |\
| `range_coder_precision` | Precision used in range coding op. |\
| `stateless` | Whether range coding tables are created as `Tensor`s or `Variable`s. |\
| `submodules` | Sequence of all sub-modules.<br><br>Submodules are modules which are properties of this module, or found as properties of modules which are properties of this module (and so on).<br><br>    a = tf.Module() |\
| `tail_mass` | Approximate probability mass which is range encoded with overflow. |\
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |\
| `variables` | Sequence of variables owned by this module and its submodules. |\
\
Methods\
-------\
\
### `compress`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L581-L610)\
\
compress(\
        bottleneck, scale_indexes, loc=None\
    )\
\
Compresses a floating-point tensor.\
\
Compresses the tensor to bit strings. `bottleneck` is first quantized as in `quantize()`, and then compressed using the probability tables derived from `indexes`. The quantized tensor can later be recovered by calling `decompress()`.\
\
The innermost `self.coding_rank` dimensions are treated as one coding unit, i.e. are compressed into one string each. Any additional dimensions to the left are treated as batch dimensions.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. |\
| `scale_indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> indexing the scale parameter for each element in `bottleneck`. Must have the same shape as `bottleneck`. |\
| `loc` | `None` or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. If `None`, the location parameter for all elements is assumed to be zero. Otherwise, specifies the location parameter for each element in `bottleneck`. Must have the same shape as `bottleneck`. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions, containing a string for each coding unit. |     |\
\
### `decompress`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L612-L633)\
\
decompress(\
        strings, scale_indexes, loc=None\
    )\
\
Decompresses a tensor.\
\
Reconstructs the quantized tensor from bit strings produced by `compress()`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `strings` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the compressed bit strings. |\
| `scale_indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> indexing the scale parameter for each output element. |\
| `loc` | `None` or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. If `None`, the location parameter for all output elements is assumed to be zero. Otherwise, specifies the location parameter for each output element. Must have the same shape as `scale_indexes`. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the same shape as `scale_indexes`. |     |\
\
### `from_config`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L424-L428)\
\
@classmethod\
\
Instantiates an entropy model from a configuration dictionary.\
\
### `get_config`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L419-L422)\
\
get_config()\
\
Returns the configuration of the entropy model.\
\
### `get_weights`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_base.py#L362-L363)\
\
get_weights()\
\
### `quantize`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L557-L579)\
\
quantize(\
        bottleneck, loc=None\
    )\
\
Quantizes a floating-point tensor.\
\
To use this entropy model as an information bottleneck during training, pass a tensor through this function. The tensor is rounded to integer values modulo the location parameters of the prior distribution given in `loc`.\
\
The gradient of this rounding operation is overridden with the identity (straight-through gradient estimator).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be quantized. |\
| `loc` | `None` or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. If `None`, the location parameter for all elements is assumed to be zero. Otherwise, specifies the location parameter for each element in `bottleneck`. Must have the same shape as `bottleneck`. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the quantized values. |     |\
\
### `set_weights`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_base.py#L365-L370)\
\
set_weights(\
        weights\
    )\
\
### `with_name_scope`\
\
@classmethod\
\
Decorator to automatically enter the module name scope.\
\
    class MyModule(tf.Module):\
\
Using the above module would produce [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)\
s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
s whose names included the module name:\
\
    mod = MyModule()\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `method` | The method to wrap. |\
\
|     |\
| --- |\
| Returns |     |\
| The original method wrapped such that it enters the module's name scope. |     |\
\
### `__call__`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L526-L555)\
\
__call__(\
        bottleneck, scale_indexes, loc=None, training=True\
    )\
\
Perturbs a tensor with (quantization) noise and estimates rate.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. |\
| `scale_indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> indexing the scale parameter for each element in `bottleneck`. Must have the same shape as `bottleneck`. |\
| `loc` | `None` or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. If `None`, the location parameter for all elements is assumed to be zero. Otherwise, specifies the location parameter for each element in `bottleneck`. Must have the same shape as `bottleneck`. |\
| `training` | Boolean. If `False`, computes the Shannon information of `bottleneck` under the distribution computed by `self.prior_fn`, which is a non-differentiable, tight _lower_ bound on the number of bits needed to compress `bottleneck` using `compress()`. If `True`, returns a somewhat looser, but differentiable _upper_ bound on this quantity. |\
\
|     |\
| --- |\
| Returns |     |\
| A tuple (bottleneck\_perturbed, bits) where `bottleneck_perturbed` is `bottleneck` perturbed with (quantization) noise and `bits` is the rate. `bits` has the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.