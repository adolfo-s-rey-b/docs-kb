[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.optimization.lr\_schedule Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py)

Learning rate schedule classes.

Classes
-------

[`class CosineDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset)
: A LearningRateSchedule that uses a cosine decay with optional warmup.

[`class DirectPowerDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay)
: Learning rate schedule follows lr \* (step)^power.

[`class ExponentialDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset)
: A LearningRateSchedule that uses an exponential decay schedule.

[`class LinearWarmup`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LinearWarmup)
: Linear warmup schedule.

[`class PiecewiseConstantDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset)
: A LearningRateSchedule that uses a piecewise constant decay schedule.

[`class PolynomialDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset)
: A LearningRateSchedule that uses a polynomial decay schedule.

[`class PolynomialWarmUp`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp)
: Applies polynomial warmup schedule on a given learning rate decay schedule.

[`class PowerAndLinearDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay)
: Learning rate schedule with multiplied by linear decay at the end.

[`class PowerDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset)
: Power learning rate decay with offset.

[`class StepCosineDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset)
: Stepwise cosine learning rate decay with offset.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.