[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.reduce\_all Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#used-in-the-notebooks)
    
*   [For example](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#for-example)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L3164-L3209)

Computes [`tf.math.logical_and`](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)
 of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_all`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all)

tf.math.reduce_all(
        input_tensor, axis=None, keepdims=False, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) | *   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention) |

This is the reduction operation for the elementwise [`tf.math.logical_and`](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)
 op.

Reduces `input_tensor` along the dimensions given in `axis`. Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each of the entries in `axis`, which must be unique. If `keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single element is returned.

|     |
| --- |
| For example<br>----------- |     |
| >>> x = tf.constant([[True,  True], [False, False]])<br>    >>> tf.math.reduce_all(x)<br>    <tf.Tensor: shape=(), dtype=bool, numpy=False><br>    >>> tf.math.reduce_all(x, 0)<br>    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False, False])><br>    >>> tf.math.reduce_all(x, 1)<br>    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])> |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_tensor` | The boolean tensor to reduce. |
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
Equivalent to np.all\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.