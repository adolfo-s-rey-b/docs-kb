[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.distributions Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions#other-members)
    

Public API for tf.\_api.v2.distributions namespace

Classes
-------

[`class Bernoulli`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Bernoulli)
: Bernoulli distribution.

[`class Beta`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Beta)
: Beta distribution.

[`class Categorical`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Categorical)
: Categorical distribution.

[`class Dirichlet`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Dirichlet)
: Dirichlet distribution.

[`class DirichletMultinomial`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/DirichletMultinomial)
: Dirichlet-Multinomial compound distribution.

[`class Distribution`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Distribution)
: A generic probability distribution base class.

[`class Exponential`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Exponential)
: Exponential distribution.

[`class Gamma`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Gamma)
: Gamma distribution.

[`class Laplace`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Laplace)
: The Laplace distribution with location `loc` and `scale` parameters.

[`class Multinomial`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Multinomial)
: Multinomial distribution.

[`class Normal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Normal)
: The Normal distribution with location `loc` and `scale` parameters.

[`class RegisterKL`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/RegisterKL)
: Decorator to register a KL divergence implementation function.

[`class ReparameterizationType`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/ReparameterizationType)
: Instances of this class represent how sampling is reparameterized.

[`class StudentT`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/StudentT)
: Student's t-distribution.

[`class Uniform`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/Uniform)
: Uniform distribution with `low` and `high` parameters.

Functions
---------

[`kl_divergence(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/kl_divergence)
: Get the KL-divergence KL(distribution\_a || distribution\_b). (deprecated)

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| FULLY\_REPARAMETERIZED | Instance of [`tf.compat.v1.distributions.ReparameterizationType`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/ReparameterizationType) |
| NOT\_REPARAMETERIZED | Instance of [`tf.compat.v1.distributions.ReparameterizationType`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distributions/ReparameterizationType) |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.