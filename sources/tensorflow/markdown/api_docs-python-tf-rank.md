[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/rank#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/rank)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/rank?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/rank#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/rank#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/rank#numpy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.rank Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/rank#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/rank#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/rank#returns)
    
*   [numpy compatibility](https://www.tensorflow.org/api_docs/python/tf/rank#numpy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L879-L912)

Returns the rank of a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.rank`](https://www.tensorflow.org/api_docs/python/tf/rank)

tf.rank(
        input, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor) |

See also [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape)
.

Returns a 0-D `int32` `Tensor` representing the rank of `input`.

#### For example:

# shape of tensor 't' is [2, 2, 3]
    t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
    tf.rank(t)  # 3

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` or `SparseTensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. |     |

numpy compatibility
-------------------

Equivalent to np.ndim

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.