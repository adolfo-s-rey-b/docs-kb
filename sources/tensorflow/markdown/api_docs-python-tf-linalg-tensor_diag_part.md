[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.tensor\_diag\_part Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2388-L2430)

Returns the diagonal part of the tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.diag_part`](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part)

tf.linalg.tensor_diag_part(
        input, name=None
    )

This operation returns a tensor with the `diagonal` part of the `input`. The `diagonal` part is computed as follows:

Assume `input` has dimensions `[D1,..., Dk, D1,..., Dk]`, then the output is a tensor of rank `k` with dimensions `[D1,..., Dk]` where:

`diagonal[i1,..., ik] = input[i1, ..., ik, i1,..., ik]`.

For a rank 2 tensor, [`linalg.diag_part`](https://www.tensorflow.org/api_docs/python/tf/linalg/diag_part)
 and [`linalg.tensor_diag_part`](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag_part)
 produce the same result. For rank 3 and higher, linalg.diag\_part extracts the diagonal of each inner-most matrix in the tensor. An example where they differ is given below.

    x = [[[[1111,1112],[1121,1122]],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `input` | A `Tensor` with rank `2k`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A Tensor containing diagonals of `input`. Has the same type as `input`, and rank `k`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.