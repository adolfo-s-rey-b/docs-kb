[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.clip\_by\_average\_norm Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/clip_by_average_norm#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/clip_ops.py#L395-L440)

Clips tensor values to a maximum average L2-norm. (deprecated)

tf.compat.v1.clip_by_average_norm(
        t, clip_norm, name=None
    )

Given a tensor `t`, and a maximum clip value `clip_norm`, this operation normalizes `t` so that its average L2-norm is less than or equal to `clip_norm`. Specifically, if the average L2-norm is already less than or equal to `clip_norm`, then `t` is not modified. If the average L2-norm is greater than `clip_norm`, then this operation returns a tensor of the same type and shape as `t` with its values set to:

`t * clip_norm / l2norm_avg(t)`

In this case, the average L2-norm of the output tensor is `clip_norm`.

This operation is typically used to clip gradients before applying them with an optimizer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t` | A `Tensor`. |
| `clip_norm` | A 0-D (scalar) `Tensor` > 0. A maximum clipping value. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A clipped `Tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.