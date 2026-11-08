[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#decompress)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.ContinuousIndexedEntropyModel Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#decompress)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#get_weights)
        
    *   [quantize](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#quantize)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L30-L428)

Indexed entropy model for continuous random variables.

#### View aliases

**Main aliases**

[`tfc.ContinuousIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel)

tfc.entropy_models.ContinuousIndexedEntropyModel(
        prior_fn,
        index_ranges,
        parameter_fns,
        coding_rank,
        channel_axis=-1,
        compression=False,
        stateless=False,
        expected_grads=False,
        tail_mass=(2 ** -8),
        range_coder_precision=12,
        bottleneck_dtype=None,
        prior_dtype=tf.float32,
        decode_sanity_check=True,
        laplace_tail_mass=0
    )

This entropy model handles quantization of a bottleneck tensor and helps with training of the parameters of the probability distribution modeling the tensor (a shared "prior" between sender and receiver). It also pre-computes integer probability tables, which can then be used to compress and decompress bottleneck tensors reliably across different platforms.

A typical workflow looks like this:

*   Train a model using an instance of this entropy model as a bottleneck, passing the bottleneck tensor through it. With `training=True`, the model computes a differentiable upper bound on the number of bits needed to compress the bottleneck tensor.
*   For evaluation, get a closer estimate of the number of compressed bits using `training=False`.
*   Instantiate an entropy model with `compression=True` (and the same parameters as during training), and share the model between a sender and a receiver.
*   On the sender side, compute the bottleneck tensor and call `compress()` on it. The output is a compressed string representation of the tensor. Transmit the string to the receiver, and call `decompress()` there. The output is the quantized bottleneck tensor. Continue processing the tensor on the receiving side.

This class assumes that all scalar elements of the encoded tensor are conditionally independent given some other random variable, possibly depending on data. All dependencies must be represented by the `indexes` tensor. For each bottleneck tensor element, it selects the appropriate scalar distribution.

The `indexes` tensor must contain only integer values in a pre-specified range (but may have floating-point type for purposes of backpropagation). To make the distribution conditional on `n`\-dimensional indexes, `index_ranges` must be specified as an iterable of `n` integers. `indexes` must have the same shape as the bottleneck tensor with an additional channel dimension of length `n`. The position of the channel dimension is given by `channel_axis`. The index values in the `k`th channel must be in the range `[0, index_ranges[k])`. If `index_ranges` has only one element (i.e. `n == 1`), `channel_axis` may be `None`. In that case, the additional channel dimension is omitted, and the `indexes` tensor must have the same shape as the bottleneck tensor.\
\
The implied distribution for the bottleneck tensor is determined as:\
\
prior_fn(**{k: f(indexes) for k, f in parameter_fns.items()})\
\
A more detailed description (and motivation) of this indexing scheme can be found in the following paper. Please cite the paper when using this code for derivative work.\
\
> "Integer Networks for Data Compression with Latent-Variable Models"  \
> J. Ballé, N. Johnston, D. Minnen  \
> [https://openreview.net/forum?id=S1zz2i0cY7](https://openreview.net/forum?id=S1zz2i0cY7)\
\
#### Examples:\
\
To make a parameterized zero-mean normal distribution, one could use:\
\
tfc.ContinuousIndexedEntropyModel(\
        prior_fn=tfc.NoisyNormal,\
        index_ranges=(64,),\
        parameter_fns=dict(\
            loc=lambda _: 0.,\
            scale=lambda i: tf.exp(i / 8 - 5),\
        ),\
        coding_rank=1,\
        channel_axis=None,\
    )\
\
Then, each element of `indexes` in the range `[0, 64)` would indicate that the corresponding element in `bottleneck` is normally distributed with zero mean and a standard deviation between `exp(-5)` and `exp(2.875)`, inclusive.\
\
To make a parameterized logistic mixture distribution, one could use:\
\
tfc.ContinuousIndexedEntropyModel(\
        prior_fn=tfc.NoisyLogisticMixture,\
        index_ranges=(10, 10, 5),\
        parameter_fns=dict(\
            loc=lambda i: i[..., 0:2] - 5,\
            scale=lambda _: 1,\
            weight=lambda i: tf.nn.softmax((i[..., 2:3] - 2) * [-1, 1]),\
        ),\
        coding_rank=1,\
        channel_axis=-1,\
    )\
\
Then, the last dimension of `indexes` would consist of triples of elements in the ranges `[0, 10)`, `[0, 10)`, and `[0, 5)`, respectively. Each triple would indicate that the element in `bottleneck` corresponding to the other dimensions is distributed with a mixture of two logistic distributions, where the components each have one of 10 location parameters between `-5` and `+4`, inclusive, unit scale parameters, and one of five different mixture weightings.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `prior_fn` | A callable returning a [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object, typically a `Distribution` class or factory function. This is a density model fitting the marginal distribution of the bottleneck data with additive uniform noise, which is shared a priori between the sender and the receiver. For best results, the distributions should be flexible enough to have a unit-width uniform distribution as a special case, since this is the marginal distribution for bottleneck dimensions that are constant. The callable will receive keyword arguments as determined by `parameter_fns`. |\
| `index_ranges` | Iterable of integers. `indexes` must have the same shape as the bottleneck tensor, with an additional dimension at position `channel_axis`. The values of the `k`th channel must be in the range `[0, index_ranges[k])`. |\
| `parameter_fns` | Dict of strings to callables. Functions mapping `indexes` to each distribution parameter. For each item, `indexes` is passed to the callable, and the string key and return value make up one keyword argument to `prior_fn`. |\
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the bits in the `__call__` method are summed over each coding unit. |\
| `channel_axis` | Integer or `None`. Determines the position of the channel axis in `indexes`. Defaults to the last dimension. If set to `None`, the index tensor is expected to have the same shape as the bottleneck tensor (only allowed when `index_ranges` has length 1). |\
| `compression` | Boolean. If set to `True`, the range coding tables used by `compress()` and `decompress()` will be built on instantiation. If set to `False`, these two methods will not be accessible. |\
| `stateless` | Boolean. If `False`, range coding tables are created as `Variable`s. This allows the entropy model to be serialized using the `SavedModel` protocol, so that both the encoder and the decoder use identical tables when loading the stored model. If `True`, creates range coding tables as `Tensor`s. This makes the entropy model stateless and allows it to be constructed within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> body, for when the range coding tables are provided manually. If `compression=False`, then `stateless=True` is implied and the provided value is ignored. |\
| `expected_grads` | If True, will use analytical expected gradients during backpropagation w.r.t. additive uniform noise. |\
| `tail_mass` | Float. Approximate probability mass which is encoded using an Elias gamma code embedded into the range coder. |\
| `range_coder_precision` | Integer. Precision passed to the range coding op. |\
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |\
| `prior_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of prior and probability computations. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |\
| `decode_sanity_check` | Boolean. If `True`, an raises an error if the binary strings passed into `decompress` are not completely decoded. |\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L354-L386)\
\
compress(\
        bottleneck, indexes\
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
| `indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> specifying the scalar distribution for each element in `bottleneck`. See class docstring for examples. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions, containing a string for each coding unit. |     |\
\
### `decompress`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L388-L417)\
\
decompress(\
        strings, indexes\
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
| `indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> specifying the scalar distribution for each output element. See class docstring for examples. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of the same shape as `indexes` (without the optional channel dimension). |     |\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L335-L352)\
\
quantize(\
        bottleneck\
    )\
\
Quantizes a floating-point tensor.\
\
To use this entropy model as an information bottleneck during training, pass a tensor through this function. The tensor is rounded to integer values.\
\
The gradient of this rounding operation is overridden with the identity (straight-through gradient estimator).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be quantized. |\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_indexed.py#L291-L333)\
\
__call__(\
        bottleneck, indexes, training=True\
    )\
\
Perturbs a tensor with (quantization) noise and estimates rate.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing the data to be compressed. |\
| `indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> specifying the scalar distribution for each element in `bottleneck`. See class docstring for examples. |\
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