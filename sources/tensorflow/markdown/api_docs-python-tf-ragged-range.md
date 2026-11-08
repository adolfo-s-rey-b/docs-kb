[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/range#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/range)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/range?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/range#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/range#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/range#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.range Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/range#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/range#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/range#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_math_ops.py#L44-L115)

Returns a `RaggedTensor` containing the specified sequences of numbers.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.range`](https://www.tensorflow.org/api_docs/python/tf/ragged/range)

tf.ragged.range(
        starts,
        limits=None,
        deltas=1,
        dtype=None,
        name=None,
        row_splits_dtype=tf.dtypes.int64
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

Each row of the returned `RaggedTensor` contains a single sequence:

ragged.range(starts, limits, deltas)[i] ==
        tf.range(starts[i], limits[i], deltas[i])

If `start[i] < limits[i] and deltas[i] > 0`, then `output[i]` will be an empty list. Similarly, if `start[i] > limits[i] and deltas[i] < 0`, then `output[i]` will be an empty list. This behavior is consistent with the Python `range` function, but differs from the [`tf.range`](https://www.tensorflow.org/api_docs/python/tf/range)
 op, which returns an error for these cases.

#### Examples:

    tf.ragged.range([3, 5, 2]).to_list()

The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors. The vector inputs must all have the same size. Scalar inputs are broadcast to match the size of the vector inputs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `starts` | Vector or scalar `Tensor`. Specifies the first entry for each range if `limits` is not `None`; otherwise, specifies the range limits, and the first entries default to `0`. |
| `limits` | Vector or scalar `Tensor`. Specifies the exclusive upper limits for each range. |
| `deltas` | Vector or scalar `Tensor`. Specifies the increment for each range. Defaults to `1`. |
| `dtype` | The type of the elements of the resulting tensor. If not specified, then a value is chosen based on the other args. |
| `name` | A name for the operation. |
| `row_splits_dtype` | `dtype` for the returned `RaggedTensor`'s `row_splits` tensor. One of [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` of type `dtype` with `ragged_rank=1`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.