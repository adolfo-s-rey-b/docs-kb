[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reduce\_mean Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_mean#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2504-L2568)

Computes the mean of elements across dimensions of a tensor.

tf.compat.v1.reduce_mean(
        input_tensor,
        axis=None,
        keepdims=None,
        name=None,
        reduction_indices=None,
        keep_dims=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings)<br>    <br>*   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm)<br>    <br>*   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

Reduces `input_tensor` along the dimensions given in `axis` by computing the mean of elements across the dimensions in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

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
| `reduction_indices` | The old (deprecated) name for axis. |\
| `keep_dims` | Deprecated alias for `keepdims`. |\
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
Last updated 2026-11-06 UTC.