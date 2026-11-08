[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flosses%2Fmean_pairwise_squared_error&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.mean\_pairwise\_squared\_error Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L513-L618)

Adds a pairwise-errors-squared loss to the training procedure.

tf.compat.v1.losses.mean_pairwise_squared_error(
        labels,
        predictions,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES
    )

Unlike `mean_squared_error`, which is a measure of the differences between corresponding elements of `predictions` and `labels`, `mean_pairwise_squared_error` is a measure of the differences between pairs of corresponding elements of `predictions` and `labels`.

For example, if `labels`\=\[a, b, c\] and `predictions`\=\[x, y, z\], there are three pairs of differences are summed to compute the loss: loss = \[ ((a-b) - (x-y)).^2 + ((a-c) - (x-z)).^2 + ((b-c) - (y-z)).^2 \] / 3

Note that since the inputs are of shape `[batch_size, d0, ... dN]`, the corresponding pairs are computed within each batch sample but not across samples within a batch. For example, if `predictions` represents a batch of 16 grayscale images of dimension \[batch\_size, 100, 200\], then the set of pairs is drawn from each image, but not across images.

`weights` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `weights` is a tensor of size `[batch_size]`, then the total loss for each sample of the batch is rescaled by the corresponding element in the `weights` vector.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth output tensor, whose shape must match the shape of `predictions`. |
| `predictions` | The predicted outputs, a tensor of size `[batch_size, d0, .. dN]` where N+1 is the total number of dimensions in `predictions`. |
| `weights` | Coefficients for the loss a scalar, a tensor of shape `[batch_size]` or a tensor whose shape matches `predictions`. |
| `scope` | The scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which the loss will be added. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar `Tensor` that returns the weighted loss. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shape of `predictions` doesn't match that of `labels` or if the shape of `weights` is invalid. Also if `labels` or `predictions` is None. |

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