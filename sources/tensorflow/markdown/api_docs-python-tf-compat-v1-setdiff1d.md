[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.setdiff1d Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/setdiff1d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L481-L522)

Computes the difference between two lists of numbers or strings.

tf.compat.v1.setdiff1d(
        x,
        y,
        index_dtype=tf.dtypes.int32,
        name=None
    )

Given a list `x` and a list `y`, this operation returns a list `out` that represents all values that are in `x` but not in `y`. The returned list `out` is sorted in the same order that the numbers appear in `x` (duplicates are preserved). This operation also returns a list `idx` that represents the position of each `out` element in `x`. In other words:

`out[i] = x[idx[i]] for i in [0, 1, ..., len(out) - 1]`

For example, given this input:

x = [1, 2, 3, 4, 5, 6]
    y = [1, 3, 5]

This operation would return:

out ==> [2, 4, 6]
    idx ==> [1, 3, 5]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. 1-D. Values to keep. |
| `y` | A `Tensor`. Must have the same type as `x`. 1-D. Values to remove. |
| `out_idx` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (out, idx). |     |
| `out` | A `Tensor`. Has the same type as `x`. |
| `idx` | A `Tensor` of type `out_idx`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.