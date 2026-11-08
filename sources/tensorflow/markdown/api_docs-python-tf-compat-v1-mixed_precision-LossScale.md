[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.LossScale Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L35-L198)

Base class for all TF1 loss scales.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.mixed_precision.experimental.LossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)
, [`tf.compat.v1.train.experimental.LossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)

tf.compat.v1.mixed_precision.LossScale()

This is an abstract base class, so you cannot instantiate it directly. Instead, use one of its concrete subclasses:

*   [`tf.compat.v1.mixed_precision.DynamicLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/DynamicLossScale)
    
*   [`tf.compat.v1.mixed_precision.FixedLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale)
    

Loss scaling is a process that multiplies the loss by a multiplier called the loss scale, and divides each gradient by the same multiplier. The pseudocode for this process is:

loss = ...
    loss *= loss_scale
    grads = gradients(loss, vars)
    grads /= loss_scale

Mathematically, loss scaling has no effect, but can help avoid numerical underflow in intermediate gradients when float16 tensors are used for mixed precision training. By multiplying the loss, each intermediate gradient will have the same multiplier applied.

Instances of this class represent a loss scale. Calling instances of this class returns the loss scale as a scalar float32 tensor, while method `update()` updates the loss scale depending on the values of the gradients. Optimizers use instances of this class to scale loss and gradients.

In most functions that accept a LossScale, you can also pass an int (such as

8) to create a `FixedLossScale` or the string `"dynamic"` to create a dynamic loss scale.

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L195-L198)

@classmethod

Creates the LossScale from its config.

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L190-L193)

@abc.abstractmethod

Returns the config of this loss scale.

### `update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L86-L121)

@abc.abstractmethod

Updates the value of the loss scale.

The loss scale will be potentially updated, based on the value of `grads`. The tensor returned by calling this class is only updated when this function is evaluated.

In eager mode, this directly updates the loss scale, so that calling `__call__` will return the newly updated loss scale. In graph mode, this returns an op that, when evaluated, updates the loss scale.

This function also returns a `should_apply_gradients` bool. If False, gradients should not be applied to the variables that step, as nonfinite gradients were found, and the loss scale has been be updated to reduce the chance of finding nonfinite gradients in the next step. Some loss scale classes will always return True, as they cannot adjust themselves in response to nonfinite gradients.

When a DistributionStrategy is used, this function may only be called in a cross-replica context.

|     |     |
| --- | --- |
| Args |     |
| `grads` | A nested structure of unscaled gradients, each which is the gradient of the loss with respect to a weight. The gradients should have already been divided by the loss scale being before passed to this function. 'None' gradients are accepted, and are ignored. |

|     |     |
| --- | --- |
| Returns |     |
| `update_op` | In eager mode, None. In graph mode, an op to update the loss scale. |
| `should_apply_gradients` | Either a bool or a scalar boolean tensor. If False, the caller should skip applying `grads` to the variables this step. |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L81-L84)

@abc.abstractmethod

Returns the current loss scale as a scalar `float32` tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.