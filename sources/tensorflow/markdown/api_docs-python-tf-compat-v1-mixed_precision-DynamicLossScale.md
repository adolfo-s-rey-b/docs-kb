[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.DynamicLossScale Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L297-L438)

Loss scale that dynamically adjusts itself.

Inherits From: [`LossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.mixed_precision.experimental.DynamicLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale)
, [`tf.compat.v1.train.experimental.DynamicLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale)

tf.compat.v1.mixed_precision.DynamicLossScale(
        initial_loss_scale=(2 ** 15), increment_period=2000, multiplier=2.0
    )

Dynamic loss scaling works by adjusting the loss scale as training progresses. The goal is to keep the loss scale as high as possible without overflowing the gradients. As long as the gradients do not overflow, raising the loss scale never hurts.

The algorithm starts by setting the loss scale to an initial value. Every N steps that the gradients are finite, the loss scale is increased by some factor. However, if a NaN or Inf gradient is found, the gradients for that step are not applied, and the loss scale is decreased by the factor. This process tends to keep the loss scale as high as possible without gradients overflowing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_loss_scale` | A Python float. The loss scale to use at the beginning. It's better to start this at a very high number, because a loss scale that is too high gets lowered far more quickly than a loss scale that is too low gets raised. The default is 2 \*\* 15, which is approximately half the maximum float16 value. |
| `increment_period` | Increases loss scale every `increment_period` consecutive steps that finite gradients are encountered. If a nonfinite gradient is encountered, the count is reset back to zero. |
| `multiplier` | The multiplier to use when increasing or decreasing the loss scale. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `increment_period` |     |
| `initial_loss_scale` |     |
| `multiplier` |     |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L195-L198)

@classmethod

Creates the LossScale from its config.

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L433-L438)

get_config()

Returns the config of this loss scale.

### `update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L373-L420)

update(
        grads
    )

Updates loss scale based on if gradients are finite in current step.

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L370-L371)

__call__()

Returns the current loss scale as a scalar `float32` tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.