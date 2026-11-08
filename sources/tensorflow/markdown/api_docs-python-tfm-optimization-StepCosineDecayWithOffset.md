[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Foptimization%2FStepCosineDecayWithOffset&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.optimization.StepCosineDecayWithOffset Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L392-L490)

Stepwise cosine learning rate decay with offset.

#### View aliases

**Main aliases**

[`tfm.optimization.lr_schedule.StepCosineDecayWithOffset`](https://www.tensorflow.org/api_docs/python/tfm/optimization/StepCosineDecayWithOffset)

tfm.optimization.StepCosineDecayWithOffset(
        boundaries,
        values,
        offset: int = 0,
        name: str = 'StepCosineDecayWithOffset'
    )

Learning rate is equivalent to one or more cosine decay(s) starting and ending at each interval.

ExampleL

  boundaries: [100000, 110000]
      values: [1.0, 0.5]
      lr_decayed_fn = (
      lr_schedule.StepCosineDecayWithOffset(
          boundaries,
          values))

from 0 to 100000 step, it will cosine decay from 1.0 to 0.5 from 100000 to 110000 step, it cosine decay from 0.5 to 0.0

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boundaries` | A list of `Tensor`s or `int`s with strictly increasing entries, and with all elements having the same type as the optimizer step. |
| `values` | A list of `Tensor`s or `float`s that specifies the values for the intervals defined by `boundaries`. It should have one more element than `boundaries`, and all elements should have the same type. |
| `offset` | The offset when computing the power decay. |
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L484-L490)

get_config()

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/optimization/lr_schedule.py#L449-L482)

__call__(
        global_step
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.