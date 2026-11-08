[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.DirectPowerDecay Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L236-L270)

Learning rate schedule follows lr \* (step)^power.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.DirectPowerDecay`](https://www.tensorflow.org/api_docs/python/tfm/optimization/DirectPowerDecay)

tfm.optimization.DirectPowerDecay(
        initial_learning_rate: float,
        power: float = 1.0,
        name: str = 'DirectPowerDecay'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_learning_rate` | The initial learning rate. |
| `power` | The order of the polynomial. |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L264-L270)

get_config()

Get the configuration of the learning rate schedule.

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L255-L262)

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