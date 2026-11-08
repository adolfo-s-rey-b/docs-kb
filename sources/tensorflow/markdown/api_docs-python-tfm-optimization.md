[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/optimization#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/optimization#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.optimization Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/optimization#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/optimization#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/__init__.py)

Optimization package definition.

Modules
-------

[`adafactor_optimizer`](https://www.tensorflow.org/api_docs/python/tfm/optimization/adafactor_optimizer)
 module: Adafactor optimizer.

[`base_config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/base_config)
 module: Base configurations to standardize experiments.

[`configs`](https://www.tensorflow.org/api_docs/python/tfm/optimization/configs)
 module

[`ema_optimizer`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ema_optimizer)
 module: Exponential moving average optimizer.

[`lamb`](https://www.tensorflow.org/api_docs/python/tfm/optimization/lamb)
 module: Layer-wise Adaptive Moments (LAMB) optimizer.

[`lars`](https://www.tensorflow.org/api_docs/python/tfm/optimization/lars)
 module: Layer-wise adaptive rate scaling optimizer.

[`legacy_adamw`](https://www.tensorflow.org/api_docs/python/tfm/optimization/legacy_adamw)
 module: Adam optimizer with weight decay that exactly matches the original BERT.

[`lr_cfg`](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_cfg)
 module: Dataclasses for learning rate schedule config.

[`lr_schedule`](https://www.tensorflow.org/api_docs/python/tfm/optimization/lr_schedule)
 module: Learning rate schedule classes.

[`oneof`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/oneof)
 module: Config class that supports oneof functionality.

[`opt_cfg`](https://www.tensorflow.org/api_docs/python/tfm/optimization/opt_cfg)
 module: Dataclasses for optimizer configs.

[`optimizer_factory`](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory)
 module: Optimizer factory class.

[`slide_optimizer`](https://www.tensorflow.org/api_docs/python/tfm/optimization/slide_optimizer)
 module: SLIDE optimizer.

Classes
-------

[`class AdafactorConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorConfig)
: Configuration for Adafactor optimizer.

[`class AdafactorKerasConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdafactorKerasConfig)
: Configuration for AdafactorKeras optimizer.

[`class AdagradConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdagradConfig)
: Configuration for Adagrad optimizer.

[`class AdamConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdamConfig)
: Configuration for Adam optimizer.

[`class AdamExperimentalConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdamExperimentalConfig)
: Configuration for experimental Adam optimizer.

[`class AdamWeightDecayConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdamWeightDecayConfig)
: Configuration for Adam optimizer with weight decay.

[`class AdamWeightDecayExperimentalConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/AdamWeightDecayExperimentalConfig)
: Configuration for Adam optimizer with weight decay.

[`class BaseOptimizerConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/BaseOptimizerConfig)
: Base optimizer config.

[`class ConstantLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ConstantLrConfig)
: Configuration for constant learning rate.

[`class CosineDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineDecayWithOffset)
: A LearningRateSchedule that uses a cosine decay with optional warmup.

[`class CosineLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/CosineLrConfig)
: Configuration for Cosine learning rate decay.

[`class DirectPowerDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay)
: Learning rate schedule follows lr \* (step)^power.

[`class DirectPowerLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerLrConfig)
: Configuration for DirectPower learning rate decay.

[`class EMAConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/EMAConfig)
: Exponential moving average optimizer config.

[`class ExponentialDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialDecayWithOffset)
: A LearningRateSchedule that uses an exponential decay schedule.

[`class ExponentialLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialLrConfig)
: Configuration for exponential learning rate decay.

[`class ExponentialMovingAverage`](https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage)
: Optimizer that computes an exponential moving average of the variables.

[`class LAMBConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LAMBConfig)
: Configuration for LAMB optimizer.

[`class LARSConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LARSConfig)
: Layer-wise adaptive rate scaling config.

[`class LinearWarmup`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LinearWarmup)
: Linear warmup schedule.

[`class LinearWarmupConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LinearWarmupConfig)
: Configuration for linear warmup schedule config.

[`class LrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/LrConfig)
: Configuration for lr schedule.

[`class OptimizationConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizationConfig)
: Configuration for optimizer and learning rate schedule.

[`class OptimizerConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerConfig)
: Configuration for optimizer.

[`class OptimizerFactory`](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory)
: Optimizer factory class.

[`class PiecewiseConstantDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PiecewiseConstantDecayWithOffset)
: A LearningRateSchedule that uses a piecewise constant decay schedule.

[`class PolynomialDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialDecayWithOffset)
: A LearningRateSchedule that uses a polynomial decay schedule.

[`class PolynomialLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialLrConfig)
: Configuration for polynomial learning rate decay.

[`class PolynomialWarmUp`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp)
: Applies polynomial warmup schedule on a given learning rate decay schedule.

[`class PolynomialWarmupConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmupConfig)
: Configuration for linear warmup schedule config.

[`class PowerAndLinearDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay)
: Learning rate schedule with multiplied by linear decay at the end.

[`class PowerAndLinearDecayLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecayLrConfig)
: Configuration for DirectPower learning rate decay.

[`class PowerDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset)
: Power learning rate decay with offset.

[`class PowerDecayWithOffsetLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffsetLrConfig)
: Configuration for power learning rate decay with step offset.

[`class RMSPropConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/RMSPropConfig)
: Configuration for RMSProp optimizer.

[`class SGDConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/SGDConfig)
: Configuration for SGD optimizer.

[`class SGDExperimentalConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/SGDExperimentalConfig)
: Configuration for SGD optimizer.

[`class SLIDEConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/SLIDEConfig)
: Configuration for SLIDE optimizer.

[`class StepCosineDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset)
: Stepwise cosine learning rate decay with offset.

[`class StepCosineLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineLrConfig)
: Configuration for stepwise learning rate decay.

[`class StepwiseLrConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepwiseLrConfig)
: Configuration for stepwise learning rate decay.

[`class WarmupConfig`](https://www.tensorflow.org/api_docs/python/tfm/optimization/WarmupConfig)
: Configuration for lr schedule.

Functions
---------

[`register_optimizer_cls(...)`](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls)
: Register customize optimizer cls.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.