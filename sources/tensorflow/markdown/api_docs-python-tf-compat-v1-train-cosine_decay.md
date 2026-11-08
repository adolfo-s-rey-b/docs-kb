[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#references)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.cosine\_decay Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#references)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/cosine_decay#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L457-L517)

Applies cosine decay to the learning rate.

tf.compat.v1.train.cosine_decay(
        learning_rate, global_step, decay_steps, alpha=0.0, name=None
    )

When training a model, it is often recommended to lower the learning rate as the training progresses. This function applies a cosine decay function to a provided initial learning rate. It requires a `global_step` value to compute the decayed learning rate. You can just pass a TensorFlow variable that you increment at each training step.

The function returns the decayed learning rate. It is computed as:

global_step = min(global_step, decay_steps)
    cosine_decay = 0.5 * (1 + cos(pi * global_step / decay_steps))
    decayed = (1 - alpha) * cosine_decay + alpha
    decayed_learning_rate = learning_rate * decayed

#### Example usage:

decay_steps = 1000
    lr_decayed = cosine_decay(learning_rate, global_step, decay_steps)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate` | A scalar `float32` or `float64` Tensor or a Python number. The initial learning rate. |
| `global_step` | A scalar `int32` or `int64` `Tensor` or a Python number. Global step to use for the decay computation. |
| `decay_steps` | A scalar `int32` or `int64` `Tensor` or a Python number. Number of steps to decay over. |
| `alpha` | A scalar `float32` or `float64` Tensor or a Python number. Minimum learning rate value as a fraction of learning\_rate. |
| `name` | String. Optional name of the operation. Defaults to 'CosineDecay'. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` of the same type as `learning_rate`. The decayed learning rate. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `global_step` is not supplied. |

|     |
| --- |
| References<br>---------- |     |
| Stochastic Gradient Descent with Warm Restarts: [Loshchilov et al., 2017](https://openreview.net/forum?id=Skq89Scxx&noteId=Skq89Scxx)<br> ([pdf](https://openreview.net/pdf?id=Skq89Scxx)<br>) |     |

eager compatibility
-------------------

When eager execution is enabled, this function returns a function which in turn returns the decayed learning rate Tensor. This can be useful for changing the learning rate value across different invocations of optimizer functions.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.