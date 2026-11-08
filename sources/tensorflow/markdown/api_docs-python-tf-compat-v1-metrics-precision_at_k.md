[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fmetrics%2Fprecision_at_k&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.precision\_at\_k Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L3720-L3811)

Computes precision@k of the predictions with respect to sparse labels.

tf.compat.v1.metrics.precision_at_k(
        labels,
        predictions,
        k,
        class_id=None,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

If `class_id` is specified, we calculate precision by considering only the entries in the batch for which `class_id` is in the top-k highest `predictions`, and computing the fraction of them for which `class_id` is indeed a correct label. If `class_id` is not specified, we'll calculate precision as how often on average a class among the top-k classes with the highest predicted values of a batch entry is correct and can be found in the label for that entry.

`precision_at_k` creates two local variables, `true_positive_at_<k>` and `false_positive_at_<k>`, that are used to compute the precision@k frequency. This frequency is ultimately returned as `precision_at_<k>`: an idempotent operation that simply divides `true_positive_at_<k>` by total (`true_positive_at_<k>` + `false_positive_at_<k>`).

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `precision_at_<k>`. Internally, a `top_k` operation computes a `Tensor` indicating the top `k` `predictions`. Set operations applied to `top_k` and `labels` calculate the true positives and false positives weighted by `weights`. Then `update_op` increments `true_positive_at_<k>` and `false_positive_at_<k>` using these values.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `int64` `Tensor` or `SparseTensor` with shape \[D1, ... DN, num\_labels\] or \[D1, ... DN\], where the latter implies num\_labels=1. N >= 1 and num\_labels is the number of target classes for the associated prediction. Commonly, N=1 and `labels` has shape \[batch\_size, num\_labels\]. \[D1, ... DN\] must match `predictions`. Values should be in range \[0, num\_classes), where num\_classes is the last dimension of `predictions`. Values outside this range are ignored. |\
| `predictions` | Float `Tensor` with shape \[D1, ... DN, num\_classes\] where N >= 1. Commonly, N=1 and predictions has shape \[batch size, num\_classes\]. The final dimension contains the logit values for each class. \[D1, ... DN\] must match `labels`. |\
| `k` | Integer, k for @k metric. |\
| `class_id` | Integer class ID for which we want binary metrics. This should be in range \[0, num\_classes\], where num\_classes is the last dimension of `predictions`. If `class_id` is outside this range, the method returns NAN. |\
| `weights` | `Tensor` whose rank is either 0, or n-1, where n is the rank of `labels`. If the latter, it must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |\
| `metrics_collections` | An optional list of collections that values should be added to. |\
| `updates_collections` | An optional list of collections that updates should be added to. |\
| `name` | Name of new update operation, and namespace for other dependent ops. |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| `precision` | Scalar `float64` `Tensor` with the value of `true_positives` divided by the sum of `true_positives` and `false_positives`. |\
| `update_op` | `Operation` that increments `true_positives` and `false_positives` variables appropriately, and whose value matches `precision`. |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `weights` is not `None` and its shape doesn't match `predictions`, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |\
| `RuntimeError` | If eager execution is enabled. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.