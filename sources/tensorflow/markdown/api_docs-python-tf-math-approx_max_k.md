[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.approx\_max\_k Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5887-L5947)

Returns max `k` values and their indices of the input `operand` in an approximate manner.

#### View aliases

**Main aliases**

[`tf.nn.approx_max_k`](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.approx_max_k`](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k)
, [`tf.compat.v1.nn.approx_max_k`](https://www.tensorflow.org/api_docs/python/tf/math/approx_max_k)

tf.math.approx_max_k(
        operand,
        k,
        reduction_dimension=-1,
        recall_target=0.95,
        reduction_input_size_override=-1,
        aggregate_to_topk=True,
        name=None
    )

See [https://arxiv.org/abs/2206.14286](https://arxiv.org/abs/2206.14286)
 for the algorithm details. This op is only optimized on TPU currently.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `operand` | Array to search for max-k. Must be a floating number type. |
| `k` | Specifies the number of max-k. |
| `reduction_dimension` | Integer dimension along which to search. Default: -1. |
| `recall_target` | Recall target for the approximation. |
| `reduction_input_size_override` | When set to a positive value, it overrides the size determined by `operand[reduction_dim]` for evaluating the recall. This option is useful when the given `operand` is only a subset of the overall computation in SPMD or distributed pipelines, where the true input size cannot be deferred by the `operand` shape. |
| `aggregate_to_topk` | When true, aggregates approximate results to top-k. When false, returns the approximate results. The number of the approximate results is implementation defined and is greater equals to the specified `k`. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of two arrays. The arrays are the max `k` values and the corresponding indices along the `reduction_dimension` of the input `operand`. The arrays' dimensions are the same as the input `operand` except for the `reduction_dimension`: when `aggregate_to_topk` is true, the reduction dimension is `k`; otherwise, it is greater equals to `k` where the size is implementation-defined. |     |

We encourage users to wrap `approx_max_k` with jit. See the following example for maximal inner production search (MIPS):

    import tensorflow as tf

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.