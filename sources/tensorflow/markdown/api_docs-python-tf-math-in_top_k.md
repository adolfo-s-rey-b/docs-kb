[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fin_top_k&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.in\_top\_k Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L6572-L6605)

Outputs whether the targets are in the top `K` predictions.

#### View aliases

**Main aliases**

[`tf.nn.in_top_k`](https://www.tensorflow.org/api_docs/python/tf/math/in_top_k)

tf.math.in_top_k(
        targets, predictions, k, name=None
    )

This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the prediction for the target class is finite (not inf, -inf, or nan) and among the top `k` predictions among all predictions for example `i`. `predictions` does not have to be normalized.

Note that the behavior of `InTopK` differs from the `TopK` op in its handling of ties; if multiple classes have the same prediction value and straddle the top-`k` boundary, all of those classes are considered to be in the top `k`.

    target = tf.constant([0, 1, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `targets` | A `batch_size` vector of class ids. Must be `int32` or `int64`. |
| `predictions` | A `batch_size` x `classes` tensor of type `float32`. |
| `k` | An `int`. The parameter to specify search space. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same shape of `targets` with type of `bool`. Each element specifies if the target falls into top-k predictions. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.