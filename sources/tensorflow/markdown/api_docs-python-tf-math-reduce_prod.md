[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Freduce_prod&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_prod Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2745-L2791)

Computes [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
 of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_prod`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_prod)

tf.math.reduce_prod(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Sparse weights using structural pruning](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | *   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1)<br>    <br>*   [TensorFlow Distributions: A Gentle Introduction](https://www.tensorflow.org/probability/examples/TensorFlow_Distributions_Tutorial) |

This is the reduction operation for the elementwise [`tf.math.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in `axis`. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

|     |
| --- |
| For example<br>----------- |     |
| >>> x = tf.constant([[1., 2.], [3., 4.]])<br>    >>> tf.math.reduce_prod(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=24.><br>    >>> tf.math.reduce_prod(x, 0)<br>    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)><br>    >>> tf.math.reduce_prod(x, 1)<br>    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],<br>    dtype=float32)> |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | The tensor to reduce. Should have numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced tensor. |     |\
\
numpy compatibility\
-------------------\
\
Equivalent to np.prod\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.