[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.mixed\_precision.FixedLossScale Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#get_config)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#update)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L201-L257)

Loss scale with a fixed value.

Inherits From: [`LossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/LossScale)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.mixed_precision.experimental.FixedLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale)
, [`tf.compat.v1.train.experimental.FixedLossScale`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/mixed_precision/FixedLossScale)

tf.compat.v1.mixed_precision.FixedLossScale(
        loss_scale_value
    )

The loss scale is not updated for the lifetime of instances of this class. A given instance of this class always returns the same number when called.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `loss_scale_value` | A Python float. Its ideal value varies depending on models to run. Choosing a too small loss\_scale might affect model quality; a too big loss\_scale might cause inf or nan. There is no single right loss\_scale to apply. There is no harm choosing a relatively big number as long as no nan or inf is encountered in training. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If loss\_scale\_value is less than 1. |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L195-L198)

@classmethod

Creates the LossScale from its config.

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L256-L257)

get_config()

Returns the config of this loss scale.

### `update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L249-L251)

update(
        grads
    )

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/experimental/loss_scale.py#L246-L247)

__call__()

Returns the current loss scale as a scalar `float32` tensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.