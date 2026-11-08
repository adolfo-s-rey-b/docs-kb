[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/top_k#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/top_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.top\_k Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/top_k#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/top_k#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5820-L5884)

Finds values and indices of the `k` largest entries for the last dimension.

#### View aliases

**Main aliases**

[`tf.nn.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)
, [`tf.compat.v1.nn.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)

tf.math.top_k(
        input,
        k=1,
        sorted=True,
        index_type=tf.dtypes.int32,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients) |

If the input is a vector (rank=1), finds the `k` largest entries in the vector and outputs their values and indices as vectors. Thus `values[j]` is the `j`\-th largest entry in `input`, and its index is `indices[j]`.

    result = tf.math.top_k([1, 2, 98, 1, 1, 99, 3, 1, 3, 96, 4, 1],

For matrices (resp. higher rank input), computes the top `k` entries in each row (resp. vector along the last dimension). Thus,

    input = tf.random.normal(shape=(3,4,5,6))

The indices can be used to `gather` from a tensor who's shape matches `input`.

    gathered_values = tf.gather(input, indices, batch_dims=-1)

If two elements are equal, the lower-index element appears first.

    result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],

By default, indices are returned as type `int32`, however, this can be changed by specifying the `index_type`.

    result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | 1-D or higher `Tensor` with last dimension at least `k`. |
| `k` | 0-D `Tensor` of type `int16`, `int32` or `int64`. Number of top element to look for along the last dimension (along each row for matrices). |
| `sorted` | If true the resulting `k` elements will be sorted by the values in descending order. |
| `index_type` | Optional dtype for output indices. |
| `name` | Optional name for the operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple with two named fields: |     |
| `values` | The `k` largest elements along each last dimensional slice. |
| `indices` | The indices of `values` within the last dimension of `input`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.