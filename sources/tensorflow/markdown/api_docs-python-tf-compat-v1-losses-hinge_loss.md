[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/hinge_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.hinge\_loss Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L327-L375)

Adds a hinge loss to the training procedure.

tf.compat.v1.losses.hinge_loss(
        labels,
        logits,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth output tensor. Its shape should match the shape of logits. The values of the tensor are expected to be 0.0 or 1.0. Internally the {0,1} labels are converted to {-1,1} when calculating the hinge loss. |
| `logits` | The logits, a float tensor. Note that logits are assumed to be unbounded and 0-centered. A value > 0 (resp. < 0) is considered a positive (resp. negative) binary prediction. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `losses` dimension). |
| `scope` | The scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which the loss will be added. |
| `reduction` | Type of reduction to apply to loss. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same shape as `labels`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shapes of `logits` and `labels` don't match or if `labels` or `logits` is None. |

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