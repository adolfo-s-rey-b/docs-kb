[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flosses%2Fcompute_weighted_loss&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#raises)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#note)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.compute\_weighted\_loss Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#raises)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#note)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L137-L213)

Computes the weighted loss.

tf.compat.v1.losses.compute_weighted_loss(
        losses,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `losses` | `Tensor` of shape `[batch_size, d1, ... dN]`. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `losses`, and must be broadcastable to `losses` (i.e., all dimensions must be either `1`, or the same as the corresponding `losses` dimension). |
| `scope` | the scope for the operations performed in computing the loss. |
| `loss_collection` | the loss will be added to these collections. |
| `reduction` | Type of reduction to apply to loss. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss `Tensor` of the same type as `losses`. If `reduction` is `NONE`, this has the same shape as `losses`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `weights` is `None` or the shape is not compatible with `losses`, or if the number of dimensions (rank) of either `losses` or `weights` is missing. |

|     |
| --- |
| Note<br>---- |     |
| When calculating the gradient of a weighted loss contributions from both `losses` and `weights` are considered. If your `weights` depend on some model parameters but you do not want this to affect the loss gradient, you need to apply [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)<br> to `weights` before passing them to `compute_weighted_loss`. |     |

eager compatibility
-------------------

The `loss_collection` argument is ignored when executing eagerly. Consider holding on to the return value or collecting losses via a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.