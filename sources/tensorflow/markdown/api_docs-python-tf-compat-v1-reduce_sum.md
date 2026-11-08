[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reduce\_sum Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_sum#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2147-L2224)

Computes the sum of elements across dimensions of a tensor. (deprecated arguments)

tf.compat.v1.reduce_sum(
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
| *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

This is the reduction operation for the elementwise [`tf.math.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

|     |
| --- |
| For example<br>----------- |     |
| >>> # x has a shape of (2, 3) (two rows and three columns):<br>    >>> x = tf.constant([[1, 1, 1], [1, 1, 1]])<br>    >>> x.numpy()<br>    array([[1, 1, 1],<br>           [1, 1, 1]], dtype=int32)<br>    >>> # sum all the elements<br>    >>> # 1 + 1 + 1 + 1 + 1+ 1 = 6<br>    >>> tf.reduce_sum(x).numpy().item()<br>    6<br>    >>> # reduce along the first dimension<br>    >>> # the result is [1, 1, 1] + [1, 1, 1] = [2, 2, 2]<br>    >>> tf.reduce_sum(x, 0).numpy()<br>    array([2, 2, 2], dtype=int32)<br>    >>> # reduce along the second dimension<br>    >>> # the result is [1, 1] + [1, 1] + [1, 1] = [3, 3]<br>    >>> tf.reduce_sum(x, 1).numpy()<br>    array([3, 3], dtype=int32)<br>    >>> # keep the original dimensions<br>    >>> tf.reduce_sum(x, 1, keepdims=True).numpy()<br>    array([[3],<br>           [3]], dtype=int32)<br>    >>> # reduce along both dimensions<br>    >>> # the result is 1 + 1 + 1 + 1 + 1 + 1 = 6<br>    >>> # or, equivalently, reduce along rows, then reduce the resultant array<br>    >>> # [1, 1, 1] + [1, 1, 1] = [2, 2, 2]<br>    >>> # 2 + 2 + 2 = 6<br>    >>> tf.reduce_sum(x, [0, 1]).numpy().item()<br>    6 |     |

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
| The reduced tensor, of the same dtype as the input\_tensor. |     |\
\
numpy compatibility\
-------------------\
\
Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to int64 while tensorflow returns the same dtype as the input.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.