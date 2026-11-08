[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2FPolynomialWarmUp&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PolynomialWarmUp Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L168-L233)

Applies polynomial warmup schedule on a given learning rate decay schedule.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.PolynomialWarmUp`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PolynomialWarmUp)

tfm.optimization.PolynomialWarmUp(
        after_warmup_lr_sched: Union[tf_keras.optimizers.schedules.LearningRateSchedule, float],
        warmup_steps: int,
        power: float = 1.0,
        name: str = 'PolynomialWarmup'
    )

Methods
-------

### `from_config`

@classmethod

Instantiates a `LearningRateSchedule` from its config.

|     |     |
| --- | --- |
| Args |     |
| `config` | Output of `get_config()`. |

|     |
| --- |
| Returns |     |
| A `LearningRateSchedule` instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L220-L233)

get_config() -> Mapping[str, Any]

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L190-L218)

__call__(
        step
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.