[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Freduce_std&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_std Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2694-L2742)

Computes the standard deviation of elements across dimensions of a tensor.

tf.math.reduce_std(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Playing CartPole with the Actor-Critic method](https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic)<br>    <br>*   [Modeling COVID-19 spread in Europe and the effect of interventions](https://www.tensorflow.org/probability/examples/Estimating_COVID_19_in_11_European_countries)<br>    <br>*   [Barren plateaus](https://www.tensorflow.org/quantum/tutorials/barren_plateaus)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data) |

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

#### For example:

    x = tf.constant([[1., 2.], [3., 4.]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | The tensor to reduce. Should have real or complex type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |\
| `keepdims` | If true, retains reduced dimensions with length 1. |\
| `name` | A name scope for the associated operations (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| The reduced tensor, of the same dtype as the input\_tensor. Note, for `complex64` or `complex128` input, the returned `Tensor` will be of type `float32` or `float64`, respectively. |     |\
\
numpy compatibility\
-------------------\
\
Equivalent to np.std\
\
Please note `np.std` has a `dtype` parameter that could be used to specify the output type. By default this is `dtype=float64`. On the other hand, [`tf.math.reduce_std`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std)\
 has aggressive type inference from `input_tensor`.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.