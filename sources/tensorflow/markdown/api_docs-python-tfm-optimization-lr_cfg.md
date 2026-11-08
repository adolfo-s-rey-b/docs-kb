[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.optimization.lr\_cfg Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/configs/learning_rate_config.py)

Dataclasses for learning rate schedule config.

Classes
-------

[`class ConstantLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ConstantLrConfig)
: Configuration for constant learning rate.

[`class CosineLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineLrConfig)
: Configuration for Cosine learning rate decay.

[`class DirectPowerLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerLrConfig)
: Configuration for DirectPower learning rate decay.

[`class ExponentialLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialLrConfig)
: Configuration for exponential learning rate decay.

[`class LinearWarmupConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LinearWarmupConfig)
: Configuration for linear warmup schedule config.

[`class PolynomialLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialLrConfig)
: Configuration for polynomial learning rate decay.

[`class PolynomialWarmupConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmupConfig)
: Configuration for linear warmup schedule config.

[`class PowerAndLinearDecayLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig)
: Configuration for DirectPower learning rate decay.

[`class PowerDecayWithOffsetLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffsetLrConfig)
: Configuration for power learning rate decay with step offset.

[`class StepCosineLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineLrConfig)
: Configuration for stepwise learning rate decay.

[`class StepwiseLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepwiseLrConfig)
: Configuration for stepwise learning rate decay.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.