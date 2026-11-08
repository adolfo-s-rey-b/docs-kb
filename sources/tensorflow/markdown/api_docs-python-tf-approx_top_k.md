[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/approx_top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/approx_top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/approx_top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/approx_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/approx_top_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.approx\_top\_k Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/approx_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/approx_top_k#returns)
    

Returns min/max k values and their indices of the input operand in an approximate manner.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.approx_top_k`](https://www.tensorflow.org/api_docs/python/tf/approx_top_k)

tf.approx_top_k(
        input: Annotated[Any, TV_ApproxTopK_T],
        k: int,
        reduction_dimension: int = -1,
        recall_target: float = 0.95,
        is_max_k: bool = True,
        reduction_input_size_override: int = -1,
        aggregate_to_topk: bool = True,
        name=None
    )

See [https://arxiv.org/abs/2206.14286](https://arxiv.org/abs/2206.14286)
 for the algorithm details. This op is only optimized on TPU currently.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`. Array to search. Must be at least 1-D of the floating type |
| `k` | An `int` that is `>= 0`. Specifies the number of min/max-k. |
| `reduction_dimension` | An optional `int`. Defaults to `-1`. Integer dimension along which to search. Default: -1. |
| `recall_target` | An optional `float`. Defaults to `0.95`. Recall target for the approximation. Range in (0,1\] |
| `is_max_k` | An optional `bool`. Defaults to `True`. When true, computes max-k; otherwise computes min-k. |
| `reduction_input_size_override` | An optional `int`. Defaults to `-1`. When set to a positive value, it overrides the size determined by `input[reduction_dim]` for evaluating the recall. This option is useful when the given `input` is only a subset of the overall computation in SPMD or distributed pipelines, where the true input size cannot be deferred by the `input` shape. |
| `aggregate_to_topk` | An optional `bool`. Defaults to `True`. When true, aggregates approximate results to top-k. When false, returns the approximate results. The number of the approximate results is implementation defined and is greater equals to the specified `k`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (values, indices). |     |
| `values` | A `Tensor`. Has the same type as `input`. |
| `indices` | A `Tensor` of type `int32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.