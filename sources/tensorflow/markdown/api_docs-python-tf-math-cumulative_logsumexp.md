[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.cumulative\_logsumexp Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4374-L4427)

Compute the cumulative log-sum-exp of the tensor `x` along the `axis`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.cumulative_logsumexp`](https://www.tensorflow.org/api_docs/python/tf/math/cumulative_logsumexp)

tf.math.cumulative_logsumexp(
        x, axis=0, exclusive=False, reverse=False, name=None
    )

By default, this operation performs an inclusive cumulative log-sum-exp, which means that the first element of the input is identical to the first element of the output.

This operation is significantly more numerically stable than the equivalent Tensorflow operation `tf.math.log(tf.math.cumsum(tf.math.exp(x)))`, although it computes the same result given infinite numerical precision. However, note that in some cases, it may be less stable than [`tf.math.reduce_logsumexp`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_logsumexp)
 for a given element, as it applies the "log-sum-exp trick" in a different way.

More precisely, where [`tf.math.reduce_logsumexp`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_logsumexp)
 uses the following trick:

log(sum(exp(x))) == log(sum(exp(x - max(x)))) + max(x)

it cannot be directly used here as there is no fast way of applying it to each prefix `x[:i]`. Instead, this function implements a prefix scan using pairwise log-add-exp, which is a commutative and associative (up to floating point precision) operator:

log_add_exp(x, y) = log(exp(x) + exp(y))
                      = log(1 + exp(min(x, y) - max(x, y))) + max(x, y)

However, reducing using the above operator leads to a different computation tree (logs are taken repeatedly instead of only at the end), and the maximum is only computed pairwise instead of over the entire prefix. In general, this leads to a different and slightly less precise computation.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. Must be one of the following types: `float16`, `float32`, `float64`. |
| `axis` | A `Tensor` of type `int32` or `int64` (default: 0). Must be in the range `[-rank(x), rank(x))`. |\
| `exclusive` | If `True`, perform exclusive cumulative log-sum-exp. |\
| `reverse` | If `True`, performs the cumulative log-sum-exp in the reverse direction. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same shape and type as `x`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.