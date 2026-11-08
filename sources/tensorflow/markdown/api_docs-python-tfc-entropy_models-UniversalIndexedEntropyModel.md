[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#decompress)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.entropy\_models.UniversalIndexedEntropyModel Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#methods)
    *   [compress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#compress)
        
    *   [decompress](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#decompress)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#get_config)
        
    *   [get\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#get_weights)
        
    *   [set\_weights](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#set_weights)
        
    *   [with\_name\_scope](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#with_name_scope)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/universal.py#L307-L603)

Indexed entropy model model which implements Universal Quantization.

#### View aliases

**Main aliases**

[`tfc.UniversalIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel)

tfc.entropy_models.UniversalIndexedEntropyModel(
        prior_fn,
        index_ranges,
        parameter_fns,
        coding_rank,
        compression=False,
        laplace_tail_mass=0.0,
        expected_grads=False,
        tail_mass=(2 ** -8),
        range_coder_precision=12,
        bottleneck_dtype=None,
        prior_dtype=tf.float32,
        stateless=False,
        num_noise_levels=15,
        decode_sanity_check=True
    )

In contrast to the base class, which uses rounding for quantization, here "quantization" is performed additive uniform noise, which is implemented with Universal Quantization.

This is described in Sec. 3.2. in the paper

> "Universally Quantized Neural Compression"  
> Eirikur Agustsson & Lucas Theis  
> [https://arxiv.org/abs/2006.09952](https://arxiv.org/abs/2006.09952)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `prior_fn` | A callable returning a [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)<br> object, typically a `Distribution` class or factory function. This is a density model fitting the marginal distribution of the bottleneck data with additive uniform noise, which is shared a priori between the sender and the receiver. For best results, the distributions should be flexible enough to have a unit-width uniform distribution as a special case, since this is the marginal distribution for bottleneck dimensions that are constant. The callable will receive keyword arguments as determined by `parameter_fns`. |
| `index_ranges` | Iterable of integers. Compared to `bottleneck`, `indexes` in `__call__()` must have an additional trailing dimension, and the values of the `k`th channel must be in the range `[0, index_ranges[k])`. |\
| `parameter_fns` | Dict of strings to callables. Functions mapping `indexes` to each distribution parameter. For each item, `indexes` is passed to the callable, and the string key and return value make up one keyword argument to `prior_fn`. |\
| `coding_rank` | Integer. Number of innermost dimensions considered a coding unit. Each coding unit is compressed to its own bit string, and the `bits()` method sums over each coding unit. |\
| `compression` | Boolean. If set to `True`, the range coding tables used by `compress()` and `decompress()` will be built on instantiation. This assumes eager mode (throws an error if in graph mode or inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> call). If set to `False`, these two methods will not be accessible. |\
| `laplace_tail_mass` | Float. If positive, will augment the prior with a laplace mixture for training stability. (experimental) |\
| `expected_grads` | If True, will use analytical expected gradients during backpropagation w.r.t. additive uniform noise. |\
| `tail_mass` | Float. Approximate probability mass which is encoded using an Elias gamma code embedded into the range coder. |\
| `range_coder_precision` | Integer. Precision passed to the range coding op. |\
| `bottleneck_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of bottleneck tensor. Defaults to [`tf.keras.mixed_precision.global_policy().compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |\
| `prior_dtype` | [`tf.dtypes.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>. Data type of prior and probability computations. Defaults to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br>. |\
| `stateless` | Boolean. If True, creates range coding tables as `Tensor`s rather than `Variable`s. |\
| `num_noise_levels` | Integer. The number of levels used to quantize the uniform noise. |\
| `decode_sanity_check` | Boolean. If `True`, an raises an error if the binary strings passed into `decompress` are not completely decoded. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `bottleneck_dtype` | Data type of the bottleneck tensor. |\
| `cdf` | The CDFs used by range coding. |\
| `cdf_offset` | The CDF offsets used by range coding. |\
| `coding_rank` | Number of innermost dimensions considered a coding unit. |\
| `compression` | Whether this entropy model is prepared for compression. |\
| `expected_grads` | Whether to use analytical expected gradients during backpropagation. |\
| `index_ranges` | Upper bound(s) on values allowed in `indexes` tensor. |\
| `index_ranges_without_offsets` | Upper bound(s) on values allowed in `indexes` , excluding offsets. |\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/universal.py#L533-L567)\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/universal.py#L569-L599)\
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
### `get_config`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/universal.py#L601-L603)\
\
get_config()\
\
Returns the configuration of the entropy model.\
\
|     |\
| --- |\
| Returns |     |\
| A JSON-serializable Python dict. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `RuntimeError` | on attempting to call this method on an entropy model with `compression=False` or with `stateless=True`. |\
\
### `get_weights`\
\
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/continuous_base.py#L362-L363)\
\
get_weights()\
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
[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/entropy_models/universal.py#L481-L531)\
\
__call__(\
        bottleneck, indexes, training=True\
    )\
\
Perturbs a tensor with additive uniform noise and estimates bitcost.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `bottleneck` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> containing a non-perturbed bottleneck. Must have at least `self.coding_rank` dimensions. |\
| `indexes` | [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> specifying the scalar distribution for each element in `bottleneck`. See class docstring for examples. |\
| `training` | Boolean. If `False`, computes the bitcost using discretized uniform noise. If `True`, estimates the differential entropy with uniform noise. |\
\
|     |\
| --- |\
| Returns |     |\
| A tuple (bottleneck\_perturbed, bits) where `bottleneck_perturbed` is `bottleneck` perturbed with nosie and `bits` is the bitcost of transmitting such a sample having the same shape as `bottleneck` without the `self.coding_rank` innermost dimensions. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.