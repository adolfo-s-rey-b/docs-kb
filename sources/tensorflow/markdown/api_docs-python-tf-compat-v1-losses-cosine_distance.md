[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.cosine\_distance Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L270-L324)

Adds a cosine-distance loss to the training procedure. (deprecated arguments)

tf.compat.v1.losses.cosine_distance(
        labels,
        predictions,
        axis=None,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS,
        dim=None
    )

Note that the function assumes that `predictions` and `labels` are already unit-normalized.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `Tensor` whose shape matches 'predictions' |
| `predictions` | An arbitrary matrix. |
| `axis` | The dimension along which the cosine distance is computed. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `losses` dimension). |
| `scope` | The scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which this loss will be added. |
| `reduction` | Type of reduction to apply to loss. |
| `dim` | The old (deprecated) name for `axis`. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same shape as `labels`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `predictions` shape doesn't match `labels` shape, or `axis`, `labels`, `predictions` or `weights` is `None`. |

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