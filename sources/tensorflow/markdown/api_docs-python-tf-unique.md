[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/unique#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/unique)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/unique?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/unique#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unique#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unique#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.unique Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/unique#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/unique#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/unique#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1643-L1685)

Finds unique elements in a 1-D tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.unique`](https://www.tensorflow.org/api_docs/python/tf/unique)

tf.unique(
        x,
        out_idx=tf.dtypes.int32,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet) |

This operation returns a tensor `y` containing all of the unique elements of `x` sorted in the same order that they occur in `x`; `x` does not need to be sorted. This operation also returns a tensor `idx` the same size as `x` that contains the index of each value of `x` in the unique output `y`. In other words:

`y[idx[i]] = x[i] for i in [0, 1,...,rank(x) - 1]`

#### Examples:

# tensor 'x' is [1, 1, 2, 4, 4, 4, 7, 8, 8]
    y, idx = unique(x)
    y ==> [1, 2, 4, 7, 8]
    idx ==> [0, 0, 1, 2, 2, 2, 3, 4, 4]

# tensor 'x' is [4, 5, 1, 2, 3, 3, 4, 5]
    y, idx = unique(x)
    y ==> [4, 5, 1, 2, 3]
    idx ==> [0, 1, 2, 3, 4, 4, 0, 1]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor`. 1-D. |
| `out_idx` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (y, idx). |     |
| `y` | A `Tensor`. Has the same type as `x`. |
| `idx` | A `Tensor` of type `out_idx`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.