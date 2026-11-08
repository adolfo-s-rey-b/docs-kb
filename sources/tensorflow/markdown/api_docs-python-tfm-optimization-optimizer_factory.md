[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2Foptimizer_factory&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.optimization.optimizer\_factory Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/optimization/optimizer_factory#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/optimizer_factory.py)

Optimizer factory class.

Classes
-------

[`class OptimizerFactory`](https://www.tensorflow.org/api_docs/python/tfm/optimization/OptimizerFactory)
: Optimizer factory class.

Functions
---------

[`register_optimizer_cls(...)`](https://www.tensorflow.org/api_docs/python/tfm/optimization/register_optimizer_cls)
: Register customize optimizer cls.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| LEGACY\_OPTIMIZERS\_CLS | {<br>     'adafactor': 'Unimplemented',<br>     'adafactor_keras': <class 'tf_keras.src.optimizers.adafactor.Adafactor'>,<br>     'adagrad': <class 'tf_keras.src.optimizers.legacy.adagrad.Adagrad'>,<br>     'adam': <class 'tf_keras.src.optimizers.legacy.adam.Adam'>,<br>     'adam_experimental': <class 'tf_keras.src.optimizers.adam.Adam'>,<br>     'adamw': <class 'official.modeling.optimization.legacy_adamw.AdamWeightDecay'>,<br>     'adamw_experimental': <class 'tf_keras.src.optimizers.adamw.AdamW'>,<br>     'lamb': <class 'official.modeling.optimization.lamb.LAMB'>,<br>     'lars': <class 'official.modeling.optimization.lars.LARS'>,<br>     'rmsprop': <class 'tf_keras.src.optimizers.legacy.rmsprop.RMSprop'>,<br>     'sgd': <class 'tf_keras.src.optimizers.legacy.gradient_descent.SGD'>,<br>     'sgd_experimental': <class 'tf_keras.src.optimizers.sgd.SGD'>,<br>     'slide': 'Unimplemented'<br>    } |
| LR\_CLS | {<br>     'cosine': <class 'official.modeling.optimization.lr_schedule.CosineDecayWithOffset'>,<br>     'exponential': <class 'official.modeling.optimization.lr_schedule.ExponentialDecayWithOffset'>,<br>     'polynomial': <class 'official.modeling.optimization.lr_schedule.PolynomialDecayWithOffset'>,<br>     'power': <class 'official.modeling.optimization.lr_schedule.DirectPowerDecay'>,<br>     'power_linear': <class 'official.modeling.optimization.lr_schedule.PowerAndLinearDecay'>,<br>     'power_with_offset': <class 'official.modeling.optimization.lr_schedule.PowerDecayWithOffset'>,<br>     'step_cosine_with_offset': <class 'official.modeling.optimization.lr_schedule.StepCosineDecayWithOffset'>,<br>     'stepwise': <class 'official.modeling.optimization.lr_schedule.PiecewiseConstantDecayWithOffset'><br>    } |
| NEW\_OPTIMIZERS\_CLS | {<br>     'adafactor': 'Unimplemented',<br>     'adafactor_keras': <class 'tf_keras.src.optimizers.adafactor.Adafactor'>,<br>     'adagrad': <class 'tf_keras.src.optimizers.adagrad.Adagrad'>,<br>     'adam': <class 'tf_keras.src.optimizers.adam.Adam'>,<br>     'adam_experimental': <class 'tf_keras.src.optimizers.adam.Adam'>,<br>     'adamw': <class 'official.modeling.optimization.legacy_adamw.AdamWeightDecay'>,<br>     'adamw_experimental': <class 'tf_keras.src.optimizers.adamw.AdamW'>,<br>     'lamb': <class 'official.modeling.optimization.lamb.LAMB'>,<br>     'lars': <class 'official.modeling.optimization.lars.LARS'>,<br>     'rmsprop': <class 'tf_keras.src.optimizers.rmsprop.RMSprop'>,<br>     'sgd': <class 'tf_keras.src.optimizers.sgd.SGD'>,<br>     'sgd_experimental': <class 'tf_keras.src.optimizers.sgd.SGD'>,<br>     'slide': 'Unimplemented'<br>    } |
| SHARED\_OPTIMIZERS | {<br>     'adafactor': 'Unimplemented',<br>     'adafactor_keras': <class 'tf_keras.src.optimizers.adafactor.Adafactor'>,<br>     'adam_experimental': <class 'tf_keras.src.optimizers.adam.Adam'>,<br>     'adamw': <class 'official.modeling.optimization.legacy_adamw.AdamWeightDecay'>,<br>     'adamw_experimental': <class 'tf_keras.src.optimizers.adamw.AdamW'>,<br>     'lamb': <class 'official.modeling.optimization.lamb.LAMB'>,<br>     'lars': <class 'official.modeling.optimization.lars.LARS'>,<br>     'sgd_experimental': <class 'tf_keras.src.optimizers.sgd.SGD'>,<br>     'slide': 'Unimplemented'<br>    } |
| WARMUP\_CLS | {<br>     'linear': <class 'official.modeling.optimization.lr_schedule.LinearWarmup'>,<br>     'polynomial': <class 'official.modeling.optimization.lr_schedule.PolynomialWarmUp'><br>    } |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.