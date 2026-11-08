[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/eye#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/eye)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/eye?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/eye#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/eye#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/eye#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.eye Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/eye#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/eye#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/eye#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg_ops.py#L196-L241)

Construct an identity matrix, or a batch of matrices.

#### View aliases

**Main aliases**

[`tf.linalg.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)
, [`tf.compat.v1.linalg.eye`](https://www.tensorflow.org/api_docs/python/tf/eye)

tf.eye(
        num_rows,
        num_columns=None,
        batch_shape=None,
        dtype=tf.dtypes.float32,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs) | *   [TensorFlow Probability Case Study: Covariance Estimation](https://www.tensorflow.org/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation)<br>    <br>*   [Learnable Distributions Zoo](https://www.tensorflow.org/probability/examples/Learnable_Distributions_Zoo)<br>    <br>*   [A Tour of TensorFlow Probability](https://www.tensorflow.org/probability/examples/A_Tour_of_TensorFlow_Probability)<br>    <br>*   [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://www.tensorflow.org/probability/examples/Bayesian_Gaussian_Mixture_Model)<br>    <br>*   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution) |

See also [`tf.ones`](https://www.tensorflow.org/api_docs/python/tf/ones)
, [`tf.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros)
, [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill)
, [`tf.one_hot`](https://www.tensorflow.org/api_docs/python/tf/one_hot)
.

# Construct one identity matrix.
    tf.eye(2)
    ==> [[1., 0.],\
         [0., 1.]]
    
    # Construct a batch of 3 identity matrices, each 2 x 2.
    # batch_identity[i, :, :] is a 2 x 2 identity matrix, i = 0, 1, 2.
    batch_identity = tf.eye(2, batch_shape=[3])
    
    # Construct one 2 x 3 "identity" matrix
    tf.eye(2, num_columns=3)
    ==> [[ 1.,  0.,  0.],\
         [ 0.,  1.,  0.]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_rows` | Non-negative `int32` scalar `Tensor` giving the number of rows in each batch matrix. |
| `num_columns` | Optional non-negative `int32` scalar `Tensor` giving the number of columns in each batch matrix. Defaults to `num_rows`. |
| `batch_shape` | A list or tuple of Python integers or a 1-D `int32` `Tensor`. If provided, the returned `Tensor` will have leading batch dimensions of this shape. |
| `dtype` | The type of an element in the resulting `Tensor` |
| `name` | A name for this `Op`. Defaults to "eye". |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of shape `batch_shape + [num_rows, num_columns]` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.