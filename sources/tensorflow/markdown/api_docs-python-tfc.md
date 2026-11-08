[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfc#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfc Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfc#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/__init__.py)

Data compression in TensorFlow.

Modules
-------

[`distributions`](https://www.tensorflow.org/api_docs/python/tfc/distributions)
 module: Distributions, based on [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)
.

[`entropy_models`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models)
 module: Entropy models.

[`layers`](https://www.tensorflow.org/api_docs/python/tfc/layers)
 module: Layers, based on [`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
.

[`ops`](https://www.tensorflow.org/api_docs/python/tfc/ops)
 module: TensorFlow operations and functions.

Classes
-------

[`class ContinuousBatchedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousBatchedEntropyModel)
: Batched entropy model for continuous random variables.

[`class ContinuousIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/ContinuousIndexedEntropyModel)
: Indexed entropy model for continuous random variables.

[`class DeepFactorized`](https://www.tensorflow.org/api_docs/python/tfc/distributions/DeepFactorized)
: Fully factorized distribution based on neural network cumulative.

[`class GDN`](https://www.tensorflow.org/api_docs/python/tfc/layers/GDN)
: Generalized divisive normalization layer.

[`class GDNParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/GDNParameter)
: Nonnegative parameterization as needed for GDN parameters.

[`class IdentityInitializer`](https://www.tensorflow.org/api_docs/python/tfc/layers/IdentityInitializer)
: Initialize to the identity kernel with the given shape.

[`class LocationScaleIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/LocationScaleIndexedEntropyModel)
: Indexed entropy model for location-scale family of random variables.

[`class MonotonicAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/MonotonicAdapter)
: Adapt a continuous distribution via an ascending monotonic function.

[`class NoisyDeepFactorized`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyDeepFactorized)
: `DeepFactorized` that is convolved with uniform noise.

[`class NoisyLaplace`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyLaplace)
: Laplacian distribution with additive i.i.d. uniform noise.

[`class NoisyLogistic`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyLogistic)
: Logistic distribution with additive i.i.d. uniform noise.

[`class NoisyLogisticMixture`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyLogisticMixture)
: Mixture of logistic distributions with additive i.i.d. uniform noise.

[`class NoisyMixtureSameFamily`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyMixtureSameFamily)
: Mixture of distributions with additive i.i.d. uniform noise.

[`class NoisyNormal`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormal)
: Gaussian distribution with additive i.i.d. uniform noise.

[`class NoisyNormalMixture`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyNormalMixture)
: Mixture of normal distributions with additive i.i.d. uniform noise.

[`class NoisyRoundedDeepFactorized`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyRoundedDeepFactorized)
: Rounded `DeepFactorized` + uniform noise.

[`class NoisyRoundedNormal`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisyRoundedNormal)
: Rounded normal distribution + uniform noise.

[`class NoisySoftRoundedDeepFactorized`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisySoftRoundedDeepFactorized)
: Soft rounded `DeepFactorized` + uniform noise.

[`class NoisySoftRoundedNormal`](https://www.tensorflow.org/api_docs/python/tfc/distributions/NoisySoftRoundedNormal)
: Soft rounded normal distribution + uniform noise.

[`class PackedTensors`](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors)
: Packed representation of compressed tensors.

[`class Parameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/Parameter)
: Reparameterized `Layer` variable.

[`class PowerLawEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/PowerLawEntropyModel)
: Entropy model for power-law distributed random variables.

[`class RDFTParameter`](https://www.tensorflow.org/api_docs/python/tfc/layers/RDFTParameter)
: RDFT reparameterization of a convolution kernel.

[`class RoundAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/RoundAdapter)
: Continuous density function + round.

[`class SignalConv1D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv1D)
: 1D convolution layer.

[`class SignalConv2D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv2D)
: 2D convolution layer.

[`class SignalConv3D`](https://www.tensorflow.org/api_docs/python/tfc/layers/SignalConv3D)
: 3D convolution layer.

[`class SoftRound`](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRound)
: Applies a differentiable approximation of rounding.

[`class SoftRoundAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/SoftRoundAdapter)
: Differentiable approximation to round.

[`class SoftRoundConditionalMean`](https://www.tensorflow.org/api_docs/python/tfc/layers/SoftRoundConditionalMean)
: Conditional mean of inputs given noisy soft rounded values.

[`class UniformNoiseAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/UniformNoiseAdapter)
: Additive i.i.d. uniform noise adapter distribution.

[`class UniversalBatchedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalBatchedEntropyModel)
: Batched entropy model model which implements Universal Quantization.

[`class UniversalIndexedEntropyModel`](https://www.tensorflow.org/api_docs/python/tfc/entropy_models/UniversalIndexedEntropyModel)
: Indexed entropy model model which implements Universal Quantization.

[`class Y4MDataset`](https://www.tensorflow.org/api_docs/python/tfc/Y4MDataset)
: A `tf.Dataset` of Y'CbCr video frames from '.y4m' files.

Functions
---------

[`create_range_decoder(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_decoder)
: Creates range decoder objects to be used by `EntropyDecode*` ops.

[`create_range_encoder(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/create_range_encoder)
: Creates range encoder objects to be used by `EntropyEncode*` ops.

[`entropy_decode_channel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_channel)
: Decodes the encoded stream inside `handle`.

[`entropy_decode_finalize(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize)
: Finalizes the decoding process.

[`entropy_decode_index(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_index)
: Decodes the encoded stream inside `handle`.

[`entropy_encode_channel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_channel)
: Encodes each input in `value`.

[`entropy_encode_finalize(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_finalize)
: Finalizes the encoding process and extracts byte stream from the encoder.

[`entropy_encode_index(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_encode_index)
: Encodes each input in `value` according to a distribution selected by `index`.

[`estimate_tails(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails)
: Estimates approximate tail quantiles.

[`lower_bound(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound)
: Same as [`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
, but with helpful gradient for `inputs < bound`.

[`lower_tail(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/lower_tail)
: Approximates lower tail quantile for range coding.

[`perturb_and_apply(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/perturb_and_apply)
: Perturbs the inputs of a pointwise function.

[`pmf_to_quantized_cdf(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/pmf_to_quantized_cdf)
: Converts a PMF into a quantized CDF for range coding.

[`quantization_offset(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset)
: Computes distribution-dependent quantization offset.

[`round_st(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/round_st)
: Straight-through round with optional quantization offset.

[`run_length_decode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_decode)
: Decodes `data` using run-length coding.

[`run_length_encode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_encode)
: Encodes `data` using run-length coding.

[`run_length_gamma_decode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_decode)
: Decodes `data` using run-length and Elias gamma coding.

[`run_length_gamma_encode(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/run_length_gamma_encode)
: Encodes `data` using run-length and Elias gamma coding.

[`same_padding_for_kernel(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/same_padding_for_kernel)
: Determine correct amount of padding for `same` convolution.

[`soft_round(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round)
: Differentiable approximation to `round`.

[`soft_round_conditional_mean(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_conditional_mean)
: Conditional mean of inputs given noisy soft rounded values.

[`soft_round_inverse(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/soft_round_inverse)
: Inverse of `soft_round`.

[`stochastic_round(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/stochastic_round)
: Rounds `inputs / step_size` stochastically.

[`upper_bound(...)`](https://www.tensorflow.org/api_docs/python/tfc/ops/upper_bound)
: Same as [`tf.minimum`](https://www.tensorflow.org/api_docs/python/tf/math/minimum)
, but with helpful gradient for `inputs > bound`.

[`upper_tail(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail)
: Approximates upper tail quantile for range coding.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.