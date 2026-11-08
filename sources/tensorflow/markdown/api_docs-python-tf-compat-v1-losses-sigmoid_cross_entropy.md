[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flosses%2Fsigmoid_cross_entropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.sigmoid\_cross\_entropy Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L771-L834)

Creates a cross-entropy loss using tf.nn.sigmoid\_cross\_entropy\_with\_logits.

tf.compat.v1.losses.sigmoid_cross_entropy(
        multi_class_labels,
        logits,
        weights=1.0,
        label_smoothing=0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

`weights` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `weights` is a tensor of shape `[batch_size]`, then the loss weights apply to each corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/2:

new_multiclass_labels = multiclass_labels * (1 - label_smoothing)
    
                            + 0.5 * label_smoothing

|     |     |
| --- | --- |
| Args<br>---- |     |
| `multi_class_labels` | `[batch_size, num_classes]` target integer labels in `{0, 1}`. |
| `logits` | Float `[batch_size, num_classes]` logits outputs of the network. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `multi_class_labels`, and must be broadcastable to `multi_class_labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `losses` dimension). |
| `label_smoothing` | If greater than `0` then smooth the labels. |
| `scope` | The scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which the loss will be added. |
| `reduction` | Type of reduction to apply to loss. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss `Tensor` of the same type as `logits`. If `reduction` is `NONE`, this has the same shape as `logits`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shape of `logits` doesn't match that of `multi_class_labels` or if the shape of `weights` is invalid, or if `weights` is None. Also if `multi_class_labels` or `logits` is None. |

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