[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Fweighted_cross_entropy_with_logits&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.weighted\_cross\_entropy\_with\_logits Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/weighted_cross_entropy_with_logits#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L342-L404)

Computes a weighted cross entropy. (deprecated arguments)

tf.compat.v1.nn.weighted_cross_entropy_with_logits(
        labels=None, logits=None, pos_weight=None, name=None, targets=None
    )

This is like `sigmoid_cross_entropy_with_logits()` except that `pos_weight`, allows one to trade off recall and precision by up- or down-weighting the cost of a positive error relative to a negative error.

The usual cross-entropy cost is defined as:

labels * -log(sigmoid(logits)) +
        (1 - labels) * -log(1 - sigmoid(logits))

A value `pos_weight > 1` decreases the false negative count, hence increasing the recall. Conversely setting `pos_weight < 1` decreases the false positive count and increases the precision. This can be seen from the fact that `pos_weight` is introduced as a multiplicative coefficient for the positive labels term in the loss expression:

labels * -log(sigmoid(logits)) * pos_weight +
        (1 - labels) * -log(1 - sigmoid(logits))

For brevity, let `x = logits`, `z = labels`, `q = pos_weight`. The loss is:

  qz * -log(sigmoid(x)) + (1 - z) * -log(1 - sigmoid(x))
    = qz * -log(1 / (1 + exp(-x))) + (1 - z) * -log(exp(-x) / (1 + exp(-x)))
    = qz * log(1 + exp(-x)) + (1 - z) * (-log(exp(-x)) + log(1 + exp(-x)))
    = qz * log(1 + exp(-x)) + (1 - z) * (x + log(1 + exp(-x))
    = (1 - z) * x + (qz +  1 - z) * log(1 + exp(-x))
    = (1 - z) * x + (1 + (q - 1) * z) * log(1 + exp(-x))

Setting `l = (1 + (q - 1) * z)`, to ensure stability and avoid overflow, the implementation uses

(1 - z) * x + l * (log(1 + exp(-abs(x))) + max(-x, 0))

`logits` and `labels` must have the same type and shape.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | A `Tensor` of the same type and shape as `logits`. |
| `logits` | A `Tensor` of type `float32` or `float64`. |
| `pos_weight` | A coefficient to use on the positive examples. |
| `name` | A name for the operation (optional). |
| `targets` | Deprecated alias for labels. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of the same shape as `logits` with the componentwise weighted logistic losses. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `logits` and `labels` do not have the same shape. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.