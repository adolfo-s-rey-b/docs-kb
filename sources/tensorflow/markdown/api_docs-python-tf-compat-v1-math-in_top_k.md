Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.in\_top\_k Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L6537-L6569)

Says whether the targets are in the top `K` predictions.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.in_top_k`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/in_top_k)

tf.compat.v1.math.in_top_k(
        predictions, targets, k, name=None
    )

This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the prediction for the target class is finite (not inf, -inf, or nan) and among the top `k` predictions among all predictions for example `i`. Note that the behavior of `InTopK` differs from the `TopK` op in its handling of ties; if multiple classes have the same prediction value and straddle the top-`k` boundary, all of those classes are considered to be in the top `k`.

More formally, let

predictionsi be the predictions for all classes for example `i`, targetsi be the target class for example `i`, outi be the output for example `i`,

outi\=predictionsi,targetsi∈TopKIncludingTies(predictionsi)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `predictions` | A `Tensor` of type `float32`. A `batch_size` x `classes` tensor. |
| `targets` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A `batch_size` vector of class ids. |
| `k` | An `int`. Number of top elements to look at for computing precision. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. Computed Precision at `k` as a `bool Tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.