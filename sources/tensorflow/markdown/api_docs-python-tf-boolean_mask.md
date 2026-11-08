[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/boolean_mask#main-content)

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
    

tf.boolean\_mask Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1539-L1596)

Apply boolean mask to tensor.

tf.boolean_mask(
        tensor, mask, axis=None, name='boolean_mask'
    )

Numpy equivalent is `tensor[mask]`.

In general, `0 < dim(mask) = K <= dim(tensor)`, and `mask`'s shape must match the first K dimensions of `tensor`'s shape. We then have: `boolean_mask(tensor, mask)[i, j1,...,jd] = tensor[i1,...,iK,j1,...,jd]` where `(i1,...,iK)` is the ith `True` entry of `mask` (row-major order). The `axis` could be used with `mask` to indicate the axis to mask from. In that case, `axis + dim(mask) <= dim(tensor)` and `mask`'s shape must match the first `axis + dim(mask)` dimensions of `tensor`'s shape.

See also: [`tf.ragged.boolean_mask`](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask)
, which can be applied to both dense and ragged tensors, and can be used if you need to preserve the masked dimensions of `tensor` (rather than flattening them, as [`tf.boolean_mask`](https://www.tensorflow.org/api_docs/python/tf/boolean_mask)
 does).

#### Examples:

    tensor = [0, 1, 2, 3]  # 1-D example

    tensor = [[1, 2], [3, 4], [5, 6]] # 2-D example

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | N-D Tensor. |
| `mask` | K-D boolean Tensor, K <= N and K must be known statically. |
| `axis` | A 0-D int Tensor representing the axis in `tensor` to mask from. By default, axis is 0 which will mask from the first dimension. Otherwise K + axis <= N. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| (N-K+1)-dimensional tensor populated by entries in `tensor` corresponding to `True` values in `mask`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If shapes do not conform. |

#### Examples:

# 2-D example
    tensor = [[1, 2], [3, 4], [5, 6]]
    mask = np.array([True, False, True])
    boolean_mask(tensor, mask)  # [[1, 2], [5, 6]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.