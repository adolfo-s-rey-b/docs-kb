[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fclip_by_norm&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.clip\_by\_norm Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/clip_ops.py#L152-L242)

Clips tensor values to a maximum L2-norm.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.clip_by_norm`](https://www.tensorflow.org/api_docs/python/tf/clip_by_norm)

tf.clip_by_norm(
        t, clip_norm, axes=None, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff) |

Given a tensor `t`, and a maximum clip value `clip_norm`, this operation normalizes `t` so that its L2-norm is less than or equal to `clip_norm`, along the dimensions given in `axes`. Specifically, in the default case where all dimensions are used for calculation, if the L2-norm of `t` is already less than or equal to `clip_norm`, then `t` is not modified. If the L2-norm is greater than `clip_norm`, then this operation returns a tensor of the same type and shape as `t` with its values set to:

`t * clip_norm / l2norm(t)`

In this case, the L2-norm of the output tensor is `clip_norm`.

As another example, if `t` is a matrix and `axes == [1]`, then each row of the output will have L2-norm less than or equal to `clip_norm`. If `axes == [0]` instead, each column of the output will be clipped.

#### Code example:

    some_nums = tf.constant([[1, 2, 3, 4, 5]], dtype=tf.float32)

This operation is typically used to clip gradients before applying them with an optimizer. Most gradient data is a collection of different shaped tensors for different parts of the model. Thus, this is a common usage:

# Get your gradients after training
    loss_value, grads = grad(model, features, labels)
    
    # Apply some clipping
    grads = [tf.clip_by_norm(g, norm)\
                 for g in grads]
    
    # Continue on with training
    optimizer.apply_gradients(grads)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t` | A `Tensor` or `IndexedSlices`. This must be a floating point type. |
| `clip_norm` | A 0-D (scalar) `Tensor` > 0. A maximum clipping value, also floating point. Note: If a negative clip\_norm is provided, it will be treated as zero. |
| `axes` | A 1-D (vector) `Tensor` of type int32 containing the dimensions to use for computing the L2-norm. If `None` (the default), uses all dimensions. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A clipped `Tensor` or `IndexedSlices`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the clip\_norm tensor is not a 0-D scalar tensor. |
| `TypeError` | If dtype of the input is not a floating point or complex type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.