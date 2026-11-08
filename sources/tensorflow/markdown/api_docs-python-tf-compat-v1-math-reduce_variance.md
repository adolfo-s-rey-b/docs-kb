[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.math.reduce\_variance Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/math/reduce_variance#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2631-L2691)

Computes the variance of elements across dimensions of a tensor.

tf.compat.v1.math.reduce_variance(
        input_tensor, axis=None, keepdims=False, name=None
    )

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
Equivalent to np.var\
\
Please note `np.var` has a `dtype` parameter that could be used to specify the output type. By default this is `dtype=float64`. On the other hand, [`tf.math.reduce_variance`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_variance)\
 has aggressive type inference from `input_tensor`.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.