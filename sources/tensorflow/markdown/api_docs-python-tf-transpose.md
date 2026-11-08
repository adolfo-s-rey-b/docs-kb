[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/transpose#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/transpose)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/transpose?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftranspose&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/transpose#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/transpose#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/transpose#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.transpose Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/transpose#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/transpose#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/transpose#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/transpose#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L1826-L1904)

Transposes `a`, where `a` is a Tensor.

tf.transpose(
        a, perm=None, conjugate=False, name='transpose'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer)<br>    <br>*   [MoViNet for streaming action recognition](https://www.tensorflow.org/hub/tutorials/movinet) |

Permutes the dimensions according to the value of `perm`.

The returned tensor's dimension `i` will correspond to the input dimension `perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank of the input tensor. Hence, by default, this operation performs a regular matrix transpose on 2-D input Tensors.

If conjugate is `True` and `a.dtype` is either `complex64` or `complex128` then the values of `a` are conjugated and transposed.

#### For example:

    x = tf.constant([[1, 2, 3], [4, 5, 6]])

Equivalently, you could call `tf.transpose(x, perm=[1, 0])`.

If `x` is complex, setting conjugate=True gives the conjugate transpose:

    x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],\
\
'perm' is more useful for n-dimensional tensors where n > 2:\
\
    x = tf.constant([[[ 1,  2,  3],\
\
As above, simply calling [`tf.transpose`](https://www.tensorflow.org/api_docs/python/tf/transpose)\
 will default to `perm=[2,1,0]`.\
\
To take the transpose of the matrices in dimension-0 (such as when you are transposing matrices where 0 is the batch dimension), you would set `perm=[0,2,1]`.\
\
    tf.transpose(x, perm=[0, 2, 1])\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `a` | A `Tensor`. |\
| `perm` | A permutation of the dimensions of `a`. This should be a vector. |\
| `conjugate` | Optional bool. Setting it to `True` is mathematically equivalent to tf.math.conj(tf.transpose(input)). |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A transposed `Tensor`. |     |\
\
numpy compatibility\
-------------------\
\
In `numpy` transposes are memory-efficient constant time operations as they simply return a new view of the same data with adjusted `strides`.\
\
TensorFlow does not support strides, so `transpose` returns a new tensor with the items permuted.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.