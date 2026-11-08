[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/distributions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/distributions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/distributions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc/distributions#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc/distributions#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfc.distributions Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfc/distributions#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfc/distributions#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/distributions/__init__.py)

Distributions, based on [`tfp.distributions.Distribution`](https://www.tensorflow.org/probability/api_docs/python/tfp/distributions/Distribution)
.

Classes
-------

[`class DeepFactorized`](https://www.tensorflow.org/api_docs/python/tfc/distributions/DeepFactorized)
: Fully factorized distribution based on neural network cumulative.

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

[`class RoundAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/RoundAdapter)
: Continuous density function + round.

[`class SoftRoundAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/SoftRoundAdapter)
: Differentiable approximation to round.

[`class UniformNoiseAdapter`](https://www.tensorflow.org/api_docs/python/tfc/distributions/UniformNoiseAdapter)
: Additive i.i.d. uniform noise adapter distribution.

Functions
---------

[`estimate_tails(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/estimate_tails)
: Estimates approximate tail quantiles.

[`lower_tail(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/lower_tail)
: Approximates lower tail quantile for range coding.

[`quantization_offset(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/quantization_offset)
: Computes distribution-dependent quantization offset.

[`upper_tail(...)`](https://www.tensorflow.org/api_docs/python/tfc/distributions/upper_tail)
: Approximates upper tail quantile for range coding.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.