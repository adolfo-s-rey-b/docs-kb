[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_mean Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2571-L2628)

Computes the mean of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)

tf.math.reduce_mean(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core)<br>    <br>*   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff) | *   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Uncertainty-aware Deep Learning with SNGP](https://www.tensorflow.org/tutorials/understanding/sngp)<br>    <br>*   [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

Reduces `input_tensor` along the dimensions given in `axis` by computing the mean of elements across the dimensions in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

#### For example:

    x = tf.constant([[1., 1.], [2., 2.]])

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
Equivalent to np.mean\
\
Please note that `np.mean` has a `dtype` parameter that could be used to specify the output type. By default this is `dtype=float64`. On the other hand, [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)\
 has an aggressive type inference from `input_tensor`, for example:\
\
    x = tf.constant([1, 0, 1, 0])\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.