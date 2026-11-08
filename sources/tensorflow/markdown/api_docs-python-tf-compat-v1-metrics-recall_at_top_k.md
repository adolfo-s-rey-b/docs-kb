[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.recall\_at\_top\_k Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L2756-L2837)

Computes recall@k of top-k predictions with respect to sparse labels.

tf.compat.v1.metrics.recall_at_top_k(
        labels,
        predictions_idx,
        k=None,
        class_id=None,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

Differs from `recall_at_k` in that predictions must be in the form of top `k` class indices, whereas `recall_at_k` expects logits. Refer to `recall_at_k` for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `int64` `Tensor` or `SparseTensor` with shape \[D1, ... DN, num\_labels\] or \[D1, ... DN\], where the latter implies num\_labels=1. N >= 1 and num\_labels is the number of target classes for the associated prediction. Commonly, N=1 and `labels` has shape \[batch\_size, num\_labels\]. \[D1, ... DN\] must match `predictions`. Values should be in range \[0, num\_classes), where num\_classes is the last dimension of `predictions`. Values outside this range always count towards `false_negative_at_<k>`. |\
| `predictions_idx` | Integer `Tensor` with shape \[D1, ... DN, k\] where N >= 1. Commonly, N=1 and predictions has shape \[batch size, k\]. The final dimension contains the top `k` predicted class indices. \[D1, ... DN\] must match `labels`. |\
| `k` | Integer, k for @k metric. Only used for the default op name. |\
| `class_id` | Integer class ID for which we want binary metrics. This should be in range \[0, num\_classes), where num\_classes is the last dimension of `predictions`. If class\_id is outside this range, the method returns NAN. |\
| `weights` | `Tensor` whose rank is either 0, or n-1, where n is the rank of `labels`. If the latter, it must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |\
| `metrics_collections` | An optional list of collections that values should be added to. |\
| `updates_collections` | An optional list of collections that updates should be added to. |\
| `name` | Name of new update operation, and namespace for other dependent ops. |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| `recall` | Scalar `float64` `Tensor` with the value of `true_positives` divided by the sum of `true_positives` and `false_negatives`. |\
| `update_op` | `Operation` that increments `true_positives` and `false_negatives` variables appropriately, and whose value matches `recall`. |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `weights` is not `None` and its shape doesn't match `predictions`, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.