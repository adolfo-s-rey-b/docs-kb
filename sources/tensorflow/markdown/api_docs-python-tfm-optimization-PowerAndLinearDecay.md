[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2FPowerAndLinearDecay&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.PowerAndLinearDecay Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L273-L337)

Learning rate schedule with multiplied by linear decay at the end.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.PowerAndLinearDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/PowerAndLinearDecay)

tfm.optimization.PowerAndLinearDecay(
        initial_learning_rate: float,
        total_decay_steps: int,
        power: float = 1.0,
        linear_decay_fraction: float = 0.1,
        offset: int = 0,
        name: str = 'PowerAndLinearDecay'
    )

The schedule has the following behavoir. Let offset\_step = step - offset.

1) offset\_step < 0, the actual learning rate equals initial\_learning\_rate. 2) offset\_step <= total\_decay\_steps \* (1 - linear\_decay\_fraction), the actual learning rate equals lr \* offset\_step^power. 3) total\_decay\_steps \* (1 - linear\_decay\_fraction) <= offset\_step < total\_decay\_steps, the actual learning rate equals lr \* offset\_step^power \* (total\_decay\_steps - offset\_step) / (total\_decay\_steps \* linear\_decay\_fraction). 4) offset\_step >= total\_decay\_steps, the actual learning rate equals zero.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | The initial learning rate. |
| `total_decay_steps` | The total number of steps for power + linear decay. |
| `power` | The order of the polynomial. |
| `linear_decay_fraction` | In the last `linear_decay_fraction` steps, the learning rate will be multiplied by a linear decay. |
| `offset` | The offset applied to steps. |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L328-L337)

get_config()

Get the configuration of the learning rate schedule.

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L314-L326)

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