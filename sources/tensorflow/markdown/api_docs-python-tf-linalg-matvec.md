[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.matvec Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3743-L3840)

Multiplies matrix `a` by vector `b`, producing `a` \* `b`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.matvec`](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec)

tf.linalg.matvec(
        a,
        b,
        transpose_a=False,
        adjoint_a=False,
        a_is_sparse=False,
        b_is_sparse=False,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models)<br>    <br>*   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial)<br>    <br>*   [A Tutorial on Multi-Armed Bandits with Per-Arm Features](https://www.tensorflow.org/agents/tutorials/per_arm_bandits_tutorial)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) |

The matrix `a` must, following any transpositions, be a tensor of rank >= 2, with `shape(a)[-1] == shape(b)[-1]`, and `shape(a)[:-2]` able to broadcast with `shape(b)[:-1]`.

Both `a` and `b` must be of the same type. The supported types are: `float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Matrix `a` can be transposed or adjointed (conjugated and transposed) on the fly by setting one of the corresponding flag to `True`. These are `False` by default.

If one or both of the inputs contain a lot of zeros, a more efficient multiplication algorithm can be used by setting the corresponding `a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default. This optimization is only available for plain matrices/vectors (rank-2/1 tensors) with datatypes `bfloat16` or `float32`.

#### For example:

# 2-D tensor `a`
    # [[1, 2, 3],\
    #  [4, 5, 6]]
    a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
    
    # 1-D tensor `b`
    # [7, 9, 11]
    b = tf.constant([7, 9, 11], shape=[3])
    
    # `a` * `b`
    # [ 58,  139]
    c = tf.linalg.matvec(a, b)
    
    
    # 3-D tensor `a`
    # [[[ 1,  2,  3],\
    #   [ 4,  5,  6]],\
    #  [[ 7,  8,  9],\
    #   [10, 11, 12]]]
    a = tf.constant(np.arange(1, 13, dtype=np.int32),
                    shape=[2, 2, 3])
    
    # 2-D tensor `b`
    # [[13, 14, 15],\
    #  [16, 17, 18]]
    b = tf.constant(np.arange(13, 19, dtype=np.int32),
                    shape=[2, 3])
    
    # `a` * `b`
    # [[ 86, 212],\
    #  [410, 563]]
    c = tf.linalg.matvec(a, b)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`, `complex128` and rank > 1. |
| `b` | `Tensor` with same type as `a` and compatible dimensions. |
| `transpose_a` | If `True`, `a` is transposed before multiplication. |
| `adjoint_a` | If `True`, `a` is conjugated and transposed before multiplication. |
| `a_is_sparse` | If `True`, `a` is treated as a sparse matrix. |
| `b_is_sparse` | If `True`, `b` is treated as a sparse matrix. |
| `name` | Name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A `Tensor` of the same type as `a` and `b` where each inner-most vector is the product of the corresponding matrices in `a` and vectors in `b`, e.g. if all transpose or adjoint attributes are `False`:<br><br>`output`\[..., i\] = sum\_k (`a`\[..., i, k\] \* `b`\[..., k\]), for all indices i. |     |
| `Note` | This is matrix-vector product, not element-wise product. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If transpose\_a and adjoint\_a are both set to True. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.