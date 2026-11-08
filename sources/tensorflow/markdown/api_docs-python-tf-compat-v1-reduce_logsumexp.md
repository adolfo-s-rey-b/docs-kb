[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Freduce_logsumexp&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reduce\_logsumexp Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3318-L3372)

Computes log(sum(exp(elements across dimensions of a tensor))). (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.reduce_logsumexp`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_logsumexp)

tf.compat.v1.reduce_logsumexp(
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
| *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD) |

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a tensor with a single element is returned.

This function is more numerically stable than log(sum(exp(input))). It avoids overflows caused by taking the exp of large inputs and underflows caused by taking the log of small inputs.

#### For example:

x = tf.constant([[0., 0., 0.], [0., 0., 0.]])
    tf.reduce_logsumexp(x)  # log(6)
    tf.reduce_logsumexp(x, 0)  # [log(2), log(2), log(2)]
    tf.reduce_logsumexp(x, 1)  # [log(3), log(3)]
    tf.reduce_logsumexp(x, 1, keepdims=True)  # [[log(3)], [log(3)]]
    tf.reduce_logsumexp(x, [0, 1])  # log(6)

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
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.