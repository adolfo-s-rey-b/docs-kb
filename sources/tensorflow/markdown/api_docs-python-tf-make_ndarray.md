[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/make_ndarray)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/make_ndarray?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.make\_ndarray Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/make_ndarray#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_util.py#L756-L859)

Create a numpy ndarray from a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.make_ndarray`](https://www.tensorflow.org/api_docs/python/tf/make_ndarray)

tf.make_ndarray(
        tensor
    )

Create a numpy ndarray with the same shape and data as the tensor.

#### For example:

# Tensor a has shape (2,3)
    a = tf.constant([[1,2,3],[4,5,6]])
    proto_tensor = tf.make_tensor_proto(a)  # convert `tensor a` to a proto tensor
    tf.make_ndarray(proto_tensor) # output: array([[1, 2, 3],\
    #                                              [4, 5, 6]], dtype=int32)
    # output has shape (2,3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A TensorProto. |

|     |
| --- |
| Returns<br>------- |     |
| A numpy array with the tensor contents. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if tensor has unsupported type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.