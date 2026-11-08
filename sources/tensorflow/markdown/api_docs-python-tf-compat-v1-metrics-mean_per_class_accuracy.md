[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.mean\_per\_class\_accuracy Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L1177-L1279)

Calculates the mean of the per-class accuracies.

tf.compat.v1.metrics.mean_per_class_accuracy(
        labels,
        predictions,
        num_classes,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

Calculates the accuracy for each class, then takes the mean of that.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates the accuracy of each class and returns them.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |     |
| --- | --- | --- |
| Args<br>---- |     |
| `labels` | A `Tensor` of ground truth labels with shape \[batch size\] and of type `int32` or `int64`. The tensor will be flattened if its rank > 1. |
| `predictions` | A `Tensor` of prediction results for semantic labels, whose shape is \[batch size\] and type `int32` or `int64`. The tensor will be flattened if its rank > 1. |
| `num_classes` | The possible number of labels the prediction task can have. This value must be provided, since two variables with shape = \[num\_classes\] will be allocated. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `metrics_collections` | An optional list of collections that `mean_per_class_accuracy' should be added to. </td> </tr><tr> <td>`updates\_collections`<a id="updates_collections"></a> </td> <td> An optional list of collections`update\_op`should be added to. </td> </tr><tr> <td>`name\` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `mean_accuracy` | A `Tensor` representing the mean per class accuracy. |
| `update_op` | An operation that updates the accuracy tensor. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `predictions` and `labels` have mismatched shapes, or if `weights` is not `None` and its shape doesn't match `predictions`, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.