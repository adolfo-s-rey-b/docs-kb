[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#usage-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reduce\_max Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Usage example](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#usage-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reduce_max#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L2981-L3042)

Computes [`tf.math.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
 of elements across dimensions of a tensor. (deprecated arguments)

tf.compat.v1.reduce_max(
        input_tensor,
        axis=None,
        keepdims=None,
        name=None,
        reduction_indices=None,
        keep_dims=None
    )

This is the reduction operation for the elementwise [`tf.math.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

|     |
| --- |
| Usage example<br>------------- |     |
| >>> x = tf.constant([5, 1, 2, 4])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=int32, numpy=5><br>    >>> x = tf.constant([-5, -1, -2, -4])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=int32, numpy=-1><br>    >>> x = tf.constant([4, float('nan')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=nan><br>    >>> x = tf.constant([float('nan'), float('nan')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=nan><br>    >>> x = tf.constant([float('-inf'), float('inf')])<br>    >>> tf.reduce_max(x)<br>    <tf.Tensor: shape=(), dtype=float32, numpy=inf> |     |

See the numpy docs for `np.amax` and `np.nanmax` behavior.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | The tensor to reduce. Should have real numeric type. |
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