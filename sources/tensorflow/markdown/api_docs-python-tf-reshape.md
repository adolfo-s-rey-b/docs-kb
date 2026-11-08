[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/reshape#main-content)

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
    

tf.reshape Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L63-L201)

Reshapes a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)

tf.reshape(
        tensor, shape, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text) |

Given `tensor`, this operation returns a new [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 that has the same values as `tensor` in the same order, except with a new shape given by `shape`.

    t1 = [[1, 2, 3],\
\
The [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)\
 does not change the order of or the total number of elements in the tensor, and so it can reuse the underlying data buffer. This makes it a fast operation independent of how big of a tensor it is operating on.\
\
    tf.reshape([1, 2, 3], [2, 2])\
\
To instead reorder the data to rearrange the dimensions of a tensor, see [`tf.transpose`](https://www.tensorflow.org/api_docs/python/tf/transpose)\
.\
\
    t = [[1, 2, 3],\
\
If one component of `shape` is the special value -1, the size of that dimension is computed so that the total size remains constant. In particular, a `shape` of `[-1]` flattens into 1-D. At most one component of `shape` can be -1.\
\
    t = [[1, 2, 3],\
\
`tf.reshape(t, [])` reshapes a tensor `t` with one element to a scalar.\
\
    tf.reshape([7], []).numpy().item()\
\
#### More examples:\
\
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9]\
\
    t = [[[1, 1], [2, 2]],\
\
    t = [[[1, 1, 1],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `tensor` | A `Tensor`. |\
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Defines the shape of the output tensor. |\
| `name` | Optional string. A name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor`. Has the same type as `tensor`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.