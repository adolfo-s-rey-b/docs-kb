[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/parallel_stack#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.parallel\_stack Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1136-L1195)

Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.parallel_stack`](https://www.tensorflow.org/api_docs/python/tf/parallel_stack)

tf.parallel_stack(
        values, name='parallel_stack'
    )

Requires that the shape of inputs be known at graph construction time.

Packs the list of tensors in `values` into a tensor with rank one higher than each tensor in `values`, by packing them along the first dimension. Given a list of length `N` of tensors of shape `(A, B, C)`; the `output` tensor will have the shape `(N, A, B, C)`.

#### For example:

x = tf.constant([1, 4])
    y = tf.constant([2, 5])
    z = tf.constant([3, 6])
    tf.parallel_stack([x, y, z])  # [[1, 4], [2, 5], [3, 6]]

The difference between `stack` and `parallel_stack` is that `stack` requires all the inputs be computed before the operation will begin but doesn't require that the input shapes be known during graph construction.

`parallel_stack` will copy pieces of the input into the output as they become available, in some situations this can provide a performance benefit.

Unlike `stack`, `parallel_stack` does NOT support backpropagation.

This is the opposite of unstack. The numpy equivalent is

tf.parallel_stack([x, y, z]) = np.asarray([x, y, z])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A list of `Tensor` objects with the same shape and type. |
| `name` | A name for this operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | A stacked `Tensor` with the same type as `values`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if executed in eager mode. |

eager compatibility
-------------------

parallel\_stack is not compatible with eager execution.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.