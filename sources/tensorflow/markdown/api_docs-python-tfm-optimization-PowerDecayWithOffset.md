[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2FPowerDecayWithOffset&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PowerDecayWithOffset Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L340-L389)

Power learning rate decay with offset.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.PowerDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerDecayWithOffset)

tfm.optimization.PowerDecayWithOffset(
        initial_learning_rate: float,
        power: float = 1.0,
        offset: int = 0,
        pre_offset_learning_rate: float = 1000000.0,
        name: str = 'PowerDecayWithOffset'
    )

Learning rate equals to `pre_offset_learning_rate` if `step` < `offset`. Otherwise, learning rate equals to lr \* (step - offset)^power.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | The initial learning rate. |
| `power` | The order of the polynomial. |
| `offset` | The offset when computing the power decay. |
| `pre_offset_learning_rate` | The maximum learning rate we'll use. |
| `name` | Optional, name of learning rate schedule. |

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L381-L389)

get_config()

Get the configuration of the learning rate schedule.

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L369-L379)

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