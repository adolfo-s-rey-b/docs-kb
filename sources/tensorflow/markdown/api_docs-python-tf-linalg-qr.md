[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/qr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/qr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/qr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/qr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/qr#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.qr Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/qr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/qr#returns)
    

Computes the QR decompositions of one or more matrices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.qr`](https://www.tensorflow.org/api_docs/python/tf/linalg/qr)
, [`tf.compat.v1.qr`](https://www.tensorflow.org/api_docs/python/tf/linalg/qr)

tf.linalg.qr(
        input: Annotated[Any, TV_Qr_T], full_matrices: bool = False, name=None
    )

Computes the QR decomposition of each inner matrix in `tensor` such that `tensor[..., :, :] = q[..., :, :] * r[..., :,:])`

Currently, the gradient for the QR decomposition is well-defined only when the first `P` columns of the inner matrix are linearly independent, where `P` is the minimum of `M` and `N`, the 2 inner-most dimmensions of `tensor`.

# a is a tensor.
    # q is a tensor of orthonormal matrices.
    # r is a tensor of upper triangular matrices.
    q, r = qr(a)
    q_full, r_full = qr(a, full_matrices=True)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`. A tensor of shape `[..., M, N]` whose inner-most 2 dimensions form matrices of size `[M, N]`. Let `P` be the minimum of `M` and `N`. |
| `full_matrices` | An optional `bool`. Defaults to `False`. If true, compute full-sized `q` and `r`. If false (the default), compute only the leading `P` columns of `q`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (q, r). |     |
| `q` | A `Tensor`. Has the same type as `input`. |
| `r` | A `Tensor`. Has the same type as `input`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.