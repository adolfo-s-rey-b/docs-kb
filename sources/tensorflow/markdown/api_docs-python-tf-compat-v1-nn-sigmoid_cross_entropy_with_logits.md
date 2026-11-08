[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fnn%2Fsigmoid_cross_entropy_with_logits&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.sigmoid\_cross\_entropy\_with\_logits Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/sigmoid_cross_entropy_with_logits#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl.py#L110-L146)

Computes sigmoid cross entropy given `logits`.

tf.compat.v1.nn.sigmoid_cross_entropy_with_logits(
        labels=None, logits=None, name=None
    )

Measures the probability error in tasks with two outcomes in which each outcome is independent and need not have a fully certain label. For instance, one could perform a regression where the probability of an event happening is known and used as a label. This loss may also be used for binary classification, where labels are either zero or one.

For brevity, let `x = logits`, `z = labels`. The logistic loss is

  z * -log(sigmoid(x)) + (1 - z) * -log(1 - sigmoid(x))
    = z * -log(1 / (1 + exp(-x))) + (1 - z) * -log(exp(-x) / (1 + exp(-x)))
    = z * log(1 + exp(-x)) + (1 - z) * (-log(exp(-x)) + log(1 + exp(-x)))
    = z * log(1 + exp(-x)) + (1 - z) * (x + log(1 + exp(-x))
    = (1 - z) * x + log(1 + exp(-x))
    = x - x * z + log(1 + exp(-x))

For x < 0, to avoid overflow in exp(-x), we reformulate the above

  x - x * z + log(1 + exp(-x))
    = log(exp(x)) - x * z + log(1 + exp(-x))
    = - x * z + log(1 + exp(x))

Hence, to ensure stability and avoid overflow, the implementation uses this equivalent formulation

max(x, 0) - x * z + log(1 + exp(-abs(x)))

`logits` and `labels` must have the same type and shape.

    logits = tf.constant([1., -1., 0., 1., -1., 0., 0.])

Compared to the losses which handle multiple outcomes, [`tf.nn.softmax_cross_entropy_with_logits`](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits)
 for general multi-class classification and [`tf.nn.sparse_softmax_cross_entropy_with_logits`](https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits)
 for more efficient multi-class classification with hard labels, `sigmoid_cross_entropy_with_logits` is a slight simplification for binary classification:

  sigmoid(x) = softmax([x, 0])[0]

11+e−x\=exex+e0

While `sigmoid_cross_entropy_with_logits` works for soft binary labels (probabilities between 0 and 1), it can also be used for binary classification where the labels are hard. There is an equivalence between all three symbols in this case, with a probability 0 indicating the second class or 1 indicating the first class:

    sigmoid_logits = tf.constant([1., -1., 0.])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | A `Tensor` of the same type and shape as `logits`. Between 0 and 1, inclusive. |
| `logits` | A `Tensor` of type `float32` or `float64`. Any real number. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of the same shape as `logits` with the componentwise logistic losses. |     |

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